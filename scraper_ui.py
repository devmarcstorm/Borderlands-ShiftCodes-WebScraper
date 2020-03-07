import webbrowser
from tkinter import Button, Frame, Label, Listbox, Tk

import pyperclip as clip

import used_codes as my_codes
import webscraper as scraper

# GUI - color settings
color_wbg = 'blue'
color_bg = 'white'
color_fg = 'white'
color_sec = 'SeaGreen1'

# GUI - font settings
font_prim = ("Verdana", 8)

# URLs of the websites used
url_b1 = 'http://orcz.com/Borderlands:_Golden_Key'
url_b2 = 'http://orcz.com/Borderlands_2:_Golden_Key'
url_bps = 'http://orcz.com/Borderlands_Pre-Sequel:_Shift_Codes'
url_b3 = 'http://orcz.com/Borderlands_3:_Shift_Codes'
url_vip = 'http://orcz.com/Borderlands_VIP'

# Table columns for each platform
cell_pc = 4
cell_ps4 = 5
cell_xbox = 6

def callback(url):
        '''
        Opens the specified URL in the default browser.
        '''
        webbrowser.open_new(url)

def list_color(listBox, platform, game):
        '''
        Indicates all codes already used.
        '''
        listObjects = listBox.get(0, listBox.size())

        i = 0
        for item in listObjects:
                if (item in my_codes.read_codes(game, platform)):
                        listBox.itemconfig(i, bg="red", fg='gray30')
                i += 1
        
def fill_list(selectedList, platform = 'PC', game = 'Borderlands 2'):
        '''
        Fills the ListBox of the GUI with the codes of the selected list.
        '''
        labelSelectedCodeList.configure(text='------------------------------\n{} : {}\n------------------------------'.format(platform, game))

        # clear list
        listBox.delete(0,'end')

        # fill list
        for x in range(1, len(selectedList) + 1):
                listBox.insert(x, selectedList[x - 1])

        list_color(listBox, platform, game)

def onSelect(evt):
        '''
        Copies the codes to the clipboard and mark them as used.
        '''
        widget = evt.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        clip.copy(value)

        widget.itemconfig(index, bg="SpringGreen2", fg='gray30')
        labelCodeInfo.configure(text='{}\nhas been copied to the clipboard!'.format(value))

        platform, game = labelSelectedCodeList.cget("text").replace("------------------------------", "").replace("\n", "").split(' : ')
        my_codes.write_codes(value, game, platform)

# tkinter GUI
root = Tk()
root.title("Bl.CodeScraper - for Bolderlands ShiftCodes")
root.configure(background=color_wbg)

frame = Frame()
frame.configure(background=color_wbg)
frame.pack(side='left', padx=(7, 7))

frameL = Frame()
frameL.configure(background=color_wbg)
frameL.pack(side='right')

width_button = 7

'''
-------------------------------------------------------------------------------------
Borderlands 1
-------------------------------------------------------------------------------------
'''

titleBorderlands1 = Label(frame, text="Borderlands 1\n------------------------------")
titleBorderlands1.configure(background=color_wbg, fg=color_fg, font=font_prim)
titleBorderlands1.pack()

frameBorderlands1 = Frame(frame)
frameBorderlands1.pack()

buttonBorderlands1PC = Button(frameBorderlands1, width=width_button, text="PC", command=lambda: fill_list(list_pc_b1, 'PC', 'Borderlands 1'))
buttonBorderlands1PC.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands1PC.pack(in_=frameBorderlands1, side='left')

buttonBorderlands1PS4 = Button(frameBorderlands1, width=width_button, text="PS4", command=lambda: fill_list(list_ps4_b1, 'PS4', 'Borderlands 1'))
buttonBorderlands1PS4.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands1PS4.pack(in_=frameBorderlands1, side='left')

buttonBorderlands1XBOX = Button(frameBorderlands1, width=width_button, text="xBox", command=lambda: fill_list(list_xbox_b1, 'xBox', 'Borderlands 1'))
buttonBorderlands1XBOX.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands1XBOX.pack(in_=frameBorderlands1, side='left')

'''
-------------------------------------------------------------------------------------
Borderlands 2 
-------------------------------------------------------------------------------------
'''

titleBorderlands2 = Label(frame, text="\nBorderlands 2\n------------------------------")
titleBorderlands2.configure(background=color_wbg, fg=color_fg, font=font_prim)
titleBorderlands2.pack()

