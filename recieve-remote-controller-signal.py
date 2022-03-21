import RPi.GPIO as GPIO
import time

# setup
INPUT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN)

def main():
  prev_pin_value = None

  while True:
    pin_value = GPIO.input(INPUT_PIN)

    if prev_pin_value is None:
      prev_pin_value = pin_value
      start_time = time.time()
      print(f'Start! value: {pin_value}, start_time: {start_time}')
    elif prev_pin_value != pin_value:
      prev_pin_value = pin_value
      print(f'Value changed! value: {pin_value}, elapsed_time: {time.time() - start_time}')
    else:
      time.sleep(50/1000) # 50 millisec

if __name__ == '__main__':
  main()