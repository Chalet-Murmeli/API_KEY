import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]

def main():
    st.title("Meine API-App")
    response = requests.get(
        "https://example.com/api",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    st.write(response.json())

if __name__ == "__main__":
    main()
