
#https://sparkbyexamples.com/pandas/pandas-write-to-excel-with-examples/
import requests as req
import json
import pandas as pd
import numpy as np
import os

url= "https://api.luchtmeetnet.nl/open_api/stations/NL01485/measurements?page=1&order=&order_direction=&formula=PM10"
url2="https://iq.luchtmeetnet.nl/open_api/measurements?station_number=NL01485&formula=&page=1&order_by=timestamp_measured&order_direction=asc&end=2022-09-03T09:00:00&start=2019-09-03T09:00:00"
url3="https://iq.luchtmeetnet.nl/open_api/measurements?station_number=NL01485&formula=&page=1&order_by=timestamp_measured&order_direction=asc&start=2019-09-03T00:00:00"
url4="https://iq.luchtmeetnet.nl/open_api/measurements?station_number=NL01485&formula=&page=1&order_by=timestamp_measured&order_direction=asc&start=2018-12-01T09%3A00%3A00Z&end=2022-12-02T09%3A00%3A00Z"

data= req.get(url4)

print(data.json())
# curl --location -g '{{url}}/open_api/measurements?start=2018-12-01T09%3A00%3A00Z&end=2018-12-02T09%3A00%3A00Z&station_number=&formula=&page=&order_by=timestamp_measured&order_direction=desc'

#station_values =  ['Station','Component','Value','Date', 'Time']
station_list = []
component_list = []
value_list= []
date_list= []
time_list= []
duration = ['5o Days','35 Days',np.nan,'30 Days', '30 Days']
discount = [2000,1000,800,500,800]
station_values= ['Station','Component','Value','Date', 'Time']


for x in data.json()["data"]:
	if x["formula"]=="PM10":
		split_text= x["timestamp_measured"][0:16].split("T")
		time= split_text[1]
		split_date= split_text[0]
		day= split_date.split("-")[2]
		month= split_date.split("-")[1]
		year= split_date.split("-")[0]
		date= "{}-{}-{}".format(day,month,year)
		#print(date)
		station_list.append("Hoogvliet")
		component_list.append("PM10")
		value_list.append(x["value"])
		date_list.append(date)
		time_list.append(time)
df = pd.DataFrame(list(zip(station_list, component_list, value_list, date_list, time_list)), columns=station_values)
#print(df)
df.to_excel('lucht_data.xlsx', index = False, sheet_name='Lucht_Data')



