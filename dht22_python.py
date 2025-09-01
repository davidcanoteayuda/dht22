import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D17)
print("Leyendo datos del sensor DHT22 (CTRL+C para salir)...")

while True:
    try:
        temperatura = dhtDevice.temperature
        humedad = dhtDevice.humidity
        print(f"🌡️ Temperatura: {temperatura:.1f}°C  💧 Humedad: {humedad:.1f}%")
        time.sleep(2)
    except RuntimeError as error:
        print(f"Error al leer el sensor: {error.args[0]}")
        time.sleep(2)
    except KeyboardInterrupt:
        print("Saliendo del programa...")
        break
