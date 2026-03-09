import cv2
import numpy as np
import random
import time

print("SMART KITCHEN VISION SYSTEM STARTED")

# camera start
cap = cv2.VideoCapture(0)

def detect_fire(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_fire = np.array([18,50,50])
    upper_fire = np.array([35,255,255])

    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    fire_pixels = np.sum(mask)

    if fire_pixels > 50000:
        return True
    return False


def detect_gas():
    # simulated gas value
    gas_value = random.randint(100, 500)

    if gas_value > 400:
        return True
    return False


def temperature_monitor():
    # simulated temperature
    temp = random.randint(25, 60)

    if temp > 45:
        return True, temp
    return False, temp


while True:

    ret, frame = cap.read()

    if not ret:
        break

    fire = detect_fire(frame)
    gas = detect_gas()
    temp_alert, temperature = temperature_monitor()

    if fire:
        cv2.putText(frame,"FIRE DETECTED!",(50,50),
        cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    if gas:
        cv2.putText(frame,"GAS LEAK ALERT!",(50,100),
        cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    if temp_alert:
        cv2.putText(frame,f"HIGH TEMP: {temperature}C",(50,150),
        cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow("Kitchen Vision System",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(1)

cap.release()
cv2.destroyAllWindows()