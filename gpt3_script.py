import openai
import os
from flask import Flask, request

# Set the OpenAI API key and engine from environment variables
openai.api_key = os.environ['OPENAI_API_KEY']
openai_engine = os.environ.get('OPENAI_ENGINE', 'text-davinci-002')

# Create a pre-initialized OpenAI instance
openai_instance = openai.api.OpenAI()

# Create a dictionary to store cached responses
response_cache = {}

app = Flask(__name__)

@app.route('/generate_text')
def generate_text():
    prompt = request.args.get('prompt')
    
    # Check the cache for the response
    if prompt in response_cache:
        return response_cache[prompt]
    
    # If the response is not in the cache, make a new request to the OpenAI API
    completions = openai_instance.Completion.create(
        engine=openai_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    message = completions.choices[0].text.strip()
    
    # Add the response to the cache
    response_cache[prompt] = message
    
    return message

if __name__ == '__main__':
    app.run(debug=True)
