import tkinter as tk
from datetime import timedelta
import random


BLUE='#B9F3FC'
BLUETHICK='#AEE2FF'
RED='#FF0000'
YELLOW='#7B2869'
RESET=False
previous_timer=None
CLICKED=0
GREEN='#54B435'
work_list=['Working','Great','Amazing','Keep Going','Don\'t quit']
thick_colour=['#00425A','#1F8A70','#BFDB38','#FC7300']
success=0
window=tk.Tk()
window.title("Productivity App")
window.minsize(width=400,height=400)


window.config(padx=70,pady=70,bg='white')
canvas = tk.Canvas(window, width=300, height=300,highlightthickness=0)
title=tk.Label(text="Do it Today",fg=GREEN,bg='white',font=('courier',25,'bold'))
title.grid(column=1,row=0)
completed_rep=tk.Label(text="",fg=BLUETHICK,bg='white',font=('courier',25,'bold'))
completed_rep.grid(column=1,row=2)
rep=0
def reset_button():
    global CLICKED
    global success
    if CLICKED==0:
        timer_running.set(False)
        success-=1
        reset_button.config(text='Resume')
        CLICKED+=1
    elif CLICKED==1:
        timer_running.set(True)
        if time_left==0:
            print('here')
            success-=1
        count_down(time_left)

        CLICKED+=1
        reset_button.config(text='Reset')
    else:

        RESET=True
        start_button.config(state='normal')
        window.after_cancel(previous_timer)
        time="00:00"
        canvas.itemconfig(timer_text, text=time)
        global rep
        rep=0
        completed_rep.config(text="Data Saved")
        start_button.config(text='start')
        reset_button.config(text='Pause')
        CLICKED=0

        success=0

def count_down(count):
    global time_left
    time_left = count
    global success
    if count>=0 and RESET==False and timer_running.get()==True:
        seconds = count
        time = timedelta(seconds=seconds)
        canvas.itemconfig(timer_text,text=time)
        global previous_timer
        previous_timer=window.after(1000,count_down,count-1)
        if count==0:
            start_button.config(state='normal')
    else:
        if rep%2!=0:
            success+=1
        completed_rep.config(text='✔'*success,fg=GREEN)




def on_click():
    global rep
    global CLICKED
    print('clicked')
    if rep%2==0:
        title.config(text=random.choice(work_list),fg=random.choice(thick_colour))
        start_button['text'] = 'Break'
        start_button.config(state='disable')
        reset_button.config(text='Pause')
        CLICKED=0
        count_down(1 * 4)
    elif rep%2!=0:
        title.config(text='Relax', fg=random.choice(thick_colour))
        start_button['text'] = 'Start'
        start_button.config(state='disable')
        count_down(1 * 4)

    rep+=1


timer_running = tk.BooleanVar()
timer_running.set(True)

start_button=tk.Button(text='start',highlightthickness=0,command=on_click)
start_button.grid(column=0,row=2)
start_button.configure(font=('calibri', 10, 'bold', 'underline'),fg=YELLOW,bg='white',height=1,width=8)

reset_button=tk.Button(text='Pause',highlightthickness=0,command=reset_button)
reset_button.grid(column=2,row=2)
reset_button.configure(font=('calibri', 10, 'bold', 'underline'),fg=YELLOW,bg='white',height=1,width=8)





pic=tk.PhotoImage(file='Circle_frame.svg.png')
canvas.create_image(150,150,image=pic)
canvas.configure(bg='white')


timer_text=canvas.create_text(150,150,text="00:00",font=('courier',25,'bold'),fill=RED)

canvas.grid(column=1,row=1)
window.mainloop()