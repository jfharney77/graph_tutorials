import win32com.client

import os

def full_control_open_pptx(filename: str, stoppable: bool = True) -> None:
    

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True

    presentation = app.Presentations.Open(filename)

    if stoppable:
        # Do stuff here...
        input("Press Enter to close the presentation and quit PowerPoint...")

    print ('closing presentation and quitting PowerPoint')
    presentation.Close()
    app.Quit()
