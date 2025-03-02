# Instagram Username Availability Bot

This Python bot automates the process of checking the availability of Instagram usernames by interacting with the Instagram sign-up page using `pyautogui`. It reads a list of potential usernames from a file, enters them one by one, and determines availability based on color detection.

## Features
- Reads a list of usernames from `combinations.txt`
- Automates entering usernames in the Instagram sign-up form
- Captures a screenshot of the availability indicator
- Uses `OpenCV` and `KMeans` clustering to detect dominant colors
- Matches detected colors to predefined color names
- Stops execution when an available username is found
- Ensures automation accuracy by using timed delays

## Requirements
Make sure you have the following dependencies installed:

```sh
pip install pyautogui opencv-python numpy scikit-learn
```

Additionally, ensure that you have a Python environment set up, preferably using `venv` to manage dependencies.

## How It Works
1. The script waits for 3 seconds before execution to allow the user to switch to the browser.
2. It iterates through the list of usernames provided in `combinations.txt`.
3. Each username is typed into the Instagram sign-up page automatically.
4. A screenshot of the availability indicator is taken after a brief delay to allow page updates.
5. The script processes the image to extract dominant colors using `OpenCV` and `KMeans` clustering.
6. The extracted colors are compared with a predefined dictionary of color names.
7. If the detected color is brown (indicating an unavailable username), the script moves to the next username.
8. If another color is found, it prints the available username and exits.
9. If all usernames are unavailable, the script completes execution without finding an available name.

## Usage
1. Open Instagram's sign-up page and navigate to the username input field.
2. Ensure that the webpage is positioned correctly so that the bot can interact with the correct elements.
3. Run the script:

```sh
python main.py
```

4. The script will automatically input usernames, check availability, and stop when it finds an available username.

## Configuration
- Modify the following variables in the script to adjust automation settings:
  - `x, y, width, height`: Defines the region for capturing the availability indicator.
  - `COLOR_NAMES`: Adjust the predefined colors if needed.
  - `time.sleep(X)`: Adjust delays to prevent bot detection and ensure stability.

- The script is designed for the default Instagram layout. If Instagram updates its UI, adjustments may be required.

## Troubleshooting
- If the bot is not interacting with the webpage correctly:
  - Ensure that your screen resolution matches the coordinates used in the script.
  - Use `pyautogui.displayMousePosition()` to find the correct coordinates.
- If the bot is detecting incorrect colors:
  - Verify that the availability indicator colors are correctly mapped in `COLOR_NAMES`.
  - Check if `KMeans` clustering is extracting relevant dominant colors.
- If the script crashes or fails to detect an available username:
  - Run it in debug mode by adding print statements to inspect values.
  - Ensure that the `combinations.txt` file is formatted correctly with one username per line.

## Notes
- The script assumes that the availability indicator changes color based on username status.
- Modify `x, y, width, height` to match the correct region for capturing the indicator on your screen.
- Ensure that Instagram’s language and layout are set correctly to match the expected behavior.
- Excessive automation may trigger security measures on Instagram, so use this bot responsibly.

## Disclaimer
This bot interacts with Instagram's interface using automation. Use it responsibly and avoid violating Instagram's terms of service. Excessive requests or improper use may result in account restrictions or bans. The developers take no responsibility for misuse of this tool.

## Future Improvements
- Implement OCR (Optical Character Recognition) to read text-based availability messages.
- Add exception handling for errors like missing image files or incorrect file paths.
- Introduce a GUI interface to make the bot more user-friendly.
- Implement a dynamic region-detection algorithm to adjust to different screen resolutions automatically.
- Optimize color detection using more advanced machine-learning techniques.

