import cv2
import pyautogui
import numpy as np
from datetime import datetime

framerate=12.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
filename=str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))+".avi"
screen_size=(1920, 1080)

out=cv2.VideoWriter(filename,fourcc,framerate,(screen_size))

Xs = [0,6,2,5,4,2,2,0]
Ys = [0,2,2,4,5,2,6,0]
while True:
    img = pyautogui.screenshot()
    mouseX,mouseY = pyautogui.position()
    img_np=np.array(img)
    frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

    Xthis=[4 * x + mouseX for x in Xs]
    Ythis=[4 * y + mouseY for y in Ys]
    points=list(zip(Xthis, Ythis))
    points=np.array(points, 'int32')
    cv2.fillPoly(frame, [points], color=[1, 190, 200])

    out.write(frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
out.release()
