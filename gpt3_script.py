import openai
from flask import Flask, request

# Add your OpenAI API key
openai.api_key = "API"

app = Flask(__name__)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

if __name__ == '__main__':
    app.run(debug=True)
