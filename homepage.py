import streamlit as st

st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center;'>HIRANI ENGINEERING</h1>", unsafe_allow_html=True)
    st.title("NYC DOB Data Fetcher")
    st.subheader("Select which data you would like to explore:")

    # Center align buttons using HTML
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Initialize session state for page navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Buttons for navigating to DOB NOW and DOB Permits pages
    if st.button("DOB NOW"):
        st.session_state.page = "dob_now"
    elif st.button("DOB Permits"):
        st.session_state.page = "dob_permits"

    # Back button to return to home
    if st.button("Back to Home"):
        st.session_state.page = "home"

    st.markdown("</div>", unsafe_allow_html=True)

    # Page routing logic
    if st.session_state.page == "dob_now":
        st.write("Redirecting to DOB NOW page...")
        # Here, you would include or import the DOB NOW page code
    elif st.session_state.page == "dob_permits":
        st.write("Redirecting to DOB Permits page...")
        # Here, you would include or import the DOB Permits page code

# Main entry point
if __name__ == "__main__":
    main()