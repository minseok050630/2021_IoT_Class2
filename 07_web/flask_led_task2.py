from flask import Flask, render_template
import RPi.GPIO as GPIO

red = 19
blue = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<color>/<op>")
def led_color_op(color, op):
    if color == "red":
      if op == "on":
         GPIO.output(red, GPIO.HIGH)
         return "RED LED ON"
      elif op == "off":
         GPIO.output(red, GPIO.LOW)
         return "RED LED OFF"

    elif color == "blue":
      if op == "on":
         GPIO.output(blue, GPIO.HIGH)
         return "BLUE LED ON"
      elif op == "off":
         GPIO.output(blue, GPIO.LOW)
         return "BLUE LED OFF"

    else:
      return "ERROR"


if __name__ == "__main__":
    try:
      app.run(host="0.0.0.0")
    finally:
      GPIO.cleanup()