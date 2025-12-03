from pynput.mouse import Controller, Button
import random
import time
import mss

mouse = Controller()



sct = mss.mss()
monitor = sct.monitors[1]  # 1 = primary monitor
print("Width:", monitor["width"])
print("Height:", monitor["height"])
mwidth = monitor["width"]
mheight = monitor["height"]

# Move mouse
while True:
	nextpositionx =random.randint(1,mwidth)
	nextpositiony =random.randint(1,mheight)
	print("Next position X is: ",nextpositionx)
	print("Next position Y is: ",nextpositiony)
	
	mousecurrentX, mousecurrentY = mouse.position
	
	
	while (mousecurrentX != nextpositionx) and (mousecurrentY != nextpositiony):
		mousecurrentX, mousecurrentY = mouse.position
		if (mousecurrentX != nextpositionx):
			if (mousecurrentX - nextpositionx) < 0:
					movex = mousecurrentX +1
			else:
					movex = mousecurrentX -1
		if (mousecurrentY != nextpositiony):
			if (mousecurrentY - nextpositiony) < 0:
					movey = mousecurrentY +1
			else:
					movey = mousecurrentY -1
		
		
		
		mouse.position = (movex,movey)
		time.sleep(.0001)
		
	print("Reached Destination")
	time.sleep(.1)
