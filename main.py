from flask import Flask, render_template, request
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
    return render_template('index.html', city=city, resp=resp, temp=temp)
@app.route('/results', methods=['GET','POST'])
def results():
    input_city = request.form.get('city')
    resp = query_api(input_city)
    temp = resp["main"]["temp"]
    error = None


    if resp:
        if len(resp) <= 2:
            error = resp['message']
        else:
            temp = resp["main"]["temp"]
            city= resp["name"]
            country = resp["sys"]["country"]
            weather = resp["weather"][0]["description"]
            icon = resp["weather"][0]["icon"]
            icon_url = f"https://openweathermap.org/img/wn/@2x.png".format(icon)
            humidity = resp["main"]["humidity"]
            feels_like = resp["main"]["feels_like"]
    return render_template('index.html', temp=temp, resp=resp, city=city, error=error, country=country, weather=weather, icon_url=icon_url, humidity=humidity, feels_like=feels_like)

if __name__ == '__main__':
    app.run(debug=True)