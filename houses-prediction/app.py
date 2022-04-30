import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np

app = Flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model = joblib.load('Models/dep.h5')


@app.route('/') 
def index() :
    return render_template('index.html')


@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST' :
        Distance = request.form['Distance']
        Postcode = request.form['Postcode']
        Car = request.form['Car']
        Landsize = request.form['Landsize']
        BuildingArea = request.form['BuildingArea']
        YearBuilt = request.form['YearBuilt']
        Propertycount = request.form['Propertycount']
        year = request.form['year']
        house_rooms = request.form['house_rooms']
        Method = request.form['Method']
        Type = request.form['Type']
        day = request.form['day']
        month = request.form['month']

    data = {'Distance' : Distance, 'Postcode' : Postcode, 'Car' : Car, 
            'Landsize' : Landsize, 'BuildingArea' : BuildingArea, 'YearBuilt' : YearBuilt, 'Propertycount' : Propertycount,
            'year':year ,'house_rooms':house_rooms ,'Method':Method ,'Type':Type,'day':day ,'month':month}

    final_data = preprocess.preprocess(data)
    prediction = model.predict(scaler.transform([final_data]))[0]
    
    # return str(round(prediction))
    return render_template('prediction.html', predicted_price = str(round(prediction)))



if __name__ == '__main__' :
    app.run(debug = True)