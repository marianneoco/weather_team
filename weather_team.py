from flask import Flask, render_template, request

app = Flask("weather_team")

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London, UK", "units":"metric", "appid":"7854c0a8d8d5259f9efb07224b491299"}
response = requests.get(endpoint, params=payload)
data = response.json()
weather = data["weather"][0]["main"]

@app.route("/")
def main_page():
    return render_template("weather_team.html", weather=weather)

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    return render_template("signup.html")

#@app.route("/goodnight")
#def gn():
    #return "Goodnight"

app.run(debug=True)
