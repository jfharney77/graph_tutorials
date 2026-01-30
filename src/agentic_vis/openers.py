import win32com.client

import os

def full_control_open_pptx(filename: str):
    

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True

    presentation = app.Presentations.Open(filename)

    # Do stuff here...
    input("Press Enter to close the presentation and quit PowerPoint...")

    presentation.Close()
    app.Quit()
