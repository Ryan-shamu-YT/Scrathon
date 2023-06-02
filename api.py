import json
import datetime
from flask import Flask, render_template, make_response, jsonify, url_for
import scratchattach as scratch3

from account import getToken
from account import setToken
from account import AccountExist

# --- System.py ---

from System import getInfo

# --- coin_interaction.py ---

from coin_interaction import addCoin
from coin_interaction import removeCoin
from coin_interaction import getCoinAmount
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



app = Flask('')
page_html = ''



@app.route('/')
@app.route('/home')
def home():
  return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e): # the name is the error
  return make_response(jsonify({'Error': '404'}))

@app.errorhandler(403)
def forbidden(e): # the name is the error
  return make_response(jsonify({'Error': '403'}))

@app.errorhandler(410)
def gone(e): # the name is the error
  return make_response(jsonify({'Error': '410'}))

@app.errorhandler(500)
def internal_server_error(e): # the name is the error
  return make_response(jsonify({'Error': '500'}))

@app.route('/api/user/<username>/pay/<amount>/<UserToPay>/<Token>', methods=["GET", "POST"])
def pay(username, amount, UserToPay, Token):
      if Token == "1019141612131917181416171013181915171614101310171918121314151316105756437266756850732691":
          removeCoin(username, amount)
          addCoin(UserToPay, amount)
      return make_response(jsonify({"message": "success"}))


@app.route('/api/user/<username>/info', methods=["GET"])
def Userinfo(username):
    argument1 = username
    

    user = scratch3.get_user(argument1)
    user.update()
    requestj=requests.get("https://scratchdb.lefty.one/v3/user/info/"+argument1)

    request = requestj['statistics']
    follower = request['followers']
    user_project_count = user.project_count()
    user_fav_projects =['favorites']
    curating_studios = user.studio_count()
    message_count = user.message_count()
    studio_following = user.studio_following_count()
    joined = user.join_date
    country = user.country

    with open("Index.json", "r") as file:
        getIndex = json.load(file)

    i = getIndex.index(argument1.lower())

    with open("coins.json", "r") as file:
        getCoins = json.load(file)

    Info = getCoins[i][argument1.lower()]["Coins"]

    data = [follower, user_project_count, user_fav_projects, curating_studios, message_count, studio_following, joined, country, Info]
    return data


@app.route("/api/registeredList/")
def registeredList():
    with open("Index.json", "r") as file:
        data = json.load(file)
    return make_response(jsonify(data))


@app.route('/dashboard/<key>')
def dashboard(key):
    
    return render_template("dashboard.html", username='name', time=str(datetime.datetime.now()))





app.run(host='0.0.0.0', port=8080)
