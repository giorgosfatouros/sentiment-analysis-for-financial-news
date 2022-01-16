# imports
import json
from flask import Flask, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

model.config.id2label

app = Flask(__name__)


@app.route('/sentiment/', methods=['POST', 'GET'])
def get_text():
    content = request.get_json()
    print(content)
    news = content.get('headline')
    inputs = tokenizer(news, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    # Headline #Positive #Negative #Neutral
    positive = predictions[:, 0].tolist()[0]
    negative = predictions[:, 1].tolist()[0]
    neutral = predictions[:, 2].tolist()[0]

    result = {'Headline': news,
             "Positive": positive,
             "Negative": negative,
             "Neutral": neutral}
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=5000)

