from flask import Flask, render_template, request, url_for

app = Flask("weather_team")

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London, UK", "units":"metric", "appid":"7854c0a8d8d5259f9efb07224b491299"}
response = requests.get(endpoint, params=payload)
data = response.json()
weather = data["weather"][0]["main"]
temp = data["main"]["temp"]

@app.route("/")
def main_page():
    return render_template("weather_team.html", weather=weather, temp=temp)

#subscribe button redirects to subscribe form pages
@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('subscribe'))

    # show the form, it wasn't submitted
    return render_template('subscribe.html')




#form subscribe
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    name = form_data["name"]
    return render_template("signup.html", name=name)

#@app.route("/goodnight")
#def gn():
    #return "Goodnight"

app.run(debug=True)
