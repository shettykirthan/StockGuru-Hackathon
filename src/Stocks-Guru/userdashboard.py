import streamlit as st
import yfinance as yf
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from utils.appwrite_client import fetch_followed_stocks
import pandas as pd
import os

# Fetch news from yfinance
def fetch_yfinance_news(ticker):
    try:
        stock = yf.Ticker(ticker)
        news = stock.get_news()
        # Extract necessary details
        filtered_news = [
            {
                "title": article.get("title", "No title available"),
                "publisher": article.get("publisher", "Unknown source"),
                "link": article.get("link", "#")
            }
            for article in news
        ]
        return filtered_news
    except Exception as e:
        st.error(f"An error occurred while fetching news: {e}")
        return []


# Plot stock chart
def plot_stock(ticker, period, chart_type):
    try:
        data = yf.Ticker(ticker).history(period=period, interval="1d")
        if data.empty:
            st.error(f"No stock data available for ticker: {ticker}")
            return None

        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=[f'{ticker} Stock Price Chart', 'Trading Volume'],
            row_heights=[0.7, 0.3]
        )

        if chart_type == "Candlestick":
            fig.add_trace(
                go.Candlestick(
                    x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name="Candlestick"
                ),
                row=1, col=1
            )
        elif chart_type == "Line":
            fig.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data['Close'],
                    mode='lines',
                    name="Close Price",
                    line=dict(color='blue')
                ),
                row=1, col=1
            )
        elif chart_type == "Mountain":
            fig.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data['Close'],
                    fill='tozeroy',
                    mode='lines',
                    name="Close Price",
                    line=dict(color='skyblue')
                ),
                row=1, col=1
            )

        fig.add_trace(
            go.Bar(
                x=data.index,
                y=data['Volume'],
                name="Volume",
                marker=dict(color='gray')
            ),
            row=2, col=1
        )

        fig.update_layout(
            title=f'{ticker} Stock Data',
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis2_title="Date",
            yaxis2_title="Volume",
            template="plotly_dark",
            hovermode="x unified",
            showlegend=True,
            height=800,
            xaxis_rangeslider_visible=True
        )

        return fig
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None


# Stock page function
def stock_page():
    if st.sidebar.button("Back to Dashboard", key="back_to_dashboard"):
        st.session_state.selected_ticker = None  # Clear the selected stock
        st.session_state.selected_name = None
        st.session_state.user_id = None  # Clear user-related data if necessary
        show_page()  # Call the main dashboard function to show the dashboard again

    st.sidebar.header("Stock Page")
    selected_ticker = st.session_state.get("selected_ticker", "N/A")

    if selected_ticker == "N/A":
        st.error("No stock selected!")
        return

    st.markdown(f"## Details for {selected_ticker}")
    selected_ticker = st.session_state.get('selected_ticker', 'AAPL')
    timespan = st.sidebar.selectbox("Select Time Span", ["1y", "5y", "10y", "Max"])
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Candlestick", "Line", "Mountain"], index=0)

    try:
        stock = yf.Ticker(selected_ticker)
        info = stock.info

        if not info:
            st.error("No information available for the selected stock.")
            return

        # Display stock information
        st.markdown(f"### {info.get('longName', selected_ticker)} Stock Information")
        col1, col2, col3 = st.columns(3)
        col1.metric("Market Cap", f"{info.get('marketCap', 'N/A'):,}")
        col2.metric("PE Ratio", round(info.get('trailingPE', 0), 2))
        col3.metric("52 Week High", f"{info.get('fiftyTwoWeekHigh', 'N/A')}")

        # Plot stock chart
        fig = plot_stock(selected_ticker, timespan, chart_type)
        if fig:
            st.plotly_chart(fig)

        # Display financial data and other details (same as before)
        with st.expander("Company About"):
            st.markdown(
                f"""
                #### {info.get('longName', 'Company')}
                *Sector:* {info.get('sector', 'N/A')}  
                *Industry:* {info.get('industry', 'N/A')}  
                *Business Summary:*  
                {info.get('longBusinessSummary', 'No information available.')[:500]}...  
                [Learn more]({info.get('website', '#')})
                """
            )

        # Additional financials and recommendations
        st.markdown("### Financial Data")
        income_statement = stock.financials
        if not income_statement.empty:
            st.subheader("Income Statement")
            st.dataframe(income_statement)

        balance_sheet = stock.balance_sheet
        if not balance_sheet.empty:
            st.subheader("Balance Sheet")
            st.dataframe(balance_sheet)

        cash_flow = stock.cashflow
        if not cash_flow.empty:
            st.subheader("Cash Flow")
            st.dataframe(cash_flow)

    
        st.markdown("### Stock Recommendations & Earnings Estimate")
        col1, col2 = st.columns(2)

        recommendations = stock.recommendations
        if not recommendations.empty:
            with col1:
                st.subheader("Stock Recommendations")
                st.dataframe(recommendations)

        earnings_estimate = stock.earnings_estimate
        if isinstance(earnings_estimate, pd.DataFrame) and not earnings_estimate.empty:
            with col2:
                st.subheader("Earnings Estimate")
                st.dataframe(earnings_estimate)

        analyst_targets = stock.analyst_price_targets
        if isinstance(analyst_targets, pd.DataFrame) and not analyst_targets.empty:
            st.subheader("Analyst Price Targets")
            st.dataframe(analyst_targets)

    except Exception as e:
        st.error(f"There is no such stock available, Check Ticker Name")
    

    st.markdown("### Latest News")
    news_data = fetch_yfinance_news(selected_ticker)
    if news_data:
        for index, article in enumerate(news_data):
            st.markdown(
                f"""
                <div style="background-color: #262730; padding: 15px; border-radius: 5px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                    <h4>{index + 1}. {article['title']}</h4>
                    <p><strong>Source:</strong> {article['publisher']}</p>
                    <p><a href="{article['link']}" target="_blank">Read full article</a></p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No news articles available for this stock.")


# Main dashboard
def show_page():
    if "username" not in st.session_state or "email" not in st.session_state:
        st.error("You must log in first!")
        st.stop()

    user_id = st.session_state.get("user_id")
    username = st.session_state.username
    email = st.session_state.email

    followed_stocks = fetch_followed_stocks(user_id)

    

    st.title(f"Welcome {username}!")


    st.markdown("## Followed Stocks")
    for stock in followed_stocks:
        stock_name = stock['stock_name']
        stock_ticker = stock['stock_ticker']

        with st.container():
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin-bottom: 15px; background-color: #262730; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                    <h2 style="margin: 0; color: #FFFFFF;">{stock_name}</h2>
                    <p style="margin: 5px 0 10px; color: #666;">
                        <strong>Ticker:</strong> {stock_ticker}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button("View Details", key=f"{stock_ticker}_details"):
                st.session_state.selected_ticker = stock_ticker
                stock_page()
            

if __name__ == "_main_":
    show_page()