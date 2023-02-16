import os
import openai
from flask import Flask, request

# Add your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

# Set the OpenAI engine name from the environment variable
openai_engine = os.environ.get("OPENAI_ENGINE", "text-davinci-002")

app = Flask(__name__)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    completions = openai.Completion.create(
        engine=openai_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
