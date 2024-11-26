import streamlit as st
import os
from PIL import Image

# Define the main show_page function
def show_page():
    # Set up page configuration for Streamlit
    # st.set_page_config(
    #     page_title="Stock Evaluation Hub",
    #     page_icon="📈",
    #     layout="wide",
    # )

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Candlestick Patterns", "Investment Theories"])

    # Candlestick Patterns Section
    if page == "Candlestick Patterns":
        st.title("Candlestick Patterns")

        # Path to the folder containing your predefined images
        image_folder = "candles_pictures"

        # Dictionary for patterns and their explanations
        pattern_explanations = {
    "Hammer": [
        "A small body at the top of the candle with a long lower shadow, signaling a reversal to the upside.",
        "It indicates that despite the selling pressure, the buyers managed to push the price up, hinting at a potential upward trend."
    ],
    "Inverse Hammer": [
        "A small body at the bottom of the candle with a long upper shadow, signaling a potential reversal to the upside.",
        "It shows that although sellers pushed the price down, buyers gained control and tried to push it higher."
    ],
    "Bullish Engulfing": [
        "A bullish pattern where a smaller red candle is followed by a larger green one, indicating a shift from bearish to bullish sentiment.",
        "It signals that the bulls have taken control, suggesting an upward trend."
    ],
    "Evening Star": [
        "A three-candle pattern that starts with a large green candle, followed by a small-bodied candle (indicating indecision), and then a large red candle, signaling a reversal to the downside.",
        "It suggests that the buying pressure has been exhausted and a downward trend may begin."
    ],
    "Morning Star": [
        "A three-candle pattern where a large red candle is followed by a small-bodied candle, and then a large green candle, signaling a potential reversal to the upside.",
        "It indicates that the selling pressure has subsided and a bullish trend may start."
    ],
    "Piercing Line": [
        "A two-candle bullish reversal pattern where a red candle is followed by a green candle that opens below the previous candle's low but closes above the midpoint of the red candle.",
        "It suggests that buying pressure has overcome the selling pressure, indicating a potential upward movement."
    ],
    "Three White Soldiers": [
        "A bullish pattern consisting of three consecutive long green candles with small wicks, where each candle opens within the body of the previous one.",
        "It indicates strong buying pressure and a potential trend reversal to the upside."
    ],
    "Three Black Crows": [
        "A bearish pattern consisting of three consecutive long red candles with small wicks, where each candle opens within the body of the previous one.",
        "It signals strong selling pressure, indicating a potential reversal to the downside."
    ]
}



        col1, col2 = st.columns(2)

        # Display Bullish Patterns
        with col1:
            st.subheader("Bullish Patterns")

            for pattern_name in ["Hammer", "Inverse Hammer", "Bullish Engulfing","Morning Star","Piercing Line","Three White Soldiers"]:
                with st.expander(pattern_name):
                    st.markdown(f"<h3 style='font-size: 28px;'>{pattern_name}</h3>", unsafe_allow_html=True)
                    st.write(pattern_explanations[pattern_name][0])
                    st.write(pattern_explanations[pattern_name][1])
                    image_path = os.path.join(image_folder, f"{pattern_name.replace(' ', '_')}.png")
                    if os.path.exists(image_path):
                        img = Image.open(image_path).resize((300, 200))
                        st.image(img, caption=pattern_name)

        # Display Bearish Patterns
        with col2:
            st.subheader("Bearish Patterns")

            for pattern_name in ["Hanging Man", "Shooting Star", "Bearish Engulfing", "Evening Star", "Three Black Crows"]:
                with st.expander(pattern_name):
                    st.markdown(f"<h3 style='font-size: 28px;'>{pattern_name}</h3>", unsafe_allow_html=True)
                    st.write(pattern_explanations.get(pattern_name, ["", ""])[0])
                    st.write(pattern_explanations.get(pattern_name, ["", ""])[1])
                    image_path = os.path.join(image_folder, f"{pattern_name.replace(' ', '_')}.png")
                    if os.path.exists(image_path):
                        img = Image.open(image_path).resize((300, 200))
                        st.image(img, caption=pattern_name)

    # Stock Evaluation Theories Section
    elif page == "Investment Theories":
        st.title("Investment Theories")

        theories = {
            "Warren Buffett's 8.1 Theory": "This theory focuses on investing in businesses with sustainable competitive advantages, often called economic moats. Buffett emphasizes understanding the intrinsic value of a company and investing only when the market undervalues it.",
            "Peter Lynch's PEG Ratio": "Lynch advocates using the Price/Earnings to Growth (PEG) ratio to evaluate a stock's true value. A PEG ratio below 1 indicates undervalued growth potential.",
            "Benjamin Graham's Value Investing": "Graham's approach involves identifying stocks trading below their intrinsic value. He suggests looking for companies with strong fundamentals and a margin of safety.",
            "Philip Fisher's Scuttlebutt Method": "Fisher's strategy involves gathering information from various sources, including competitors, customers, and suppliers, to understand a company's long-term prospects.",
            "John Templeton's Diversification": "Templeton recommends diversifying across different asset classes and geographies to reduce risk and increase potential returns.",
            "Ray Dalio's All-Weather Portfolio": "Dalio's portfolio is designed to perform well in various economic environments, with diversified assets like stocks, bonds, gold, and commodities.",
            
        }

        for name, explanation in theories.items():
            with st.expander(name):
                st.markdown(f"<h3 style='font-size: 28px;'>{name}</h3>", unsafe_allow_html=True)
                st.write(explanation)
