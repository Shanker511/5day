
# 5 Day Forcast for the Raspberry pi Zero W

# Weather App

This Weather App provides current weather details and a 5-day forecast with high, low temperatures, and daily weather descriptions. It displays weather data for a specified city using the OpenWeather API.

## Features

- Shows current temperature and weather description.
- Displays a 5-day weather forecast with high and low temperatures.
- Utilizes the OpenWeather API to fetch real-time weather data.
- Full-screen application designed for Raspberry Pi with PyQt5 GUI.

## Prerequisites
Before you can run the weather app, make sure you have the following installed:
- Python 3.x
- PyQt5
- Requests library

You will also need an API key from OpenWeatherMap, which you can obtain by signing up at [OpenWeatherMap](https://openweathermap.org/api).

## Installation

1. **Clone the Repository**

git clone https://yourrepositoryurl.com cd weather-app

2. **Install Required Python Libraries**
pip3 install pyqt5 requests

3. **Set Up API Key and City**
- Open the `weather_app.py` file.
- Replace `YOUR_OPENWEATHER_API_KEY` with your OpenWeather API key.
- Replace `CITY_NAME` with the city you want to fetch weather data for.

4. **Icon Setup**
- Ensure you have the weather icons saved in an `icon` directory within the same directory as your script.
- Icons should be named according to the icon codes (example: `01d.png`, `01n.png`).

## Running the Application

To run the application, execute the following command in your terminal:
python3 weather_app.py

The application will launch in full-screen mode on your display.

## Autostart on Raspberry Pi

To have this app start automatically on Raspberry Pi boot:

1. Make your Python script executable:
chmod +x weather_app.py

2. Add it to the crontab:
crontab -e

Then add:
@reboot /usr/bin/python3 /path/to/weather_app.py

## Customization

You can customize the application by modifying the `weather_app.py`, adjusting city, units, and graphical elements as desired.

## Support

For support, raise issues on the repository or contact the repository owner.

## License

This project is licensed under the MIT License - see the LICENSE file for detail

## Authors

- [@Gareth Erwin](https://www.github.com/shanker511)


## Screenshots

![App Screenshot](https://i.postimg.cc/tgJbgZ1Y/weather.png)

