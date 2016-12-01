import os
import time
import pyHook # http://sourceforge.net/projects/pyhook/
from win32gui import GetWindowRect, GetClassName, GetWindowText

StartPos=EndPos=(0,0)
 
   
def OnMouseEvent(event):
    global StartPos, EndPos
    
    print ("On Mouse Event ")
    
    if event.Window != 0:
        if StartPos==(0,0):
            StartPos=event.Position
        else:
            EndPos=event.Position
        
 
        # return True to pass the event to other handlers
        # return False to stop the event from propagating
    return True
'''
def OnKeyboardEvent(event):
    print ("On keyboard Event ")
    Log('MessageName:' + str(event.MessageName))
    Log('Message:' + str(event.Message))
    Log('Time:' + str(event.Time))
    Log('Window:' + str(event.Window))
    if event.Window != 0:
        Log('Window Rect:' + str( GetWindowRect(event.Window)))
        Log('Window Class Name:' + str( GetClassName(event.Window)))
        Log('Window Text:' + str( GetWindowText(event.Window)))
        Log('WindowName:' + str(event.WindowName))
        Log('Ascii:' + str( event.Ascii) + str( chr(event.Ascii)))
        Log('Key:' + str( event.Key))
        Log('KeyID:' + str( event.KeyID))
        Log('ScanCode:' + str( event.ScanCode))
        Log('Extended:' + str( event.Extended))
        Log('Injected:' + str( event.Injected))
        Log('Alt' + str( event.Alt))
        Log('Transition' + str( event.Transition))
        Log('---')
 
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True
'''

def MouseHook(): 
    # create the hook mananger
    hm = pyHook.HookManager()
    # register two callbacks
    hm.MouseAllButtonsDown = OnMouseEvent
    # hm.KeyDown = OnKeyboardEvent
 
    # hook into the mouse and keyboard events
    hm.HookMouse()    
    # hm.HookKeyboard()
    import pythoncom
    pythoncom.PumpMessages()


