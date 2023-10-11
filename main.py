import streamlit as st
import pandas as pd
import numpy as np
import time

# Create a list of users and their passwords
users = ["admin", "user"]
passwords = ["admin123", "user123"]

# Create a function to check if the user is logged in
def is_logged_in():
    if "username" not in st.session_state:
        return False
    else:
        return True

# Create a function to show the login form
def show_login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and password == passwords[users.index(username)]:
            st.session_state["username"] = username
            st.session_state["role"] = "admin" if username == "admin" else "user"
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Create a function to show the admin dashboard
def show_admin_dashboard():
    st.title("Admin Dashboard")

    # Load the telemetry data
    telemetry_data = pd.read_csv("telemetry_data.csv")

    # Show the telemetry data in a table
    st.table(telemetry_data)

# Create a function to show the user dashboard
def show_user_dashboard():
    st.title("User Dashboard")

    # Load the telemetry data
    telemetry_data = pd.read_csv("telemetry_data.csv")

    # Filter the telemetry data to only show the current user's data
    #telemetry_data = telemetry_data[telemetry_data["username"] == st.session_state["username"]]

    # Show the telemetry data in a table
    st.table(telemetry_data)

# Check if the user is logged in
if not is_logged_in():
    show_login_form()
else:
    # Show the admin dashboard if the user is an admin
    if st.session_state["role"] == "admin":
        show_admin_dashboard()
    # Show the user dashboard if the user is a user
    else:
        show_user_dashboard()