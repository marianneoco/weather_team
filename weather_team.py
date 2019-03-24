from flask import Flask, render_template, request

app = Flask("weather_team")

@app.route("/")
def main_page():
    return render_template("weather_team.html")
#HTML for main page goes WeatherTeam

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    return render_template("signup.html")

#@app.route("/goodnight")
#def gn():
    #return "Goodnight"

app.run(debug=True)
