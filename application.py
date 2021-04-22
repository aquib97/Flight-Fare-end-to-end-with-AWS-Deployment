from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import sklearn
import pickle
import pandas as pd


application = Flask(__name__)
model = pickle.load(open("flight_fare.pkl", "rb"))

@application.route("/")       #decorater
@cross_origin()
def home():
    return render_template("home.html")

@application.route("/predict", methods= ['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        #Departure
        date_dep = request.form['Dep_Time']
        Journey_Day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        #print("Journey_Date:",Journey_day,Journey_month)

        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min= int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        #Arrival
        date_arr = request.form['Arrival_Time']
        Arr_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arr_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        #Duration
        dur_hour = abs(Arr_hour - Dep_hour)
        dur_min = abs(Arr_min - Dep_min)

        #Total Stops
        Total_Stops= int(request.form["stops"])

        #Airline
        airline = request.form["airline"]
        if (airline == "Jet Airways"):
            Jet_Airways = 1
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Indigo"):
            Jet_Airways = 0
            Indigo = 1
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Air India"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Multiple carriers"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Multiple carriers Premium economy"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "SpiceJet"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 1
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Truejet"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 1
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Vistara"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 1
            Go_Air = 0
            Vistara_Premium_economy = 0
        elif (airline == "Go Air"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 1
            Vistara_Premium_economy = 0
        elif (airline == "Vistara Premium economy"):
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air = 0
            Vistara_Premium_economy = 1
        else:
            Jet_Airways = 0
            Indigo = 0
            AirIndia = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Go_Air =0
            Vistara_Premium_economy = 0

        Source = request.form['Source']
        if (Source == "Delhi"):
            s_Delhi = 1
            s_Chennai = 0
            s_Kolkata = 0
            s_Mumbai = 0
        elif (Source == "Chennai"):
            s_Delhi = 0
            s_Chennai = 1
            s_Kolkata = 0
            s_Mumbai = 0
        elif (Source == "Kolkata"):
            s_Delhi = 0
            s_Chennai = 0
            s_Kolkata = 1
            s_Mumbai = 0
        elif (Source == "Mumbai"):
            s_Delhi = 0
            s_Chennai = 0
            s_Kolkata = 0
            s_Mumbai = 1
        else:
            s_Delhi = 0
            s_Chennai = 0
            s_Kolkata = 0
            s_Mumbai = 0

        Destination = request.form['Destination']
        if (Destination == "Delhi"):
            d_Delhi = 1
            d_Cochin = 0
            d_Kolkata = 0
            d_Hyderabad  = 0
            d_New_Delhi = 0
            d_Bangalore = 0
        elif (Source == "Cochin"):
            d_Delhi = 0
            d_Cochin = 1
            d_Kolkata = 0
            d_Hyderabad = 0
            d_New_Delhi = 0
            d_Bangalore = 0
        elif (Source == "Kolkata"):
            d_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 1
            d_Hyderabad = 0
            d_New_Delhi = 0
            d_Bangalore = 0
        elif (Source == "Hyderabad"):
            d_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Hyderabad = 1
            d_New_Delhi = 0
            d_Bangalore = 0
        elif (Source == "New Delhi"):
            d_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_New_Delhi = 1
            d_Bangalore = 0
        elif (Source == "Bangalore"):
            d_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_New_Delhi = 0
            d_Bangalore = 1
        else:
            d_Delhi = 0
            d_Cochin = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_New_Delhi = 0
            d_Bangalore = 0

        prediction = model.predict([[
            Total_Stops,
            Journey_Day,  Journey_month,
            Dep_hour, Dep_min,
            Arr_hour, Arr_min,
            dur_hour, dur_min,
            AirIndia, Jet_Airways,
            SpiceJet, Trujet, Vistara,
            Vistara_Premium_economy, Indigo,
            Multiple_carriers_Premium_economy, Multiple_carriers,
            Go_Air,
            s_Kolkata, s_Delhi, s_Mumbai, s_Chennai,
            d_Kolkata, d_Hyderabad, d_Bangalore,
            d_Delhi, d_New_Delhi, d_Cochin
        ]])

        output = round(prediction[0],2)

        return render_template("home.html",prediction_text="Your Flight is Rs. {}". format(output))

    return render_template("home.html")



if __name__ == "__main__":
    application.run(debug =True)