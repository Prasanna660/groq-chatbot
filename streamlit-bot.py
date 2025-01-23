import streamlit as st
from groq import Groq
from apikey import api_key

# Initialize the Groq client
client = Groq(api_key=api_key)

# Streamlit app
def main():
    st.title("Language Model Interaction")
    st.write("Ask a question and get a response from the Groq-powered language model!")

    # Input box for the user question
    user_input = st.text_area("Enter your query:", placeholder="Type something...")

    # Button to trigger API call
    if st.button("Submit"):
        if user_input.strip():
            with st.spinner("Processing..."):
                try:
                    # API call to Groq
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": user_input,
                            }
                        ],
                        model="llama-3.3-70b-versatile",
                    )

                    # Extract and display the response
                    response = chat_completion.choices[0].message.content
                    st.success("Response from the model:")
                    st.write(response)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query before submitting.")

if __name__ == "__main__":
    main()
