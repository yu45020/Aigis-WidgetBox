from AutoClick import *
import os
import time

aigisplayer = "..."
aigis = AutoClick(program_title='千年', ImgPath='aigis_img')
aigis.dlg.minimize()
aigis.dlg.wait_for_idle()

aigis.screen_shot()
loc = aigis.detect_icon_loc('click1.jpg')



aigis.dlg.set_focus()
aigis.simulate_click(loc)

# +++++++++++++

program = pywinauto.Application().connect(title_re='千年')
dlg = program.window()
dlg.active()