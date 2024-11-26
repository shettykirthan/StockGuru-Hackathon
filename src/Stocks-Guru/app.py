import streamlit as st
from utils.appwrite_client import account  # Ensure this imports your Appwrite client correctly
import uuid

# Now import your modules for pages
import google_news, market, userdashboard, information, StockGuru_chat, Research_chat

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")

    # Dropdown for Login/Signup or Navigation
    if "logged_in" in st.session_state and st.session_state.logged_in:
        # If the user is logged in, show the navigation options
        page = st.selectbox(
            "Choose a page", 
            [
                "Market", 
                "Google News", 
                "Dashboard", 
                "Learn",
                "Stock Research Chat",
                "StockGuru Chat",
            ]
        )
    else:
        # If the user is not logged in, provide Login/Signup dropdown
        auth_option = st.selectbox("Choose an option", ["Login", "Sign Up"])
        page = "Login" if auth_option == "Login" else "Sign Up"

# Login/Signup Page Logic
def user_auth_page():
    st.title("User Authentication")

    # Show the selected page based on the dropdown
    if page == "Login":
        # Login Section
        st.subheader("Log In")
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log In")

            if submitted:
                try:
                    # Email and password-based session creation using Appwrite's login API
                    session = account.create_email_password_session(email=email, password=password)
                    # Get the $id from the session response
                    st.session_state.user_id = session['userId']  # Use the existing user ID from the session
                    st.session_state.logged_in = True
                    st.session_state.email = email
                    # Add a username (you might want to fetch this from your user profile)
                    st.session_state.username = email.split('@')[0]  # Use part of email as username
                    st.success("Logged in successfully!")
                    st.rerun()  # Rerun the app to update the page
                except Exception as e:
                    st.error(f"Login failed: {e}")
    
    elif page == "Sign Up":
        # Signup Section
        st.subheader("Sign Up")
        with st.form("signup_form"):
            username = st.text_input("Username")
            new_email = st.text_input("New Email")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            signup_submitted = st.form_submit_button("Sign Up")

            if signup_submitted:
                if new_password != confirm_password:
                    st.error("Passwords do not match.")
                    return
                try:
                    # Create user account via Appwrite's signup API
                    # Make sure to call `account.create` correctly by passing email, password, and name (username)
                    account.create(user_id=str(uuid.uuid4()), name=username, email=new_email, password=new_password)
                    
                    st.success("Account created successfully! Please log in.")
                    
                    # Redirect to login page after successful signup
                    st.session_state.page = "Login"  # Change the page to Login in session state
                    st.session_state.logged_in = False  # Ensure logged_in is False
                    st.experimental_rerun()  # Rerun the app to update the page and show login

                except Exception as e:
                    st.error(f"Signup failed: {e}")

# Page-specific logic
if not ("logged_in" in st.session_state and st.session_state.logged_in):
    user_auth_page()  # Show the login/signup page if the user is not logged in
elif page == "Market":
    market.show_page()  # Show Market page if logged in
elif page == "Google News":
    google_news.show_page()  # Show Google News page if logged in
elif page == "Dashboard":
    userdashboard.show_page()  # Show Dashboard page if logged in
elif page == "Learn":
    information.show_page()  # Show Learn page if logged in
elif page == "Stock Research Chat":
    Research_chat.show_page()  # Show Research Chat page if logged in
elif page == "StockGuru Chat":
    StockGuru_chat.show_page()  # Show StockGuru Chat page if logged in
