import wiringpi
import time

# setup
OUTPUT_PIN = 18
FREQ = 38e3
RANGE = 3
CLOCK = int(19.2e6/FREQ/RANGE) 
T = 350

MICRO = 1000000
REPEAT = 4

def send_zero():
    wiringpi.pwmWrite(OUTPUT_PIN, 1)
    time.sleep(T/MICRO)
    wiringpi.pwmWrite(OUTPUT_PIN, 0)
    time.sleep(T/MICRO)

def send_one():
    wiringpi.pwmWrite(OUTPUT_PIN, 1)
    time.sleep(T/MICRO)
    wiringpi.pwmWrite(OUTPUT_PIN, 0)
    time.sleep(3*T/MICRO)

def send_data(data="110010001110100000010100"):
    wiringpi.pwmWrite(OUTPUT_PIN,1)
    time.sleep(8*T/MICRO)
    wiringpi.pwmWrite(OUTPUT_PIN,0)
    time.sleep(4*T/MICRO)

    for d in data:
        if d == "0":
            send_zero()
        else:
            send_one()

    wiringpi.pwmWrite(OUTPUT_PIN,1)
    time.sleep(T/MICRO)
    wiringpi.pwmWrite(OUTPUT_PIN,0)
    return

def main():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(OUTPUT_PIN, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    wiringpi.pwmSetRange(RANGE)
    wiringpi.pwmSetClock(CLOCK)

    time.sleep(1)

    for _ in range(REPEAT):
        send_data()
        time.sleep(8000/MICRO)

if __name__ == '__main__':
    main()