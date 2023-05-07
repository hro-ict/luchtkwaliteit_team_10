from flask import Flask
from flask import render_template, request, redirect, session
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# #mail
# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = 'd8ec82679ae6a5'
# app.config['MAIL_PASSWORD'] = '34a725c5807738'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = False
# mail = Mail(app)
# #mail


# from pymongo import MongoClient
# client = MongoClient('localhost', 8444)
# db = client.sites
# sites = db.sites
# ip= db.ip
# users= db.users
# tokens= db.tokens
# feedbacks= db.feedbacks



# def create_token(length):
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     token = ''.join(random.choice(letters) for i in range(length))
#     token+= str(random.randrange(1,9999))
#     return token


# def update_projects(username):
#     project_counter=0
#     all_sites= sites.find()
#     for x in all_sites:
#         if x["user"]==username:
#             project_counter+=1
#     session["projects"]= project_counter




@app.route("/")
def main():
    #return render_template("home2.html")
    #return render_template("home2.html")
    #return render_template("index.html")
    return "Hello world"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3389, debug=True)
