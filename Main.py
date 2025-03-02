import pyautogui
import time
import cv2
import numpy as np
from sklearn.cluster import KMeans
x, y, width, height = 820, 485, 50, 50
usernames = []
with open("combinations.txt", "r") as file:
    for line in file:
        usernames.append(line.strip())
check_color = False
COLOR_NAMES = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "gray": (128, 128, 128),
    "orange": (255, 165, 0),
    "brown": (165, 42, 42),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203)
}
def closest_color(rgb_tuple):
    min_distance = float("inf")
    closest_name = None
    for name, color in COLOR_NAMES.items():
        distance = np.sqrt((color[0] - rgb_tuple[0]) ** 2 +
                           (color[1] - rgb_tuple[1]) ** 2 +
                           (color[2] - rgb_tuple[2]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_name = name
    return closest_name

time.sleep(3)
for username in usernames:
    pyautogui.click(1250,24)
    pyautogui.click(784,503)
    pyautogui.write(username, interval=0.25)
    pyautogui.click(1075,572)
    time.sleep(5)
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("image.png")
    time.sleep(3)
    pyautogui.click(784,503)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    pyautogui.click(1075,572)
    image = cv2.imread("image.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=3, n_init=10)
    kmeans.fit(pixels)

    dominant_colors = kmeans.cluster_centers_.astype(int)

    color_names = [closest_color(tuple(color)) for color in dominant_colors]

    for color in color_names:
        if color == "brown":
            check_color = True
        else:
            continue

    if check_color:
        continue
    else:
        print(f"{username} is available")
        break



