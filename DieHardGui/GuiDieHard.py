#+-----------------+

#Die Hard Gui

#+-----------------+
from tkinter import *
from tkinter import font
from uncleengineer import thaistock

GUI = Tk()
GUI.geometry('500x700')
GUI.state('zoomed')
GUI.title('Dashboard Die Hard 4.0')

#background Color
bg = '#2b2b2b'
fg = '#12ff2a'

ww = 1920
wh = 1080

GUI.configure(background = bg)

#fullscreen.Version 2
GUI.attributes('-fullscreen', False)

GUI.bind('<F10>', lambda event: 
GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))

#Font
f1 = ('Sprite coder', 20, 'bold')
f2 = ('Sprite coder', 15, 'bold')

#Cavas
#display = 1920 x 1080
canvas = Canvas(GUI, width= ww, height= wh, background= bg, 
bd= 0, relief= 'ridge', highlightthickness= 0)
canvas.place(x=0, y=0)

def MyFram(x,y, width=300, height=100):
    frame1 = canvas.create_rectangle(0, 0, width, height, fill=bg, outline=fg)
    canvas.move(frame1, x, y)

def FixedLabel(text='This is a Text',x= 50, y= 50, font= f1, color = fg):
    L1 = Label(GUI, text= text, font= f1, bg= bg, fg= color, justify=LEFT)
    L1.place(x=x,y=y)

#F1
MyFram(20, 20)
FixedLabel('MY COIN', 50, 100)
FixedLabel('MYPROGRAM', 50, 200, font=('Sprite coder', 20, 'bold'), color= 'yellow')

# IOT Frame
MyFram(20, 300, 300, 200)
FixedLabel('IOT-Device 1', 50,285,font=f2)
FixedLabel('Temp( c ): 30\nHUMID ( % ): 55 \n STATUS : OK',25, 320, font=f2)

# IOT Frame
MyFram(20, 600, 300, 200)
FixedLabel('IOT-Device 2', 50,585,font=f2)
FixedLabel('Temp( c ): 30\nHUMID ( % ): 55 \n STATUS : OK',25, 620, font=f2)

# CHECk STOCK
MyFram(500, 20, 500, 200)
FixedLabel('STOCK', 520, 7.5, font=f2)

V_stockname = StringVar() #StingVar ตัวแปรสำหรับ GUI
 
E1 = Entry(GUI, textvariable=V_stockname, font=f1, bg=bg, fg=fg)
E1.configure(insertbackground=fg) #Cursor color
E1.configure(highlightthickness=2, highlightbackground=fg, highlightcolor=fg)
E1.place(x= 570,y= 40)

V_result = StringVar()
V_result.set('MY STOCK : 50 BAHT ')

LResult = Label(GUI, textvariable= V_result, font= f1, bg= bg, fg= fg, justify=LEFT)
LResult.place(x=570,y=80)

def CheckStockPrice(event):
    stockname = V_stockname.get()
    print(stockname)
    result = thaistock(stockname)
    text = 'STOCK COD : {}\nPRICE : {}'.format(result[0], result[1])
    V_result.set(text)

E1.bind('<Return>', CheckStockPrice)

GUI.mainloop()