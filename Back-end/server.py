from flask import Flask
from flask import render_template, request, redirect, session, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from datetime import datetime, date, timedelta
from model import Air_predict



@app.route("/")
def main():
    #test= Air_predict(2023,10,10,2023,10,15)
    # print(test.all_predictions)
    # print(test.predict_all())
    # teamplate= "<h3>Visit for documantation:
    a=  "<a href= 'https://github.com/hro-ict/luchtkwaliteit_team_10/blob/main/README.md'><h1 style='text-align:center; margin-top:100px'>Click here for API documantation</h1></a>"
    
    return render_template("./index.html")


@app.route("/get_data", methods=["POST"])
def data():
    
    # response = make_response()
    # response.headers.add("Access-Control-Allow-Origin", "*")
    data= request.get_json()
    print("END: ",data["end_date"])
    print("START: ", data["start_date"])
    start_date= data["start_date"].split("-")
    end_date= data["end_date"].split("-")
    start_year= int(start_date[0])
    start_month= int(start_date[1])
    start_day= int(start_date[2])

    

    end_year= int(end_date[0])
    end_month= int(end_date[1])
    end_day= int(end_date[2])

    #date difference

    d0 = date(start_year, start_month, start_day)
    d1 = date(end_year, end_month, end_day)
    delta = d1 - d0
    difference= delta.days
    print("Difference: ", delta.days)
    print(type(difference))
    #date difference

    test= Air_predict(
     start_year, start_month, start_day,
     end_year, end_month, end_day
    )
    #print(test.predict_all())
    # return {"response": data}
    if difference<=5:
        return {"data": test.predict_all()}
    else:
        return {"error": "MAX 5 DAYS"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3389, debug=True)