frameBorderlands2 = Frame(frame)
frameBorderlands2.pack()

buttonBorderlands2PC = Button(frameBorderlands2, width=width_button, text="PC", command=lambda: fill_list(list_pc_b2))
buttonBorderlands2PC.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands2PC.pack(in_=frameBorderlands2, side='left')

buttonBorderlands2PS4 = Button(frameBorderlands2, width=width_button, text="PS4", command=lambda: fill_list(list_ps4_b2, 'PS4'))
buttonBorderlands2PS4.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands2PS4.pack(in_=frameBorderlands2, side='left')

buttonBorderlands2XBOX = Button(frameBorderlands2, width=width_button, text="xBox", command=lambda: fill_list(list_xbox_b2, 'xBox'))
buttonBorderlands2XBOX.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands2XBOX.pack(in_=frameBorderlands2, side='left')

'''
-------------------------------------------------------------------------------------
Borderlands - Pre Sequel
-------------------------------------------------------------------------------------
'''

titleBorderlandsPS = Label(frame, text="\nBorderlands - Pre Sequel\n------------------------------")
titleBorderlandsPS.configure(background=color_wbg, fg=color_fg, font=font_prim)
titleBorderlandsPS.pack()

frameBorderlandsPS = Frame(frame)
frameBorderlandsPS.pack()

buttonBorderlandsPSPC = Button(frameBorderlandsPS, width=width_button, text="PC", command=lambda: fill_list(list_pc_bps, 'PC', 'Borderlands - Pre Sequel'))
buttonBorderlandsPSPC.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlandsPSPC.pack(in_=frameBorderlandsPS, side='left')

buttonBorderlandsPSPS4 = Button(frameBorderlandsPS, width=width_button, text="PS4", command=lambda: fill_list(list_ps4_bps, 'PS4', 'Borderlands - Pre Sequel'))
buttonBorderlandsPSPS4.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlandsPSPS4.pack(in_=frameBorderlandsPS, side='left')

buttonBorderlandsPSXBOX = Button(frameBorderlandsPS, width=width_button, text="xBox", command=lambda: fill_list(list_xbox_bps, 'xBox', 'Borderlands - Pre Sequel'))
buttonBorderlandsPSXBOX.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlandsPSXBOX.pack(in_=frameBorderlandsPS, side='left')

'''
-------------------------------------------------------------------------------------
Borderlands 3 and VIP
-------------------------------------------------------------------------------------
'''

titleBorderlands3 = Label(frame, text="\nBorderlands 3 / VIP\n------------------------------")
titleBorderlands3.configure(background=color_wbg, fg=color_fg, font=font_prim)
titleBorderlands3.pack()

frameBorderlands3 = Frame(frame)
frameBorderlands3.pack()

buttonBorderlands3Multi = Button(frameBorderlands3, width=width_button * 3, text="B3 multiplatform", command=lambda: fill_list(list_multi_b3, 'Multi', 'Borderlands 3'))
buttonBorderlands3Multi.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlands3Multi.pack(in_=frameBorderlands3, side='left')

buttonBorderlandsVIP= Button(frameBorderlands3, width=width_button * 2, text="vip codes", command=lambda: fill_list(list_vip, 'Multi', 'VIP'))
buttonBorderlandsVIP.configure(background=color_bg, highlightbackground=color_bg, font=font_prim)
buttonBorderlandsVIP.pack(in_=frameBorderlands3, side='left')

infoBorderlands3 = Label(frame, text="Not all B3 codes work on all platforms.\nIf the codes are not displayed, the websites have been changed.\nI'm working on updates.")
infoBorderlands3.configure(background='black', fg='orange', font=font_prim)
infoBorderlands3.pack()

'''
-------------------------------------------------------------------------------------
info section
-------------------------------------------------------------------------------------
'''

labelSelectedCodeList = Label(frame, text='------------------------------\nPC : Borlderlands 2\n------------------------------')
labelSelectedCodeList.configure(background=color_wbg, fg=color_fg, font=font_prim)
labelSelectedCodeList.pack()

labelCodeInfo = Label(frame, text='Click on a code to\n copy it to the clipboard!', fg=color_sec, width=50)
labelCodeInfo.configure(background=color_wbg, font=font_prim)
labelCodeInfo.pack()

