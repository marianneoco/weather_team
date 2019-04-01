from flask import Flask, render_template, request, url_for

app = Flask("weather_team")

import requests
import tweepy
import json

auth = tweepy.OAuthHandler("LcPXgIykI9tA3mjzLDvVeRV9E","jSznFDi0f0lrJQgFdnFUFXm9OC8rzxzrj5y3fEZelYAf0yuyvD")
auth.set_access_token ("813484763013115904-cNhrOkjXag5kyyXnaWxVOCkqprPpXUy", "1DXNDmeY6gSXFYWZZTsAhStrIMLDwVlAuZIQqBDIWrWOG")
twitter_api = tweepy.API(auth)
the_tweets = twitter_api.search(
    q = "@TfL")
tweet = the_tweets[0].text
print json.dumps(tweet)
twitter = json.dumps(tweet)

trends = twitter_api.trends_place(id = 44418)
print trends[0]["trends"][0]["name"]
number_one_trend = trends[0]["trends"][0]["name"]

#def process_or_store(tweet):
    #for tweet in the_tweets:
        #process_or_store(tweet._json)

#print the_tweets[0].text.encode("utf8")
#twitter = the_tweets[0].text.encode("utf8")

#the_tweets[0].user.name + ":" +
#+ tweet.text.encode('utf8')
#locale = 51.51770,-0.11352)

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London, UK", "units":"metric", "appid":"7854c0a8d8d5259f9efb07224b491299"}
response = requests.get(endpoint, params=payload)
data = response.json()
weather = data["weather"][0]["main"]
temp = data["main"]["temp"]
print data

@app.route("/")
def main_page():
    return render_template("weather_team.html", weather=weather, temp=temp, twitter=twitter, number_one_trend=number_one_trend)

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
    return render_template("signup.html", name=name, weather=weather, temp=temp, twitter=twitter, number_one_trend=number_one_trend)

#@app.route("/goodnight")
#def gn():
    #return "Goodnight"

app.run(debug=True)
