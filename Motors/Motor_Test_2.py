import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
GPIO_PIN_1 = 19
GPIO_PIN_2 = 18

# Set the GPIO pin as an output
GPIO.setup(GPIO_PIN_1, GPIO.OUT)
GPIO.setup(GPIO_PIN_2, GPIO.OUT)

# Create a PWM instance with a frequency of 50Hz
pwm1 = GPIO.PWM(GPIO_PIN_1, 100)
pwm2 = GPIO.PWM(GPIO_PIN_2, 100)

# Sleep time setting
sleep_time = .1

# Start PWM with a duty cycle of 21% (2100 microseconds)
pwm1.start(7)
pwm2.start(7)
# Wait for 5 seconds
time.sleep(sleep_time)


while True:
    # Start PWM with a duty cycle of 15% (1500 microseconds)
    pwm1.ChangeDutyCycle(23)
    pwm2.ChangeDutyCycle(23)

    # Wait for 5 seconds
    time.sleep(sleep_time)

    # Change the duty cycle to 9% (900 microseconds)
    pwm1.ChangeDutyCycle(7)
    pwm2.ChangeDutyCycle(7)

    # Wait for 5 seconds
    time.sleep(sleep_time)

    # Change the duty cycle to 9% (900 microseconds)
    pwm1.ChangeDutyCycle(23)
    pwm2.ChangeDutyCycle(23)

    # Wait for 5 seconds
    time.sleep(.5)

    # Start PWM with a duty cycle of 21% (2100 microseconds)
    pwm1.ChangeDutyCycle(7)
    pwm2.ChangeDutyCycle(7)

    # Wait for 5 seconds
    time.sleep(sleep_time)
    
    # Start PWM with a duty cycle of 15% (1500 microseconds)
    pwm1.ChangeDutyCycle(13)
    pwm2.ChangeDutyCycle(13)
    # Wait for 5 seconds
    time.sleep(sleep_time)

    # Change the duty cycle to 9% (900 microseconds)
    pwm1.ChangeDutyCycle(5)
    pwm2.ChangeDutyCycle(5)
    # Wait for 5 seconds
    time.sleep(sleep_time)
