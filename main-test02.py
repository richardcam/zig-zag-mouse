import pyautogui
import time

def move_mouse():
    # Almacenar el tiempo actual
    last_movement_time = time.time()

    # Bucle infinito
    while True:
        # Si el ratón no se ha movido en 3 minutos
        # if time.time() - last_movement_time > 180:
        if time.time() - last_movement_time > 120:

            # Mover el ratón en zig zag
            for i in range(5):
                # Mover el mouse a la derecha
                pyautogui.moveRel(50, 0)
                # Mover el mouse hacia abajo
                pyautogui.moveRel(0, 50)
                # Mover el mouse a la izquierda
                pyautogui.moveRel(-50, 0)
                # Mover el mouse hacia arriba
                pyautogui.moveRel(0, -50)

            # Actualizar el tiempo actual
            last_movement_time = time.time()

if __name__ == "__main__":
    move_mouse()
