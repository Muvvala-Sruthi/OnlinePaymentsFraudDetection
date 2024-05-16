import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
# Load the model
# Route for rendering the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission and making predictions
@app.route('/predict', methods=['GET', 'POST'])
def predict():   
# If it's a POST request, retrieve input values from the form
    print('prediction')       
    amount = float(request.form.get('amount'))   
    oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
    newbalanceOrig = float(request.form.get('newbalanceOrig'))    
    oldbalanceDest = float(request.form.get('oldbalanceDest'))
    newbalanceDest = float(request.form.get('newbalanceDest'))  

    # Make prediction using the loaded model
    prediction = model.predict([[amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])

    # Render index.html with prediction result
    return render_template('index.html', prediction_text=f'Predicted Fraud: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

