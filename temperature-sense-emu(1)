# Author : Nikunj Parmar


from sense_emu import SenseHat

red, blue = (255, 0, 0), (0, 0, 255)

sense = SenseHat()

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
