from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('flood_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(input_features)])
    if prediction[0] == 1:
        result = "YES, a flood is predicted."
    else:
        result = "NO, no flood is expected."
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)