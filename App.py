from flask import Flask, render_template, request
import joblib
import numpy as np
import locale
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load(open('model.joblib', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.template_filter('intcomma')
def intcomma(value):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.format_string("%d", value, grouping=True)

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    features = np.array(features).reshape(1, -1)
    predicted_price = model.predict(features)
    result = int(np.round(predicted_price))
    return render_template('index.html', predicted_price=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
