import time
import traceback

from pynput.mouse import Controller


def sleep_stopper(controller, wait=500):
    try:
        mouse = controller
        mouse.move(-1, 0)
        mouse.move(1, 0)
    except:
        print(traceback.format_exc())
    else:
        while True:
            mouse.move(-1, 0)
            mouse.move(1, 0)
            time.sleep(wait)


def run_program():
    try:
        mouse = Controller()
        sleep_stopper(mouse)
    except:
        try:
            mouse = Controller()
            sleep_stopper(mouse)
        except:
            pass

if __name__ == '__main__':
    for n in range(1, 10):
        run_program()
