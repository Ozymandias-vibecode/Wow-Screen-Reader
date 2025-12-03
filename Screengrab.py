import cv2
import numpy as np
import mss
import time
import os

# Create MSS instance
sct = mss.mss()

# Get monitor info (1 = primary monitor, 2 = secondary, etc.)
monitor = sct.monitors[1]

# Define crop area: from (0,0) to bottom of screen, 400px wide
crop_area = {
    "left": 0,
    "top": 0,
    "width": 400,
    "height": monitor["height"]
}

# Create an always-on-top window
cv2.namedWindow("Cropped Output", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Cropped Output", cv2.WND_PROP_TOPMOST, 1)

fps = 60
delay = 1.0 / fps

# Path to save screenshots (Desktop folder)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "screenshots")
os.makedirs(desktop_path, exist_ok=True)

# Timer for saving screenshots
save_interval = 5  # seconds
last_save_time = time.time()

try:
    while True:
        start = time.time()

        # Grab cropped screen
        screenshot = sct.grab(crop_area)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Show cropped image
        cv2.imshow("Cropped Output", img)

        # Save screenshot every 5 seconds
        if time.time() - last_save_time >= save_interval:
            filename = os.path.join(desktop_path, f"screenshot_{int(time.time())}.png")
            cv2.imwrite(filename, img)
            print(f"Saved: {filename}")
            last_save_time = time.time()

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Maintain ~10 fps
        elapsed = time.time() - start
        if elapsed < delay:
            time.sleep(delay - elapsed)

finally:
    cv2.destroyAllWindows()
