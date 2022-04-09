import RPi.GPIO as GPIO
import time

# setup
INPUT_PIN = 17

# Sensor output:
#   IR signal    -> 0
#   No IR signal -> 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

MICRO = 1000000

def main():
  prev_pin_value = None
  L = None
  H = None

  while True:
    pin_value = GPIO.input(INPUT_PIN)

    if prev_pin_value is None:
      prev_pin_value = pin_value
      last_time = time.time()
      print(f'Start! value: {pin_value}, start_time: {last_time}')
    elif prev_pin_value != pin_value:
      prev_pin_value = pin_value

      if pin_value == 1: # changed to LOW
        H = int((time.time() - last_time) * MICRO)
      else: # changed to HIGH
        L = int((time.time() - last_time) * MICRO)
        print(f'H:L = {H}:{L}')
      last_time = time.time()
    else:
      time.sleep(50/MICRO) # 50 microsec

if __name__ == '__main__':
  main()
