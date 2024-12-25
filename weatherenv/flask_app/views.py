from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
import requests
import os
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def weatherhomepage():
    """Handles current and 5-day weather forecasts."""
    weather_data = None
    forecast_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            api_key = os.getenv('API_KEY')
            base_url = "http://api.openweathermap.org/data/2.5/"
            
            # Fetch current weather
            weather_url = f"{base_url}weather?q={city}&appid={api_key}&units=metric"
            weather_response = requests.get(weather_url)
            
            # Fetch 5-day forecast
            forecast_url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url)

            if weather_response.status_code == 200:
                weather_json = weather_response.json()
                weather_data = {
                    "city": weather_json["name"],
                    "country": weather_json["sys"]["country"],
                    "temperature": weather_json["main"]["temp"],
                    "description": weather_json["weather"][0]["description"],
                    "icon": weather_json["weather"][0]["icon"],
                    "humidity": weather_json["main"]["humidity"],
                    "wind_speed": weather_json["wind"]["speed"]
                }
            else:
                flash("City not found. Please try again.", "danger")
            
            if forecast_response.status_code == 200:
                forecast_json = forecast_response.json()
                forecast_data = {}

                # Group forecast by date
                for item in forecast_json["list"]:
                    date = datetime.fromtimestamp(item["dt"]).strftime('%Y-%m-%d')
                    if date not in forecast_data:
                        forecast_data[date] = {
                            "temperature": [],
                            "description": [],
                            "icon": []
                        }
                    forecast_data[date]["temperature"].append(item["main"]["temp"])
                    forecast_data[date]["description"].append(item["weather"][0]["description"])
                    forecast_data[date]["icon"].append(item["weather"][0]["icon"])

                # Simplify forecast data for each day
                for date in forecast_data:
                    forecast_data[date] = {
                        "avg_temp": round(sum(forecast_data[date]["temperature"]) / len(forecast_data[date]["temperature"]), 1),
                        "description": max(set(forecast_data[date]["description"]), key=forecast_data[date]["description"].count),
                        "icon": forecast_data[date]["icon"][0]  # Use the first icon for simplicity
                    }
            else:
                flash("Unable to fetch forecast data. Please try again later.", "danger")
        else:
            flash("Please enter a city name.", "warning")

    return render_template("weather.html", user=current_user, weather_data=weather_data, forecast_data=forecast_data)
