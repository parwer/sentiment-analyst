import json
from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.utils.data_utils import pad_sequences
from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

model = load_model('model.h5')
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

translator = Translator()


def translate(txt):
    x = translator.translate(txt, dest='en')
    return x.text


def predict(txt):
    predict = pad_sequences(tokenizer.texts_to_sequences([txt]), maxlen=30)
    return predict


def sent_fn(x):
    x = x*4
    if x > 2.7:
        return "pos"
    elif x < 1.4:
        return "neg"
    else:
        return "neu"


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        q = request.get_json()
        print(q)
        q = translate(q['message'])
        pre = predict(q)
        x = model.predict(pre)
        print(x)
        return jsonify(
            pred=sent_fn(x)
        ), 201
    else:
        return jsonify(message="err"), 200


if __name__ == '__main__':
    app.run(port=5000)