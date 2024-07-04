from flask import Flask, request, render_template, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = load_model('my_model1.h5')

# Initialize the scaler (replace with actual scaler if needed)
scaler = StandardScaler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    location = 1 if data['location'] == 'premium' else 0
    size = float(data['size'])
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])

    # Prepare the input data
    input_data = np.array([[location, size, bedrooms, bathrooms]])
    input_data_scaled = scaler.transform(input_data)

    # Predict the price
    predicted_price = model.predict(input_data_scaled)
    price = predicted_price[0][0]

    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
