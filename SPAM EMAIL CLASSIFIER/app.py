import streamlit as st
import joblib
import pandas as pd

# Load the trained model from the file
model = joblib.load('model.pkl')

# Load the TF-IDF vectorizer from the file
vectorizer = joblib.load('vectorizer.pkl')

# Create a Streamlit web app
st.title("Spam Email Classifier")

# Add a text input box
email_text = st.text_area("Enter your email text here:")

# Add a button to perform classification
if st.button("Classify"):
    # Perform classification when the button is clicked
    if email_text:
        # Transform the input text using the loaded vectorizer
        features = vectorizer.transform([email_text])

        # Make a prediction using the loaded model
        prediction = model.predict(features)[0]

        # Display the classification result
        if prediction == 0:
            st.error("This is a spam email.")
        else:
            st.success("This is a ham (non-spam) email.")
    else:
        st.warning("Please enter an email text.")
