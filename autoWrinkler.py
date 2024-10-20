import pyautogui
import keyboard
import time
import threading

# Lista de 12 coordenadas (SOLO PANTALLA GRANDE)
coordenadas = [
    (290, 239), 
    (389, 263), 
    (435, 317), 
    (461, 421),
    (441, 522), 
    (395, 579), 
    (291, 614), 
    (196, 600),
    (120, 510), 
    (102, 420), 
    (136, 318), 
    (198, 241)
]

# Estado de la función de clickeo
clickeo_activo = False

def clickeo_automatico():
    global clickeo_activo
    while True:
        if clickeo_activo:
            for idx, (x, y) in enumerate(coordenadas):
                print(f"Iniciando clics rápidos en coordenada {idx+1}: ({x}, {y})")
                for i in range(4):  
                    pyautogui.click(x,y)
        else:
            time.sleep(1)  # Si está desactivado, espera antes de revisar nuevamente

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("[F5] Activar/Desactivar clickeo automático")
    print("[ESC] Salir del programa")

def escuchar_teclas():
    global clickeo_activo
    while True:
        # Activar/desactivar el clickeo automático con F5
        if keyboard.is_pressed('F5'):
            clickeo_activo = not clickeo_activo
            estado = "activado" if clickeo_activo else "desactivado"
            print(f"Clickeo automático {estado}")
            time.sleep(0.5)  # Pequeña pausa para evitar múltiples detecciones
        # Salir del programa con ESC
        elif keyboard.is_pressed('esc'):
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    
    mostrar_menu()

    # Ejecutar la función de clickeo automático en un hilo separado
    threading.Thread(target=clickeo_automatico, daemon=True).start()

    escuchar_teclas()