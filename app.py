import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests, json
from sklearn.preprocessing import StandardScaler
import warnings 
warnings.filterwarnings('ignore')

# Create a Flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("model.pkl", "rb"))
standard_scaler = pickle.load(open('scaler.pkl','rb'))

@app.route("/")
def HOME():
    return render_template("index.html")

@app.route("/predict", methods=["POST","GET"])
def predict():
    query = str(request.form.get("food_string"))
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'NSmmbao+4W6FEzsYy+YQfg==U1MJeNXVMcUUwGEt'})

    response_data = json.loads(response.text)
   
    fat = response_data[0]['fat_total_g']
    protein = response_data[0]['protein_g']
    carbs = response_data[0]['carbohydrates_total_g']
    features = [np.array([100,protein, fat, carbs])]
    features_std = standard_scaler.transform(features)
    prediction = model.predict(features_std)
    output = round(prediction[0], 2)
    return render_template("index.html", prediction_text="The healthiness score is {}".format(output*2))

if __name__ == "__main__":
    app.run()
