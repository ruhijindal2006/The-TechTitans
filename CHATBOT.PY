from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to access API from different origin if needed

# Set your OpenAI API key here or load from environment
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('home.html')  # if you're serving the HTML from Flask

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'reply': 'Message is empty.'}), 400

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_message}],
            max_tokens=150
        )

        bot_reply = response.choices[0].message.content.strip()
        return jsonify({'reply': bot_reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({'reply': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
