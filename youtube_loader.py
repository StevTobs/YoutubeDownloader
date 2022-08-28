from tkinter import *
from tkinter import filedialog

#Important packages
# conda install pip ()
# pip install moviepy %OR conda install moviepy
# pip install pytube
# To install using pip at the first time, we need to set new environment path

from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

#Use for move the downdloaded file to the selected path
import shutil 

#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text = path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    # print(user_path)
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move tile ti selected directory
    shutil.move( mp4_video, user_path )
    screen.title('Download Complete! Download Another File...')
    


#Set blank canvas
screen = Tk()
title = screen.title('Youtube Download')
# canvas = Canvas(screen, width = 500, height=500, background= "white")
canvas = Canvas(screen, width = 500, height=500)

canvas.pack()

#image Logo
logo_img = PhotoImage(file = 'yt.png')

#resize the image
logo_img = logo_img.subsample(1,1) # (1,1) : h1, (2,2) : h2 ...

#display the logo
canvas.create_image(250, 80, image=logo_img)

#link_fieled
link_field = Entry(screen, width=50 )
link_label = Label(screen, text="Enter Download Link:", font=('courier', 15))


#Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)



#Select Path for saving the file
path_label = Label(screen, text="Select Path for Download", font=('courier', 15))
select_btn = Button(screen, text="Select", command= select_path)

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Download_btns
download_btn = Button(screen, text="Download File", command=download_file)

#Add to canvas
canvas.create_window(250, 390, window=download_btn )

screen.mainloop()



