# from flask import Flask, render_template, redirect, url_for, flash, request, session, jsonify
# import os
# import datetime
# import requests

# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY')

# users = {}
# # api_key = os.getenv('API_KEY')  


# @app.route('/')
# def home():
#     return redirect(url_for('login'))


# # Login route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Validate user
#         if username in users and users[username] == password:
#             flash("Login successful!", "success")
#             return redirect(url_for('welcome', username=username))
#         else:
#             flash("Invalid username or password.", "danger")
#     return render_template('login.html')

# # Signup route
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         password_repeat = request.form['password-repeat']

#         # Check if passwords match
#         if password != password_repeat:
#             flash("Passwords do not match!", "danger")
#         elif email in users:
#             flash("User already exists!", "warning")
#         else:
#             # Store user
#             users[email] = password
#             flash("Account created successfully! Please log in.", "success")
#             return redirect(url_for('login'))
#     return render_template('signup.html')

# # Welcome route
# @app.route('/welcome/<username>')
# def welcome(username):
#     if request.method == 'POST':
#         city = request.form['city']
#         if not city:
#             flash("City is required.", "danger")
#         else:
#             try:
#                 current_weather = get_current_weather(city, api_key)
#                 forecast_data = get_5_day_forecast(city, api_key)
#                 processed_forecast = process_forecast_data(forecast_data)
#                 return render_template('weather.html', username=username, current_weather=current_weather, forecast=processed_forecast)
#             except Exception as e:
#                 flash(f"Error fetching weather data: {str(e)}", "danger")
#     return render_template('weather.html', username=username)

# # # RESTful API route to fetch weather data
# # @app.route('/weather', methods=['GET'])
# # def api_weather():
# #     city = request.form['city']
# #     if not city:
# #         return jsonify({"error": "City is required."}), 400

# #     try:
# #         current_weather = get_current_weather(city, api_key)
# #         forecast_data = get_5_day_forecast(city, api_key)
# #         processed_forecast = process_forecast_data(forecast_data)
# #         return jsonify({
# #             "current_weather": current_weather,
# #             "forecast": processed_forecast
# #         })
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # # Route to handle the weather page and form
# # @app.route('/weather', methods=['GET', 'POST'])
# # def weather_page():  # Renamed function
# #     weather_data = None
# #     if request.method == 'POST':
# #         city = request.form['city']
# #         if not city:
# #             flash("City is required.", "danger")
# #         else:
# #             try:
# #                 current_weather = get_current_weather(city, api_key)
# #                 forecast_data = get_5_day_forecast(city, api_key)
# #                 processed_forecast = process_forecast_data(forecast_data)
# #                 weather_data = {
# #                     "current_weather": current_weather,
# #                     "forecast": processed_forecast
# #                 }
# #             except Exception as e:
# #                 flash(f"Error fetching weather data: {str(e)}", "danger")

# #     return render_template('weather.html', weather_data=weather_data)

# # Utility functions
# def get_current_weather(city, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         weather_data = response.json()
#         icon_code = weather_data["weather"][0]["icon"]
#         icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
#         weather_data["icon_url"] = icon_url
#         return weather_data
#     else:
#         return {"error": f"Failed to fetch weather data: {response.status_code}"}

# def get_5_day_forecast(city, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Failed to fetch forecast data: {response.status_code}"}

# def process_forecast_data(forecast_data):
#     forecast_list = forecast_data.get('list', [])
#     daily_data = {}
#     for forecast in forecast_list:
#         date = datetime.datetime.fromtimestamp(forecast['dt']).date()
#         if date not in daily_data:
#             daily_data[date] = {
#                 "temps": [],
#                 "icons": [],
#                 "descriptions": [],
#             }
#         daily_data[date]["temps"].append(forecast["main"]["temp"])
#         daily_data[date]["icons"].append(forecast["weather"][0]["icon"])
#         daily_data[date]["descriptions"].append(forecast["weather"][0]["description"])

#     # Calculate averages and most common values
#     for date, data in daily_data.items():
#         data["avg_temp"] = sum(data["temps"]) / len(data["temps"])
#         data["common_icon"] = data["icons"][0]  # Pick first for simplicity
#         data["common_description"] = max(set(data["descriptions"]), key=data["descriptions"].count)

#     return daily_data

# if __name__ == '__main__':
#     app.run(debug=True)
from flask_app import create_weatherapp
app = create_weatherapp()

if __name__ == '__main__':
    app.run(debug=True) 