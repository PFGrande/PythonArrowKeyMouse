import pyautogui # Documentation: https://pyautogui.readthedocs.io/en/latest/
from pynput import keyboard

# pyauto GUI references:
# Key names: https://pynput.readthedocs.io/en/latest/keyboard.html
# Cursor movement: https://pyautogui.readthedocs.io/en/latest/mouse.html
# Install: https://stackoverflow.com/questions/67119368/modulenotfounderror-no-module-named-pyautogui
# Give Permissions (Mac): https://stackoverflow.com/questions/62035751/pyautogui-not-running-on-mac-catalina
# Cursor and Keyboard Inputs: https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/

print("start")
# pyautogui.moveRel(0, 50, duration = 3)
cursorSpeed = 0
maxSpeed = 12
keysPressed = [False, False, False, False] # up down left right
xDirection = 0
yDirection = 0
acceleration = 4
deceleration = 6
mouseToggle = True

# function inspired by: https://stackoverflow.com/questions/11918999/key-listeners-in-python
def pressed_key(key): 
    global cursorSpeed
    global maxSpeed
    global keysPressed
    global xDirection
    global yDirection
    global mouseToggle
    
        
    # catching Attribute error: https://stackoverflow.com/questions/29107534/how-to-catch-nonetype-object-has-no-attribute-something
    try:
        if (key.name == 'shift_r'): # enter and exit mouse mode
            mouseToggle = not mouseToggle
            print(mouseToggle)
            
            
        if (mouseToggle == True):
            if (key.name == "right"): 
                keysPressed[3] = True
                xDirection = 1     
                #print("right")
                
                if (cursorSpeed < maxSpeed): 
                    cursorSpeed = cursorSpeed + acceleration
                # print("not max speed yet")
                    #print(cursorSpeed)
            # else:
                    #print("max speed reached")
                    #print(cursorSpeed)
                    
                    
            if (key.name == "left"): 
                keysPressed[2] = True
                xDirection = -1
                
                if (cursorSpeed < maxSpeed): 
                    cursorSpeed = cursorSpeed + acceleration
                    #print("not max speed yet")
                    #print(cursorSpeed)
                    
                #else:
                    #print("max speed reached")
                    #print(cursorSpeed)
                    
            if (key.name == "down"): 
                keysPressed[1] = True
                yDirection = 1 # the origin of the screen is on the top left corner, making it positive to go up
                
                if (cursorSpeed < maxSpeed): 
                    cursorSpeed = cursorSpeed + acceleration
                    #print("not max speed yet")
                    #print(cursorSpeed)
                #else:
                    #print("max speed reached")
                    #print(cursorSpeed) 
                    
            if (key.name == "up"): 
                keysPressed[0] = True
                yDirection = -1 # the origin of the screen is on the top left corner, making it positive to go up
                
                if (cursorSpeed < maxSpeed): 
                    cursorSpeed = cursorSpeed + acceleration
                    #print("not max speed yet")
                    #print(cursorSpeed)
                #else:
                    #print("max speed reached")
                    #print(cursorSpeed) 
            if (key.name == "alt_r"): 
                pyautogui.click()
    except: 
        pass
    
               
                               
    #print(cursorSpeed*yDirection)
    pyautogui.moveRel(cursorSpeed*xDirection, cursorSpeed*yDirection)
        
    #cursorSpeed-=1 # when no arrow keys are being pressed    
    
def release_key(key):
    global cursorSpeed
    global maxSpeed
    global xDirection
    global yDirection
    global keysPressed
    global deceleration
    
    unpressedKeys = 0 # there is no point to decreasing speed if some keys are still pressed
    
    try:
        if (key.name == "right"):
            keysPressed[3] = False
            xDirection = 0  
        if (key.name == "left"):
            keysPressed[2] = False
            xDirection = 0
        if (key.name == "down"):
            keysPressed[1] = False
            yDirection = 0
        if (key.name == "up"):
            keysPressed[0] = False
            yDirection = 0
    except:
        pass
   
        
    
    for inputKey in keysPressed:
        if (inputKey == False):
            unpressedKeys = unpressedKeys + 1
    
    
    while (unpressedKeys > 0 and cursorSpeed > 0):
        cursorSpeed = cursorSpeed - deceleration     
        #print("decreasing speed")
        #print(cursorSpeed)
        pyautogui.moveRel(cursorSpeed*xDirection, cursorSpeed*yDirection)
    

# Key-listeners: https://stackoverflow.com/questions/11918999/key-listeners-in-python
listener = keyboard.Listener(on_press=pressed_key,on_release=release_key)

listener.start()  # start to listen on a separate thread

listener.join()  # remove if main thread is polling self.keys

program = True

while (program): # keeps program running, have not decided on what key will exit the program.
    if (not listener._running):
        program = False
    