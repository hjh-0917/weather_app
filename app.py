from flask import Flask,request, render_template, redirect, url_for
import requests
import os
api_key = os.environ.get("api_key")
city_dic = {"서울":"Seoul","부산":"Busan","대구":"Daegu","인천":"Incheon","광주":"Gwangju","대전":"Daejeon","울산":"Ulsan","제주도":"Jeju","강원도":"Gangwon-do"}

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def search ():  
    if request.method == "POST":
        city_name = request.form["city"]
        if city_name in city_dic:
            city = city_dic[city_name]
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"
                respon = requests.get(url)
                data = respon.json()
                temp = data["main"]["temp"]
                return render_template("weather.html", t = temp)
            except:
                return "날씨 정보 가져오기 실패"
        else:
            return "지원하지 않는 지역입니다"
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
