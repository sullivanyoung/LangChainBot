from flask import Flask, request, jsonify
from memorybot import get_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

## test route to ensure endpoint is setup correctly
# @app.route('/hello-world', methods=['GET']) 
# def helloWorld():    
#     return 'Hi'

## get bot response for returning answers
@app.route('/get-bot-response', methods=['POST']) 
def get_bot_response():
    try:
        input_data = request.get_json()
        result = get_response(input_data['question'])
        return jsonify(answer=result)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(error=str(e)), 500