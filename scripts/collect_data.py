import requests
import pandas as pd
from datetime import datetime, timedelta
import os

def collect_weather_data():
    API_KEY = "0eb7f67cbffc11971bf57f4ca5bdd712"  # Replace with your OpenWeatherMap API key
    CITY = "London"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    weather_data = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'weather_condition': data['weather'][0]['main']
    }
    
    df = pd.DataFrame([weather_data])
    
    # Create data directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Save data
    output_path = 'data/raw/weather_data.csv'
    df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
    
if __name__ == "__main__":
    collect_weather_data()

