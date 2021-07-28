#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
PIN = 7
UNIT = 0.5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
letters = {
      'A': '.-',
      'B': '-...',
      'C': '-.-.',
      'D': '-..',
      'E': '.',
      'F': '..-.',
      'G': '--.',
      'H': '....',
      'I': '..',
      'J': '.---',
      'K': '-.-',
      'L': '.-..',
      'M': '--',
      'N': '-.',
      'O': '---',
      'P': '.--.',
      'Q': '--.-',
      'R': '.-.',
      'S': '...',
      'T': '-',
      'U': '..-',
      'V': '...-',
      'W': '.--',
      'X': '-..-',
      'Y': '-.--',
      'Z': '--..',
      '1': '.----',
      '2': '..---',
      '3': '...--',
      '4': '....-',
      '5': '.....',
      '6': '-....',
      '7': '--...',
      '8': '---..',
      '9': '----.',
      '0': '-----',
      ' ': ' '
          }


word = input("Write a word: ")
word = list(word.upper())


def transmit(time_sleep):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(time_sleep)
    GPIO.output(PIN, GPIO.LOW)


def dot():
    transmit(1 * UNIT)
    time.sleep(1 * UNIT)


def dash():
    transmit(3 * UNIT)
    time.sleep(1 * UNIT)


for letter in word:
    sequence = letters[letter]
    print(letter)
    for char in sequence:
        if char == "-":
            dash()
        elif char == ".":
            dot()
        elif char == " ":
            time.sleep(4 * UNIT)
    time.sleep(3 * UNIT)
GPIO.cleanup()


"""
 INTERNATIONAL MORSE CODE:
Each position represents one unit. 
ON  : '='
OFF : '.'
"foo bar":
 
=.=.===.=...===.===.===...===.===.===.......===.=.=.=...=.===...=.===.=
    f            o             o                b         a        r
duration | component 
__________________________
1 unit   | dot
3 units  | dash
1 unit   | between elements of a character (dot-dot-dash)
3 units  | between characters
7 units  | between words
1) The duration of a dot  '.' is 1 unit
2) The duration of a dash '_' is 3 units
3) The duration between dots/dashes of a sequence is 1 unit
4) The duration between characters is 3 units
5) The duration between words is 7 units

"""