import streamlit as st
import requests

# Streamlit UI
st.title("Health Advice Chatbot")
st.write("Get preliminary health advice and information based on your queries. Note: This is not a substitute for professional medical advice.")

# Query type selection
query_type = st.selectbox("Select Query Type", ["Symptom Checker", "Preventive Measures", "General Health Advice", "Medical Terms", "First Aid"])

# User input
user_input = st.text_area("Enter your query here:")

if st.button("Submit"):
    if user_input:
        # Generate appropriate message based on query type
        if query_type == "Symptom Checker":
            user_message = f"User has described the following symptoms: {user_input}. What could be the potential conditions?"
        elif query_type == "Preventive Measures":
            user_message = f"Provide preventive measures for the following: {user_input}."
        elif query_type == "General Health Advice":
            user_message = f"Give general health advice on the topic: {user_input}."
        elif query_type == "Medical Terms":
            user_message = f"Explain the following medical term: {user_input}."
        elif query_type == "First Aid":
            user_message = f"Provide first aid tips for: {user_input}."

        # Prepare data for API request
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant providing health advice."},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": 150
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer open-ai-key"  # Replace with your actual API key
        }

        # Make API request
        response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)

        if response.ok:
            response_data = response.json()
            # Extract and display the response
            st.write("Response:")
            st.write(response_data['choices'][0]['message']['content'].strip())
        else:
            st.error(f"Failed to get response from OpenAI API. Status code: {response.status_code}, Response: {response.text}")
    else:
        st.error("Please enter a query.")
