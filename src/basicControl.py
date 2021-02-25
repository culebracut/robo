import time
from jetbot import Robot

import inputs
from inputs import get_gamepad

js_low = 255
js_high = 0
motor_low = -1
motor_high = 1
js_stop_speed = 128

robot = Robot()

def calcSpeed(value):

  return motor_low + (motor_high - motor_low) * ((value - js_low) / (js_high - js_low))

def main():
    while True:
        try:
            events = get_gamepad()
        except:
            #e = sys.exc_info()[0]
            #write_to_page( "<p>Error: %s</p>" % e )
            continue

        for event in events:
            print(event.ev_type, event.code, event.state)

            # stoped state
            if (event.code=='ABS_Y'):
                position = int(event.state)
                speed = calcSpeed(position)
                print(speed)
                if (event.state > js_stop_speed):
                    robot.forward(speed)
                    continue
                elif (event.state < js_stop_speed):
                    robot.backward(-speed)
                    continue
                else:
                    robot.stop()

            if (event.code=='ABS_X'):
                #robot.set_motors(fast, fast)
                #robot.stop()
                continue

if __name__ == "__main__":
    main()

