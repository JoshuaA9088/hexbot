import numpy as np
import cv2
import requests
import time


height = 500
width = 500


def get_colors():
    r = requests.get(
        "https://api.noopschallenge.com/hexbot?count=1000&width=500&height=500")
    colors = r.json()
    colors = colors["colors"]
    return colors


def hex_to_rgb(HEX):
    HEX = HEX.lstrip("#")
    RGB = tuple(int(HEX[i:i+2], 16) for i in (0, 2, 4))
    return RGB[::-1]

if __name__ == "__main__":
    while True:
        image = np.ones((height, width, 3), np.uint8) * 255
        colors = get_colors()
        for i in colors:
            color = i["value"]
            x = i["coordinates"]["x"]
            y = i["coordinates"]["y"]
            cv2.circle(image, (y, x), 1, hex_to_rgb(color), -1)
        cv2.imshow("Dots", image)
        time.sleep(5)

        if cv2.waitKey(1) == 27:
            exit(0)
