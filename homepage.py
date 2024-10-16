import streamlit as st

st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center;'>HIRANI ENGINEERING</h1>", unsafe_allow_html=True)
    st.title("NYC DOB Data Fetcher")
    st.subheader("Select which data you would like to explore:")

    # Center align buttons using HTML
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Buttons for navigating to DOB NOW and DOB Permits pages
    if st.button("DOB NOW"):
        st.write("Redirecting to DOB NOW page...")
        st.experimental_set_query_params(page="dob_now")
    elif st.button("DOB Permits"):
        st.write("Redirecting to DOB Permits page...")
        st.experimental_set_query_params(page="dob_permits")

    # Back button to return to home
    if st.button("Back to Home"):
        st.experimental_set_query_params(page="home")

    st.markdown("</div>", unsafe_allow_html=True)

# Main entry point
if __name__ == "__main__":
    main()