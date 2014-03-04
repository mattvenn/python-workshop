#shows a cancel/confirm box
import easygui as eg

while True:
    # show a Continue/Cancel dialog
    if eg.ccbox('do you want to continue?', 'ccbox demo'):     
        #user chose Continue, do nothing
        pass
    else:
        #user chose Cancel
        exit(0)
