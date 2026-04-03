from pyautogui import locateOnScreen, center, click
from time import sleep
from configparser import ConfigParser
import winsound  # Solo Windows, ver abajo para multiplataforma

#Default values
delay_between_tries = 0.2
delay_after_succeding = 1
delay_after_failing = 5

#If the config has values, use those instead
config = ConfigParser()
config.read('settings.ini')

if config.has_option("SETTINGS", "delay_between_tries"):
    delay_between_tries = float(config["SETTINGS"]["delay_between_tries"])

if config.has_option("SETTINGS", "delay_after_succeding"):
    delay_after_succeding = float(config["SETTINGS"]["delay_after_succeding"])

if config.has_option("SETTINGS", "delay_after_failing"):
    delay_after_failing = float(config["SETTINGS"]["delay_after_failing"])

def try_click(image, confidence=0.6):
    """Intenta localizar y hacer click en una imagen. Retorna True si lo logra."""
    location = locateOnScreen(image, confidence=confidence)
    if location is None:
        return False
    point = center(location)
    click(point.x, point.y)
    return True

def emit_sound():
    """Emite un sonido de alerta."""
    try:
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    except Exception:
        # Multiplataforma: si no hay winsound, usa print con bell
        print("\a")

#Main loop
while True:
    sleep(delay_between_tries)

    # Intento 1: imagen principal
    try:
        if try_click("reference.png"):
            sleep(delay_after_succeding)
            continue
    except Exception as e:
        print(f"Error con reference.png: {e}")

    # Intento 2: imagen alternativa
    print("No se encontró reference.png, intentando con reference_alt.png...")
    try:
        if try_click("reference_alt.png"):
            sleep(delay_after_succeding)
            continue
    except Exception as e:
        print(f"Error con reference_alt.png: {e}")

    # Ambas fallaron: emitir sonido y esperar
    print(f"Ambas imágenes fallaron. Emitiendo sonido y esperando {delay_after_failing}s...")
    emit_sound()
    sleep(delay_after_failing)