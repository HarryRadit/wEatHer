from flask import Flask, render_template
import requests
app = Flask(__name__)
API_KEY =  "4fa75398e2e9e87be55ebe6d07a2b2ae"
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
        return data
    except Exception as e:
        print(e)
        return None

@app.route('/')
def index():
    city = "Depok"
    resp = query_api(city)
    temp = resp["main"]["temp"]
    return render_template('index.html', city=city, resp=resp)

if __name__ == '__main__':
    app.run(debug=True)