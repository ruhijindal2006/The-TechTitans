# import tkinter as tk
# from tkinter import messagebox
# import requests
# import webbrowser
# API_KEY = "d975d9163161fbd8d1a09a595e32a2d5"
# BASE_URL = "https://www.accuweather.com/en/in/ludhiana/205592/weather-forecast/205592"

# def get_weather(city):
#     url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if data["cod"] == 200:
#             weather_info = {
#                 "city": data["name"],
#                 "temp": data["main"]["temp"],
#                 "description": data["weather"][0]["description"].title(),
#                 "humidity": data["main"]["humidity"],
#                 "wind": data["wind"]["speed"]
#             }
#             return weather_info
#         else:
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None

# def show_weather():
#     city = city_entry.get()
#     if city:
#         weather = get_weather(city)
#         if weather:
#             result_label.config(
#                 text=f"City: {weather['city']}\n"
#                      f"Temperature: {weather['temp']} °C\n"
#                      f"Weather: {weather['description']}\n"
#                      f"Humidity: {weather['humidity']}%\n"
#                      f"Wind Speed: {weather['wind']} m/s"
#             )
#         else:
#             messagebox.showerror("Error", "City not found or API error.")
#     else:
#         messagebox.showwarning("Input Error", "Please enter a city name.")

# # UI setup
# root = tk.Tk()
# root.title("Weather")
# root.geometry("350x300")
# root.config(bg="#1e1e1e")

# tk.Label(root, text="Use Current Location:", bg="#1e1e1e", fg="white", font=("Italic", 15,"bold")).pack(pady=10)

# city_entry = tk.Entry(root, font=("Canva Sans", 14), justify="center")
# city_entry.pack(pady=5)

# '''tk.Button(root, text="Get Weather", command=show_weather, bg="#4CAF50", fg="white",
#           font=("Poppins", 15), width=20).pack(pady=15)'''

# result_label = tk.Label(root, text="", bg="#1e1e1e", fg="white", font=("Poppins", 15), justify="left")
# result_label.pack(pady=15)
# def open_weather_website():
#     webbrowser.open(BASE_URL)

# tk.Button(root, text="Get Weather ", command=open_weather_website, bg="green", fg="white",
#           font=("Poppins", 15), width=20).pack(pady=10)
# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import requests

# wttr.in base URL (no API key needed)
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        data = response.json()

        current = data["current_condition"][0]
        weather_info = {
            "city": city.title(),
            "temp": current["temp_C"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind": current["windspeedKmph"]
        }
        return weather_info
    except Exception as e:
        print("Error:", e)
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        if weather:
            result_label.config(
                text=f"City: {weather['city']}\n"
                     f"Temperature: {weather['temp']} °C\n"
                     f"Weather: {weather['description']}\n"
                     f"Humidity: {weather['humidity']}%\n"
                     f"Wind Speed: {weather['wind']} km/h"
            )
        else:
            messagebox.showerror("Error", "City not found or API error.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# UI setup
root = tk.Tk()
root.title("Weather")
root.geometry("350x300")
root.config(bg="#1e1e1e")

tk.Label(root, text="Enter City Name:", bg="#1e1e1e", fg="white", font=("Italic", 15, "bold")).pack(pady=10)

city_entry = tk.Entry(root, font=("Canva Sans", 14), justify="center")
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather, bg="#4CAF50", fg="white",
          font=("Poppins", 15), width=20).pack(pady=15)

result_label = tk.Label(root, text="", bg="#1e1e1e", fg="white", font=("Poppins", 15), justify="left")
result_label.pack(pady=15)

root.mainloop()
