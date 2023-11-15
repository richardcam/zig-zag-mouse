import pyautogui

def move_mouse():
    for i in range(10):
        # mover el mouse a la derecha
        pyautogui.moveRel(50, 0)
        # mover el mouse hacia abajo
        pyautogui.moveRel(0, 50)
        # mover el mouse a la izquierda
        pyautogui.moveRel(-50, 0)
        # mover el mouse hacia arriba
        pyautogui.moveRel(0, -50)

if __name__ == "__main__":
    move_mouse()