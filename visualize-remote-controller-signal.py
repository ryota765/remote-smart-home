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
  prev_pin_value = 1 # start from LOW
  last_time = time.time()

  L = 0
  H = 0

  print(f'Start! value: {prev_pin_value}, start_time: {last_time}')

  while True:
    pin_value = GPIO.input(INPUT_PIN)
    
    if prev_pin_value != pin_value:
      prev_pin_value = pin_value

      if pin_value == 1: # changed to LOW
        H = int((time.time() - last_time) * MICRO)
      else: # changed to HIGH
        L = int((time.time() - last_time) * MICRO)

        if (2500 < H < 4000) and (1200 < L < 2000):
          print('start')
        elif (250 < H < 550) and (250 < L < 500):
          print('0', end='')
        elif (250 < H < 550) and (800 < L < 1300):
          print('1', end='')
        else:
          print('\n')
      last_time = time.time()
    else:
      time.sleep(50/MICRO) # 50 microsec

if __name__ == '__main__':
  main()