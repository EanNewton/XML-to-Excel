import sys
import os
import parserXML
import tracemalloc
from platform import system as psys
from pathlib import Path

try:
    import Tkinter as tk
    import Tkinter.messagebox as messagebox
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

toScan = []

def set_Tk_var():
    global cb_singleFile
    cb_singleFile = tk.IntVar()

    global cb_enableCore
    cb_enableCore = tk.IntVar()

    global cb_logging
    cb_logging = tk.IntVar()
    
    global eb_outputName
    eb_outputName = tk.StringVar()
    
    global msg_output
    msg_output = tk.StringVar()
    msg_output.set('')
    
    global progressBar
    progressBar = tk.IntVar()
    
    global progressSubBar
    progressSubBar = tk.IntVar()
    
    global msg_progressStage
    msg_progressStage = tk.StringVar() 

    global directory_core
    directory_core = tk.StringVar()


def addDir(directory):
    toScan.append(directory)
    msg_output.set('\n'.join(toScan))
    top_level.update()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def setProgress(message, progress):
    msg_output.set(message)
    progressBar.set(progress)
    top_level.update()

def setSubProgress(message, progress):
    msg_progressStage.set(message)
    progressSubBar.set(progress)
    top_level.update()

def run():
    if str(eb_outputName.get()):
        parserXML.OUTPUT_NAME = str(eb_outputName.get())
    else:
        parserXML.OUTPUT_NAME = 'Output'

    parserXML.DEFS = toScan
    parserXML.SINGLE_FILE = True if cb_singleFile.get() else False
    parserXML.LOGGING = True if cb_logging.get() else False
    
    parserXML.run()
    parserXML.DEFS.clear()
    sys.stdout.flush()

if __name__ == '__main__':
    import rimsheets
    rimsheets.vp_start_gui()




