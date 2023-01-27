import tkinter as tk
from datetime import timedelta
import random

# some constants used in the code
BLUE='#B9F3FC'
BLUETHICK='#AEE2FF'
RED='#FF0000'
YELLOW='#7B2869'
RESET=False
previous_timer=None
CLICKED=0
GREEN='#54B435'

#some good works added in the app when the study session is going on
work_list=['Working','Great','Amazing','Keep Going','Don\'t quit']

#some colours
thick_colour=['#00425A','#1F8A70','#BFDB38','#FC7300']
success=0

#window is like a screen object where it opens
window=tk.Tk()
#sets the title
window.title("Productivity App")
#height and width of the screen
window.minsize(width=400,height=400)

#padding some space in all sided and making the background as white
window.config(padx=70,pady=70,bg='white')

#making a small canvas to add image to it and setting highlightthicknedd to 0 so the border will not appear
canvas = tk.Canvas(window, width=300, height=300,highlightthickness=0)

#setting the main text to the app and updates based on the study/break. if it's break means relax would be displayed and if not some good words displays
title=tk.Label(text="Do it Today",fg=GREEN,bg='white',font=('courier',25,'bold'))
#used grid so it fits in the middle column of first row
title.grid(column=1,row=0)

#if the study session completed then it add one tick mark
completed_rep=tk.Label(text="",fg=BLUETHICK,bg='white',font=('courier',25,'bold'))
completed_rep.grid(column=1,row=2)
#intitialie rep to 0
rep=0

#reset fbutton functionality. if only one times clicked then it's pause the timer usimg timer_running set to false so it stops.
#if we hit again on resume it the parameter set to true and continutes from where it was there previously.
def reset_button():
    global CLICKED
    global success
    #clicked is used to track wheter pause or reset or resume button clicked
    if CLICKED==0:
        timer_running.set(False)
        
        #reduced one over here because as soon as hitting this pause button one tick mark is added so reducing it over here it was added because
        #of the else in count_down time has executed
        success-=1
        reset_button.config(text='Resume')
        CLICKED+=1
        
    #if it hits on resume then it resumes the timer.
    elif CLICKED==1:
        timer_running.set(True)
        if time_left==0:
            print('here')
            success-=1
        count_down(time_left)

        CLICKED+=1
        reset_button.config(text='Reset')
        
    #if it hits on reset then everything would be resetted. timer resetted and reps resetted and ticks marks resetted.
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

#count down timer runs
def count_down(count):
    global time_left
    time_left = count
    global success
    #if there is still seconds left and reset is false and timer running is still there then this will executed
    if count>=0 and RESET==False and timer_running.get()==True:
        seconds = count
        #here seconds has been converted to this formal '00:00" for better understanding time
        time = timedelta(seconds=seconds)
        
        #using this wonle we will update the time in the canvas
        
        canvas.itemconfig(timer_text,text=time)
        global previous_timer
        
        #for every 1 second the timer would update using this after method in the wiondow. means refresh for every second and the count of the seconds decrease by 1
        
        previous_timer=window.after(1000,count_down,count-1)
        #if the study session starts means the button is in disable state . so to enable this after the study session is completed.
        if count==0:
            start_button.config(state='normal')
    else:
        #used for adding the tick marks to track how many study sessions has completed.
        if rep%2!=0:
            success+=1
        completed_rep.config(text='✔'*success,fg=GREEN)
#on click function used to make the session times.
def on_click():
    global rep
    global CLICKED
    print('clicked')
    #if the reps are even means then it's study session
    if rep%2==0:
        title.config(text=random.choice(work_list),fg=random.choice(thick_colour))
        #when the start button hits then the button name should be change to break and diasabled
        start_button['text'] = 'Break'
        start_button.config(state='disable')
        reset_button.config(text='Pause')
        CLICKED=0
        count_down(25* 60)
    #if it is break session then breaks for 5 minutes.
    elif rep%2!=0:
        title.config(text='Relax', fg=random.choice(thick_colour))
        start_button['text'] = 'Start'
        start_button.config(state='disable')
        count_down(5 * 60)
    #rep is increased.
    rep+=1


#
timer_running = tk.BooleanVar()
timer_running.set(True)

#buttons
start_button=tk.Button(text='start',highlightthickness=0,command=on_click)
start_button.grid(column=0,row=2)
start_button.configure(font=('calibri', 10, 'bold', 'underline'),fg=YELLOW,bg='white',height=1,width=8)

reset_button=tk.Button(text='Pause',highlightthickness=0,command=reset_button)
reset_button.grid(column=2,row=2)
reset_button.configure(font=('calibri', 10, 'bold', 'underline'),fg=YELLOW,bg='white',height=1,width=8)




#image of the circle
pic=tk.PhotoImage(file='Circle_frame.svg.png')
canvas.create_image(150,150,image=pic)
canvas.configure(bg='white')

#timer text starts from 00:00
timer_text=canvas.create_text(150,150,text="00:00",font=('courier',25,'bold'),fill=RED)

canvas.grid(column=1,row=1)
window.mainloop()
