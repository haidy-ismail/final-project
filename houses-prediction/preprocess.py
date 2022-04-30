import numpy as np
import pandas
import joblib


def preprocess_Type(Type):
    if Type.lower() == 't':
        return [1,0]
    if Type.lower() == 'u':
        return [0,1]
    else:
        return [0,0]

def preprocess_Method(Method) :
    if Method.lower() == 's':
        return [1,0,0,0]
    if Method.lower() == 'sa':
        return [0,1,0,0]
    if Method.lower() == 'sp':
        return [0,0,1,0]
    if Method.lower() == 'vb':
        return [0,0,0,1]
    else:
        return [0,0,0,0]
    
    
def Month_name(month):
    if month.lower() == 'august':
        return [1,0,0,0,0,0,0,0,0,0,0]
    if month.lower() == 'december':
        return [0,1,0,0,0,0,0,0,0,0,0]
    if month.lower() == 'february':
        return [0,0,1,0,0,0,0,0,0,0,0]
    if month.lower() == 'january':
        return [0,0,0,1,0,0,0,0,0,0,0]
    if month.lower() == 'july':
        return [0,0,0,0,1,0,0,0,0,0,0]
    if month.lower() == 'june':
        return [0,0,0,0,0,1,0,0,0,0,0]
    if month.lower() == 'march':
        return [0,0,0,0,0,0,1,0,0,0,0]
    if month.lower() == 'may':
        return [0,0,0,0,0,0,0,1,0,0,0]
    if month.lower() == 'november':
        return [0,0,0,0,0,0,0,0,1,0,0]
    if month.lower() == 'october':
        return [0,0,0,0,0,0,0,0,0,1,0]
    if month.lower() == 'September':
        return [0,0,0,0,0,0,0,0,0,0,1]
    else:
        return [0,0,0,0,0,0,0,0,0,0,0]

    
            
def day_name(day) :
    if day.lower() == 'monday' :
        return [1,0,0,0,0,0]
    elif day.lower() == 'saturday' :
        return [0,1,0,0,0,0]
    elif day.lower() == 'sunday' :
        return [0,0,1,0,0,0]
    elif day.lower() == 'thursday' :
        return [0,0,0,1,0,0]
    elif day.lower() == 'tuesday' :
        return [0,0,0,0,1,0]
    elif day.lower() == 'wednesday' :
        return [0,0,0,0,0,1]
    else :
        return [0,0,0,0,0,0]

    
def preprocess(data) :
    
    Distance = data['Distance']
    
    Postcode = data['Postcode']
    
    Car = data['Car']
    
    Landsize = data['Landsize']
    
    BuildingArea = data['BuildingArea']
    
    YearBuilt = data['YearBuilt']
    
    Propertycount = data['Propertycount']
    
    year = data['year']
    
    house_rooms = data['house_rooms']
    
    Method = preprocess_Method(data['Method'])
    
    Type = preprocess_Type(data['Type'])
    
    day = day_name(data['day'])
    
    month = Month_name(data['month'])
    
    final_data = [Distance,Postcode,Car,Landsize,BuildingArea,YearBuilt,Propertycount,year,house_rooms]+Method+Type+day+month
    
    return np.array(final_data)
    
    