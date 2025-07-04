import Quartz
import CoreFoundation
KEY = None
keyMaper = {
    0: "A",
    1: "S",
    2: "D",
    3: "F",
    4: "H",
    5: "G",
    6: "Z",
    7: "X",
    8: "C",
    9: "V",
    10: "§",
    11: "B",
    12: "Q",
    13: "W",
    14: "E",
    15: "R",
    16: "Y",
    17: "T",
    18: "1",
    19: "2",
    20: "3",
    21: "4",
    22: "6",
    23: "5",
    24: "=",
    25: "9",
    26: "7",
    27: "-",
    28: "8",
    29: "0",
    30: "]",
    31: "O",
    32: "U",
    33: "[",
    34: "I",
    35: "P",
    36: "\n",
    37: "L",
    38: "J",
    39: "'",
    40: "K",
    41: ";",
    42: "\\",
    43: ",",
    44: "/",
    45: "N",
    46: "M",
    47: ".",
    48: "   ",
    49: " ",
    50: "`",
    51: "Delete",
    52: "Enter ()",
    53: "Escape",
    54: "Right Command",
    55: "Command",
    56: "Shift",
    57: "Caps Lock",
    58: "Option",
    59: "Control",
    60: "Right Shift",
    61: "Right Option",
    62: "Right Control",
    63: "Function (Fn)",
    64: "F17",
    65: "Decimal ()",
    66: "JIS_Eisu",
    67: "F18",
    68: "F19",
    69: "JIS_Kana",
    70: "F20",
    71: "0",
    72: "1",
    73: "2",
    74: "3",
    75: "4",
    76: "5",
    77: "6",
    78: "7",
    79: "F21",
    80: "8",
    81: "9",
    82: "=",
    83: "F22",
    84: "F23",
    85: "\n",
    86: "/",
    87: "F24",
    88: "*",
    89: "-",
    90: "+",
    91: "Clear",
    92: "Volume Up",
    93: "Volume Down",
    94: "Mute",
    95: "F25",
    96: "F26",
    97: "F27",
    98: "F28",
    99: "F29",
    100: "F30",
    101: "F31",
    102: "F32",
    103: "F33",
    104: "F34",
    105: "F35",
    107: "Launchpad",
    109: "Mission Control",
    111: "Media Play",
    113: "Media Next",
    114: "Media Previous",
    115: "Brightness Up",
    116: "Brightness Down",
    117: "Mission Control",
    118: "Launchpad",
    119: "Keyboard Illumination Down",
    120: "Keyboard Illumination Up",
    121: "Media Rewind",
    122: "F1",
    123: "Left Arrow",
    124: "Right Arrow",
    125: "Down Arrow",
    126: "Up Arrow",
    127: "Power",
}
SpecialKey = [48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,83,84,87,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,109,111,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]

def callback(proxy,type_,event,refcon):
    global KEY
    if type_ == Quartz.kCGEventKeyDown:
        keycode = Quartz.CGEventGetIntegerValueField(event,Quartz.kCGKeyboardEventKeycode)
        KEY = keycode
    return event

class Darwin:
    def __init__(self,filepath):
        self.file = filepath

    def Key_Pressed():
        global KEY
        KEY = None
        event_mask = Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown)

        event_tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            event_mask,
            callback,
            None
        )

        if not event_mask:
            print("Failed to create event , make sure you have acceblity permissions")
            exit(1)
                
        run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None,event_tap,0)
        Quartz.CFRunLoopAddSource(
            Quartz.CFRunLoopGetCurrent(),
            run_loop_source,
            Quartz.kCFRunLoopDefaultMode,
        )

        Quartz.CGEventTapEnable(event_tap,True)

        CoreFoundation.CFRunLoopRun()
        print(keyMaper[KEY])
        
        return keyMaper[KEY]
        
    def Key_txt(self):
        global KEY
        KEY = None
        event_mask = Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown)

        event_tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            event_mask,
            callback,
            None
        )

        if not event_mask:
            print("Failed to create event , make sure you have acceblity permissions")
            exit(1)
                
        run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None,event_tap,0)
        Quartz.CFRunLoopAddSource(
            Quartz.CFRunLoopGetCurrent(),
            run_loop_source,
            Quartz.kCFRunLoopDefaultMode,
        )

        Quartz.CGEventTapEnable(event_tap,True)

        CoreFoundation.CFRunLoopRun()
        print(keyMaper[KEY])
        
        if keyMaper[KEY] == "Delete":
            data = open(self.file,"r")
            m = data.read()
            km = m[:-1]
            
            return km,"w"
        
        elif [KEY] in SpecialKey:
            return "","a"
        
        return keyMaper[KEY],"a"