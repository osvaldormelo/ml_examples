from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Load Model
model = CelsiusFarenheintModel()  
model.load_state_dict(torch.load('celsius_farenheit_model.pth'))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    # get data from post method
    data = request.get_json(force=True)
    celsius = data['celsius']
    
    # convert to tensor and predict 
    celsius_tensor = torch.FloatTensor([celsius])
    predicted_fahrenheit = model(celsius_tensor.unsqueeze(1)).item()

    # return the prediction
    return jsonify({'fahrenheit': predicted_fahrenheit})

if __name__ == '__main__':
    app.run(debug=True)