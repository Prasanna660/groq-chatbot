import streamlit as st
from groq import Groq
from apikey import api_key

# Initialize the Groq client
client = Groq(api_key=api_key)

# Streamlit app for generating text advertisements
def main():
    st.title("Advertisement generator")
    st.write("Generate creative text advertisements for your product or service!")

    # Input fields for user
    product_name = st.text_input("Product/Service Name", placeholder="Enter your product or service name...")
    target_audience = st.text_input("Target Audience", placeholder="Describe your target audience...")
    key_features = st.text_area("Key Features or Benefits", placeholder="List the main features or benefits...")

    # Submit button
    if st.button("Generate Advertisement"):
        if product_name.strip() and target_audience.strip() and key_features.strip():
            with st.spinner("Generating your advertisement..."):
                try:
                    # Prepare the prompt
                    prompt = (
                        f"Generate a catchy and creative advertisement for a product/service named '{product_name}'. "
                        f"The target audience is: {target_audience}. "
                        f"Here are the key features or benefits of the product/service: {key_features}."
                    )

                    # API call to Groq
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": prompt,
                            }
                        ],
                        model="llama-3.3-70b-versatile",
                    )

                    # Extract and display the response
                    advertisement = chat_completion.choices[0].message.content
                    st.success("Generated Advertisement:")
                    st.write(advertisement)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in all the fields before generating the advertisement.")

if __name__ == "__main__":
    main()
