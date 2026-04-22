import time
# import board (Uncomment when using physical sensors)
# import adafruit_max30102 

def get_vitals():
    # Placeholder for sensor logic
    temp = 36.6  # Example: read from DS18B20 sensor
    pulse = 75   # Example: read from MAX30102 sensor
    return {"temp": temp, "pulse": pulse}

if __name__ == "__main__":
    while True:
        data = get_vitals()
        print(f"Current Vitals - Temp: {data['temp']}°C, Pulse: {data['pulse']} BPM")
        time.sleep(2)
