import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

def filter_data_by_date(data, specific_date):
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if 'issuance_date' exists in the DataFrame columns
    if 'issuance_date' not in df.columns:
        raise KeyError("The 'issuance_date' column is missing from the data.")
    
    # Convert 'issuance_date' to a datetime format, coerce errors, and filter by the specific date
    df['issuance_date'] = pd.to_datetime(df['issuance_date'], errors='coerce', format="%m/%d/%Y")
    
    # Filter the DataFrame to only include rows that match the specific date
    filtered_df = df[df['issuance_date'] == specific_date]
    
    return filtered_df

def save_data_to_excel(df, specific_date):
    # Define the filename with the date in 'YYYY-MM-DD' format
    filename = f"DOB_permits_data_{specific_date.strftime('%Y-%m-%d')}.xlsx"
    
    # Save the DataFrame to an Excel file
    df.to_excel(filename, index=False)
    st.success(f"Data successfully saved to {filename}")

def fetch_and_display_data(selected_date):
    # Format the date in MM/DD/YYYY format (for the API query)
    formatted_date = selected_date.strftime("%m/%d/%Y")

    # Modify the API URL to apply the specific date filter
    base_url = f"https://data.cityofnewyork.us/resource/ipu4-2q9a.json?$where=issuance_date = '{formatted_date}'"

    try:
        # Fetching the data from the API for the selected date
        response = requests.get(base_url)
        data = response.json()

        # Continue only if data is available
        if data:
            # Convert the data to a DataFrame
            df = pd.DataFrame(data)

            # Check if the filtered data is not empty
            if not df.empty:
                # Display the data as a table
                st.dataframe(df)

                # Save the data to an Excel file
                save_data_to_excel(df, selected_date)
            else:
                st.warning(f"No records found for {selected_date.strftime('%Y-%m-%d')}")
        else:
            st.warning("The API returned no data.")

    except KeyError as e:
        st.error(f"A KeyError occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("DOB Permits Data Fetcher")
    st.subheader("Select a date to fetch DOB Permits data:")

    # Add a date picker
    selected_date = st.date_input("Select Date", value=datetime.now())

    # Button to fetch data
    if st.button("Get Data"):
        fetch_and_display_data(selected_date)

# Main entry point
if __name__ == "__main__":
    main()