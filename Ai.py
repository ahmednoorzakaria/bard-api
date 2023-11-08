import os
from bardapi import Bard
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Set your Bard API key as an environment variable
os.environ['_BARD_API_KEY'] = 'cwhRP_i7DX6MIH9aO2DGK7FwH0BUsT1gr-obbBpL6SivoQb-LAoyVlUs_zlO7KpJ8iHcMA.'  # Replace 'xxxxx' with your actual API key

# Create a Bard instance and provide the API key as a token
bard = Bard(token=os.environ.get('_BARD_API_KEY'))

@app.route('/get_bard_response', methods=['POST'])
def get_bard_response():
    try:
        data = request.get_json()
        user_message = data.get('message')
        response = Bard().get_answer(str(user_message))["content"]
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100)
