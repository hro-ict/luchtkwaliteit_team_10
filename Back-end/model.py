import pandas as pd
import json
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from datetime import datetime, date, timedelta
from random import randrange
import warnings
warnings.filterwarnings(action='ignore')
import pickle
class Air_predict:
	def __init__(self, 
	start_year, 
	start_month, 
	start_day, 
	end_year, 
	end_month, 
	end_day):
		# self.start= start
		# self.end= end
		self.start_year= start_year
		self.start_month= start_month
		self.start_day= start_day
		self.end_year= end_year
		self.end_month= end_month
		self.end_day= end_day
		self.all_predictions = []
		self.data = pd.read_csv('component_data/all_data.csv').dropna()
		


	def test(self,component):
		X = self.data.drop(['PM10', 'PM25', 'O3', 'NO2'], axis=1)
		y = self.data[component]

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

		lr = LinearRegression()
		lr.fit(X_train, y_train)

		# #save model
		# filename = 'lki_model.sav'
		# pickle.dump(lr, open(filename, 'wb'))

		# Genereer de data voor de volgende 5 dagen
		#dates = pd.date_range(start='2023-04-27', end='2023-04-30', freq='D')
		dates= pd.date_range(start='2023-12-12', end='2023-12-17', freq='h')
		next_5_days = pd.DataFrame({'date': dates})

		# Voeg de tijd gerelateerde features toe
		next_5_days['YEAR'] = next_5_days['date'].dt.year
		next_5_days['MONTH'] = next_5_days['date'].dt.month
		next_5_days['DAY'] = next_5_days['date'].dt.day
		next_5_days['HOUR']= next_5_days['date'].dt.hour
		# start_dt = date(2023, 5, 10)
		# end_dt = date(2023, 5, 14)

		start_dt = date(self.start_year,
		 self.start_month, 
		 self.start_day)
		end_dt = date(self.end_year, 
		self.end_month, 
		self.end_day)

		# difference between current and previous date
		delta = timedelta(days=1)

		# store the dates between two dates in a list
		dates = []
		predictions = []

		dictionary= {}

		while start_dt <= end_dt:
			# add current date to list by converting  it to iso format
			dates.append(start_dt.isoformat())
			# increment start date by timedelta
			start_dt += delta


		#predictions = lr.predict(next_5_days[['YEAR', 'MONTH', 'DAY', 'HOUR']])

		for x in dates:
			for y in range(0, 24):
				date_split = x.split("-")
				year = int(date_split[0])
				month = int(date_split[1])
				day = int(date_split[2])
				hour = y
				dat= lr.predict([[year,month,day,hour]])
				datum= "{}-{}-{} {}".format(year,month,day,hour)
				dictionary[datum]=dat
		return dictionary
	def predict_all(self):
		state=""
		pm10_predict= self.test("PM10")
		pm25_predict= self.test("PM25")
		o3_predict= self.test("O3")
		no2_predict= self.test("NO2")
		for (pm10_x,pm10_y), (pm25_x,pm25_y), (o3_x,o3_y), (no2_x,no2_y) in zip(
				(zip(pm25_predict.values(),pm25_predict.keys())),
				(zip(pm10_predict.values(),pm10_predict.keys())),
				(zip(o3_predict.values(),o3_predict.keys())),
				(zip(no2_predict.values(),no2_predict.keys())),
		):
			pm25_index=0
			pm10_index=0
			o3_index=0
			no2_index=0
			datum= pm10_y+":00"
			pm10= float(str(pm10_x).strip("[").strip("]"))
			pm25= float(str(pm25_x).strip("[").strip("]"))+randrange(0,20)
			o3= float(str(o3_x).strip("[").strip("]"))+randrange(0,20)
			no2= float(str(no2_x).strip("[").strip("]"))+randrange(0,20)
			
			if pm10 <10: pm10_index=1
			if pm10>10 and pm10<20: pm10_index=2
			if pm10>20 and pm10<30: pm10_index=3
			#pm 2.5
			if pm25 <10: pm25_index=1
			if pm25>10 and pm25<15: pm25_index=2
			if pm25>15 and pm25<20: pm25_index=3
			#o3
			if o3 <15: o3_index=1
			if o3>15 and o3<30: o3_index=2
			if o3>30 and o3<40: o3_index=3
			if o3>40 and o3<60: o3_index=4
			#no2
			if no2 <10: no2_index=0.5
			if no2>10 and no2<20: no2_index=1.5
			if no2>20 and no2<30: no2_index=2.5
			lki_index= (pm25_index+pm10_index+o3_index+no2_index)/4+randrange(0,5)
			#print(datum, round(lki_index,3))
			if lki_index<=3:
				state= "GOED"
			if lki_index>=4:
				state="MATIG"
            
			datum_split= datum.split(" ")
			datum= datum_split[0]
			hour= datum_split[1]

			self.all_predictions.append({"date":datum, "hour":hour, "value": lki_index, "state": state})
			# self.all_predictions.append({"status": state})
		#print(self.all_predictions)
		json_date= "{}-{}-{}".format(self.start_year,
		self.start_month, self.start_day
		
		)
		with open("test.json") as read_file:
			dat= json.load(read_file)
			file_date= dat[0]["date"]
			if (json_date==file_date):
				return dat
			else:
				with open("test.json", "w+") as lki_file:
					json.dump(self.all_predictions, lki_file)
				return self.all_predictions
		

			#print(datum, state)





