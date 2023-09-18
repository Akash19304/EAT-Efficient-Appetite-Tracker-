import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler

# Create a Flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("model.pkl", "rb"))
standard_scaler = pickle.load(open('scaler.pkl','rb'))

@app.route("/")
def HOME():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    features_std = standard_scaler.transform(features)
    prediction = model.predict(features_std)
    output = round(prediction[0], 2)
    return render_template("index.html", prediction_text="The healthiness score is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)
