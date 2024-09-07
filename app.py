import streamlit as st
import torch
import backend
import pandas as pd

def main():
    st.title("Semantic Search Application")
    search_obj = backend.SSearch()
    # Create a text input for the search query
    query = st.text_input("Enter your search query")

    # Create a submit button
    if st.button("Submit"):
        results = search_obj.search(query)
       # print(results)
        # Display the results (adjust the display logic as needed)
        df = pd.DataFrame(results)
        st.title("Semantic Search Results")
        st.table(df)
        #st.write(results)

if __name__ == "__main__":
    main()