import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

def fetch_and_save_data(selected_date):
    # Base URL for the selected date
    base_url = f"https://data.cityofnewyork.us/resource/rbx6-tga4.json?$where=issued_date >= '{selected_date}T00:00:00' AND issued_date < '{selected_date}T23:59:59'"
    
    try:
        # Fetching the data
        response = requests.get(base_url)
        data = response.json()

        # Converting the data into a pandas DataFrame
        df = pd.DataFrame(data)

        # If 'issued_date' exists, process and save
        if 'issued_date' in df.columns:
            df['issued_date'] = pd.to_datetime(df['issued_date'], errors='coerce')
            df['modified_issued_date'] = df['issued_date'].dt.date
            df = df[['modified_issued_date'] + [col for col in df.columns if col != 'modified_issued_date']]

            # Display the data as a table
            st.dataframe(df)

            # Save the Excel file in the current folder
            filename = f"NYC_DOB_NOW_{selected_date}.xlsx"
            filepath = os.path.join(os.getcwd(), filename)
            df.to_excel(filepath, index=False)

            # Success message
            st.success(f"Data saved to {filename}")
        else:
            st.warning(f"No 'issued_date' data available for {selected_date}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("DOB NOW Data Fetcher")
    st.subheader("Select a date to fetch DOB NOW data:")

    # Add a date picker
    selected_date = st.date_input("Select Date", value=datetime.now())

    # Button to fetch data
    if st.button("Get Data"):
        formatted_date = selected_date.strftime('%Y-%m-%d')
        fetch_and_save_data(formatted_date)

# Main entry point
if __name__ == "__main__":
    main()