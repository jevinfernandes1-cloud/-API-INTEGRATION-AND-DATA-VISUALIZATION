import requests                     # To connect to the weather API
import matplotlib.pyplot as plt     # To make charts
import seaborn as sns

# 1. City and API Key
city = "Mangalore"
API_KEY = "2ec441e03787ddd96f92d06909906b6b"   # Replace with your real key if needed

# 2. Create the full API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# 3. Send a request to the API and get the data
response = requests.get(url)
data = response.json()

# Optional: Check for errors
if response.status_code != 200:
    print("Error fetching data:", data.get("message", "Unknown error"))
else:
    # 4. Extract needed information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']

    # 5. Organize data into a dictionary
    weather_data = {
        'Temperature (°C)': temperature,
        'Humidity (%)': humidity,
        'Pressure (hPa)': pressure,
        'Wind Speed (m/s)': wind_speed
    }

    # 6. Create bar chart using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(weather_data.keys()),
                y=list(weather_data.values()),
                palette="Blues_d")

    plt.title(f"Current Weather in {city}")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
