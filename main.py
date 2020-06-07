import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()]
    features[3] = features[features == 'F'] = 0
    features[3] = features[features == 'M'] = 1
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = "You are diagnosed with Alzheimers" if prediction == 1 else "You donot have Alzheimer's" 
    return render_template('index.html', prediction_text='Your result is :  {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)