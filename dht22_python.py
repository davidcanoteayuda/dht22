import adafruit_dht
import board
import time

# Usa el pin donde conectaste el DHT22. Ej: board.D4 (GPIO4)
sensor = adafruit_dht.DHT22(board.D4)

try:
    while True:
        temperature = sensor.temperature
        humidity = sensor.humidity

        if temperature is not None and humidity is not None:
            print(f"🌡️ Temperatura: {temperature:.1f}°C")
            print(f"💧 Humedad: {humidity:.1f}%")
        else:
            print("⚠️ No se pudo leer del sensor. Intentando de nuevo...")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Lectura interrumpida por el usuario.")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    sensor.exit()