labelInfo = Label(frame, text='\nShiftCodes are parsed from')
labelInfo.configure(background=color_wbg, fg=color_fg, font=font_prim)
labelInfo.pack()

link0 = Label(frame, text="orcz.com : Borderlands 1", cursor="target")
link0.configure(background=color_wbg, fg=color_sec, font=font_prim)
link0.pack()
link0.bind("<Button-1>", lambda e: callback(url_b1))

link1 = Label(frame, text="orcz.com : Borderlands 2", cursor="target")
link1.configure(background=color_wbg, fg=color_sec, font=font_prim)
link1.pack()
link1.bind("<Button-1>", lambda e: callback(url_b2))

link2 = Label(frame, text="orcz.com : Borderlands - Pre Sequel", cursor="target")
link2.configure(background=color_wbg, fg=color_sec, font=font_prim)
link2.pack()
link2.bind("<Button-1>", lambda e: callback(url_bps))

link3 = Label(frame, text="orcz.com : Borderlands 3", cursor="target")
link3.configure(background=color_wbg, fg=color_sec, font=font_prim)
link3.pack()
link3.bind("<Button-1>", lambda e: callback(url_b3))

link4 = Label(frame, text="orcz.com : Borderlands VIP", cursor="target")
link4.configure(background=color_wbg, fg=color_sec, font=font_prim)
link4.pack()
link4.bind("<Button-1>", lambda e: callback(url_vip))

labelInfo = Label(frame, text='\nMade with ❤ by')
labelInfo.configure(background=color_wbg, fg=color_fg, font=font_prim)
labelInfo.pack()

link5 = Label(frame, text="devmarcstorm", cursor="heart")
link5.configure(background=color_wbg, fg=color_sec, font=font_prim)
link5.pack()
link5.bind("<Button-1>", lambda e: callback("https://github.com/devmarcstorm"))

'''
-------------------------------------------------------------------------------------
ListBox
-------------------------------------------------------------------------------------
'''

listBox = Listbox(frameL, width=40, height= 100, font=font_prim)
listBox.bind('<<ListboxSelect>>', onSelect)
listBox.pack()

print(
'''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|B|l|.|C|o|d|e|S|c|r|a|p|e|r|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Codes are parsed from:

http://orcz.com/Borderlands:_Golden_Key
http://orcz.com/Borderlands_2:_Golden_Key
http://orcz.com/Borderlands_Pre-Sequel:_Shift_Codes
http://orcz.com/Borderlands_3:_Shift_Codes
http://orcz.com/Borderlands_VIP

Thanks to orcz.com for providing the codes under the license:
"Creative Commons Attribution Non-Commercial Share Alike unless otherwise noted"

-----------------------------------------------------------------------------------------------------
<> with ♥ by devmarcstorm - https://github.com/devmarcstorm/Borderlands-ShiftCodes-WebScraper
-----------------------------------------------------------------------------------------------------

!The codes are loaded in the background. After that, the GUI is available!
!This should not take longer than 20 seconds!

'''
)

# pc codes
print('[1 / 5] getting pc codes...')
list_pc_b1 = scraper.get_codes(url_b1, cell_pc)
list_pc_b2 = scraper.get_codes(url_b2, cell_pc)
list_pc_bps = scraper.get_codes(url_bps, cell_pc)

# ps4 codes
print('[2 / 5] getting ps4 codes...')
list_ps4_b1 = scraper.get_codes(url_b1, cell_ps4)
list_ps4_b2 = scraper.get_codes(url_b2, cell_ps4)
list_ps4_bps = scraper.get_codes(url_bps, cell_ps4)

# xbox codes
print('[3 / 5] getting xbox codes...')
list_xbox_b1 = scraper.get_codes(url_b1, cell_xbox)
list_xbox_b2 = scraper.get_codes(url_b2, cell_xbox)
list_xbox_bps = scraper.get_codes(url_bps, cell_xbox)

# multiplatform codes
print('[4 / 5] getting b3 codes...')
list_multi_b3 =  scraper.get_codes(url_b3, 4, 10)

# borderlands vip codes
print('[5 / 5] getting vip codes...')
list_vip = scraper.get_codes(url_vip, 0, 6, 1, 0)

fill_list(list_pc_b2)

root.geometry("680x600")
root.resizable(False, False)
root.mainloop()