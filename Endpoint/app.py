import json
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from flask import Flask, request, jsonify
from functions import functions

app = Flask(__name__)

def load_model_and_tokenizer(model_dir):
    model = BertForSequenceClassification.from_pretrained(model_dir)
    tokenizer = BertTokenizer.from_pretrained(model_dir)
    return model, tokenizer

def classify_input(user_input, model, tokenizer, data):
    encoded_dict = tokenizer.encode_plus(
        user_input,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_attention_mask=True,
        return_tensors="pt"
    )

    input_ids = encoded_dict["input_ids"]
    attention_mask = encoded_dict["attention_mask"]
    
    with torch.no_grad():
        output = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = output.logits
    
    predicted_label_index = str(torch.argmax(logits).item())
    predicted_function = data.get(predicted_label_index, "Unknown Function")
    r = functions.getting_function(value=str(predicted_function))
    return r

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    user_input = request.json.get('user_input')
    if user_input is None:
        return jsonify({'error': 'Missing user_input parameter'}), 400
    
    model_dir = "./trained_Classification_model/"
    model, tokenizer = load_model_and_tokenizer(model_dir)
    with open("Label_to_Function.json", "r") as mappings:
        data = json.load(mappings)
    
    try:
        predicted_function = classify_input(user_input, model, tokenizer, data)
        result = {'predicted_function': predicted_function}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
