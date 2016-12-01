
import EventHook
import threading
import os
import sys
import time
from PIL import ImageGrab



t= threading.Thread(name='mouse event', target=EventHook.MouseHook)
t.start()

while EventHook.EndPos == (0,0):
    time.sleep(1)


img = ImageGrab.grab(bbox=(EventHook.StartPos[0], EventHook.StartPos[1], EventHook.EndPos[0], EventHook.EndPos[1]))
img.show()



'''
from ctypes import windll, Structure, c_ulong, byref

hook_id

def listen():
    global hook_id

    def low_level_handler(aCode, wParam, lParam):
        if aCode != win32con.HC_ACTION:
            return ctypes.windll.user32.CallNextHookEx(hook_id, aCode, wParam, lParam)

        return ctypes.windll.user32.CallNextHookEx(hook_id, aCode, wParam, lParam)

    # Our low level handler signature.
    CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    # Convert the Python handler into C pointer.
    pointer = CMPFUNC(low_level_handler)


    # Hook both key up and key down events for common keys (non-system).
    hook_id = ctypes.windll.user32.SetWindowsHookExA(win32con.WH_MOUSE_LL, pointer,
                                             GetModuleHandle(None), 0)
    # Register to remove the hook when the interpreter exits. Unfortunately a
    # try/finally block doesn't seem to work here.
    atexit.register(ctypes.windll.user32.UnhookWindowsHookEx, hook_id)

def process_msg():
    while True:
        status, msg = PeekMessage(None, 0, 0, win32con.PM_REMOVE)
        if status == 0:
            break
        TranslateMessage(ctypes.byref(msg))
        DispatchMessage(ctypes.byref(msg))


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


class get_wnd_rect(ctypes.Structure):
    _fields_ = [('L', ctypes.c_int),
                ('T', ctypes.c_int),
                ('R', ctypes.c_int),
                ('B', ctypes.c_int)]
 
ctypes.windll.user32.GetWindowRect(hwid, ctypes.byref(rect))
crtW_h = rect.B - rect.T
crtW_w = rect.R - rect.L


pos = queryMousePosition()
print(pos)

'''