import openai
from decouple import config

# Set the API key properly using the latest OpenAI client setup
api_key = config("OPENAI_API_KEY")
client = openai.Client(api_key=api_key)

def generate_embedding(text):
    """
    Generates an embedding vector for the given text using OpenAI.
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"  # Corrected parameter from engine to model
    )
    return response.data[0].embedding  # Updated way to access embedding

def get_openai_response(prompt, max_tokens=150, temperature=0.7):
    """
    Generates a response from OpenAI API based on the prompt.
    """
    try:
        response = client.chat.completions.create(  # Use chat.completions.create for chat models
            model="gpt-4o",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Error generating response."