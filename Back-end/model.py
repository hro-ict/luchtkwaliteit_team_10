import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from datetime import datetime, date, timedelta
import warnings
warnings.filterwarnings(action='ignore')

test_2=[]

today = datetime.today()
days= 5

# for x in range(1,days+1):
# 	next= today + timedelta(days=x)
# 	for m in range(0,24):
# 		edited= datetime.strftime(next, '%Y-%m-%d')
# 		print(edited+ " {}".format(m))

data = pd.read_csv('./component_data/all_data.csv')
data = data.dropna()


def test(component):
	#de data opsplitsen in train en test sets:
	X = data.drop(['PM10', 'PM25', 'O3', 'NO2'], axis=1)
	y = data[component]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

	lr = LinearRegression()
	lr.fit(X_train, y_train)

	# Genereer de data voor de volgende 5 dagen
	#dates = pd.date_range(start='2023-04-27', end='2023-04-30', freq='D')
	dates= pd.date_range(start='2023-12-12', end='2023-12-17', freq='h')
	next_5_days = pd.DataFrame({'date': dates})

	# Voeg de tijd gerelateerde features toe
	next_5_days['YEAR'] = next_5_days['date'].dt.year
	next_5_days['MONTH'] = next_5_days['date'].dt.month
	next_5_days['DAY'] = next_5_days['date'].dt.day
	next_5_days['HOUR']= next_5_days['date'].dt.hour

	# print(type(next_5_days['DAY']))
	#
	# for x in next_5_days:
	# 	print(next_5_days[x])



	# print("2023", "05", "10", "3")

	# Maak een voorspelling voor de volgende 5 dagen
	# print(next_5_days[['YEAR', 'MONTH', 'DAY', 'HOUR']])

	start_dt = date(2023, 5, 10)
	end_dt = date(2023, 5, 14)

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


	# for x in predictions:
	# 	print(round(x,2))


pm10_predict= test("PM10")
pm25_predict= test("PM25")
o3_predict= test("O3")
no2_predict= test("NO2")

#print(pm10_predict)
#print(pm25_predict)
#print(o3_predict)
#print(no2_predict)

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
	pm25= float(str(pm25_x).strip("[").strip("]"))
	o3= float(str(o3_x).strip("[").strip("]"))
	no2= float(str(no2_x).strip("[").strip("]"))

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
	lki_index= (pm25_index+pm10_index+o3_index+no2_index)/4
	#print(datum, round(lki_index,3))
	if lki_index<=3:
		state= "GOED"
	if lki_index>=4:
		state="MATIG"

	test_2.append({"datum":datum})
	test_2.append({"status": state})

	print(datum, state)



print(test_2)
	# print(datum,pm10_data,pm25_data,o3_data,no2_data)


# for pm10,pm25,o3,no2 in zip(pm10_predict[0],pm25_predict[0],o3_predict[0],no2_predict[0]):
# 	if pm10 <10: pm10_index=1
# 	if pm10>10 and pm10<20: pm10_index=2
# 	if pm10>20 and pm10<30: pm10_index=3
# 	#pm 2.5
# 	if pm25 <10: pm25_index=1
# 	if pm25>10 and pm25<15: pm25_index=2
# 	if pm25>15 and pm25<20: pm25_index=3
# 	#o3
# 	if o3 <15: o3_index=1
# 	if o3>15 and o3<30: o3_index=2
# 	if o3>30 and o3<40: o3_index=3
# 	if o3>40 and o3<60: o3_index=4
# 	#no2
# 	if no2 <10: no2_index=0.5
# 	if no2>10 and no2<20: no2_index=1.5
# 	if no2>20 and no2<30: no2_index=2.5
# 	lki_index= (pm25_index+pm10_index+o3_index+no2_index)/4
# 	print(round(lki_index,1))
# 	if lki_index<=3:
# 		state= "GOED"
# 	if lki_index>=4:
# 		state="MATIG"
#
# 	#print(state)
# 	print(pm10_index)
# 	print(pm25_index)
# 	print(o3_index)
# 	print(no2_index)







