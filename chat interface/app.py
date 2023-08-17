from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    user_input = request.json.get('user_input')
    if user_input is None:
        return jsonify({'error': 'Missing user_input parameter'}), 400
    
    classify_url = "http://localhost:5001/classify"
    classify_data = {"user_input": user_input}
    classify_response = requests.post(classify_url, json=classify_data)
    
    if classify_response.status_code == 200:
        result = classify_response.json()
        predicted_function = result.get("predicted_function")
        return jsonify({'predicted_function': predicted_function})
    else:
        return jsonify({'error': 'Failed to classify'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5002)
