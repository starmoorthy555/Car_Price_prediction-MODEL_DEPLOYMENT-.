from flask import Flask,render_template,request
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

model  = pickle.load(open('model.pkl.','rd'))

app = Flask(__name__)

@app.route('/',methods='GET')
def home():
    return render_template('index.html')

@app.route('/predict',methods='POST')
def predict():
    if request == 'POST':
        Year = int(request.form['Year'])
        Present_Price = int(request.form['Present_Price'])
        Kms_Driven =  int(request.form['Kms_Driven'])
        kms_Driven2 = np.log(Kms_Driven)
        Owners = int(request.form['Owners'])

        if(Fuel_Type == Petrol:)
            Fuel_Type_petrol = 1
            Fuel_Type_Diesel = 0

        else:
            Fuel_Type_petrol = 0
            Fuel_Type_Diesel = 1

        Seller_Type_Individual = int(request.form('Seller_Type_Individual'))
        if (Seller_Type_Individual == 'Manual'):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        Transmission_Mannual = int(request.form('Transmission_Mannual'))
        if (Transmission_Mannual == 'Mannual'):
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0

predict = model.predict([[Present_Price,Kms_Driven,Year,Owners,Fuel_Type,Seller_Type_Individual,Transmission_Mannual]])
output  = round(predict)
print(output)










if __name__ == ('__main__'):
    app.run(debug=True)
