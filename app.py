from flask import Flask, render_template, request, jsonify
from utils import make_predictions


app = Flask(__name__, static_folder="static")  

@app.route("/")
def home():
    return render_template("index.html", email="", prediction=None)

@app.route("/predict", methods=['POST'])
def predict():
    email = request.form.get('content')
    prediction = make_predictions(email)
    return render_template("index.html", prediction=prediction, email=email)


@app.route("/api/predict",methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    email = data['content']
    prediction = make_predictions(email)
    return jsonify({'Prediction':prediction, 'Email':email})


if __name__ == '__main__':
    app.run(debug=True)
