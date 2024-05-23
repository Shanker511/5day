import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette

# Update these with your actual details
api_key = "YOUR_OPENWEATHER_API_KEY"
city = "CITY_NAME"
units = "imperial"  # Display in Fahrenheit

def get_current_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return f"{data['main']['temp']}°", data['weather'][0]['description']

def get_weather_forecast():
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    forecast = []
    temp_data = {}

    for i, item in enumerate(data['list']):
        date = item['dt_txt'].split(' ')[0]
        if date not in temp_data:
            temp_data[date] = []
        temp_data[date].append(item['main']['temp'])

        if (i + 1) % 8 == 0 or i == len(data['list']) - 1:
            high_temp = max(temp_data[date])
            low_temp = min(temp_data[date])
            forecast.append({
                "date": date,
                "high_temp": f"{high_temp}°",
                "low_temp": f"{low_temp}°",
                "description": item['weather'][0]['main'],
                "icon": item['weather'][0]['icon']
            })

    return forecast

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather Forecast')
        self.showFullScreen()  # Making the application full screen
        self.setup_ui()

    def setup_ui(self):
        current_temp, current_desc = get_current_weather()
        forecast = get_weather_forecast()

        weather_layout = QVBoxLayout()

        # Setup label styles
        temp_font = QFont('Arial', 20, QFont.Bold)
        desc_font = QFont('Arial', 10, QFont.Bold)

        # Palette for blue background
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#0000ff'))  # Blue background
        self.setPalette(palette)
        
        current_temp_label = QLabel(f"Current Temperature: {current_temp}")
        current_desc_label = QLabel(f"Weather: {current_desc}")
        
        current_temp_label.setFont(temp_font)
        current_desc_label.setFont(desc_font)
        
        current_temp_label.setStyleSheet("color: black;")  # Black text
        current_desc_label.setStyleSheet("color: black;")  # Black text
        
        weather_layout.addWidget(current_temp_label)
        weather_layout.addWidget(current_desc_label)

        # Day cells layout
        forecast_layout = QHBoxLayout()

        for day in forecast:
            v_layout = QVBoxLayout()
            v_layout.setAlignment(Qt.AlignCenter)  # Center items
            
            # Setup labels
            date_label = QLabel(day["date"])
            date_label.setFont(desc_font)
            date_label.setStyleSheet("color: black;")
            
            icon_label = QLabel()
            pixmap = QPixmap(f'icon/{day["icon"]}.png').scaled(64, 64, Qt.KeepAspectRatio)
            icon_label.setPixmap(pixmap)
            
            high_temp_label = QLabel(f"High: {day['high_temp']}")
            low_temp_label = QLabel(f"Low: {day['low_temp']}")
            desc_label = QLabel(day["description"])
            
            high_temp_label.setFont(desc_font)
            low_temp_label.setFont(desc_font)
            desc_label.setFont(desc_font)
            
            high_temp_label.setStyleSheet("color: black;")
            low_temp_label.setStyleSheet("color: black;")
            desc_label.setStyleSheet("color: black;")

            v_layout.addWidget(date_label)
            v_layout.addWidget(icon_label)
            v_layout.addWidget(high_temp_label)
            v_layout.addWidget(low_temp_label)
            v_layout.addWidget(desc_label)

            forecast_layout.addLayout(v_layout)

        weather_layout.addLayout(forecast_layout)

        central_widget = QWidget()
        central_widget.setLayout(weather_layout)
        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec_()