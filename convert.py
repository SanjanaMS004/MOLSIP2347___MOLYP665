from tkinter import*
from tkinter import filedialog
import moviepy.editor
from tkinter import messagebox
import PIL.ImageTk as imtk 

win= Tk()
win.geometry('950x580')
win.resizable(width=False, height=False)
win.title("Converter")

bg= imtk.PhotoImage(file="bg_5.png")

win.iconbitmap("icon.png")

my_canvas= Canvas(win)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image=bg,anchor="nw")

my_canvas.create_text(710,120,text="Video to Audio Converter", font=("Trebuchet MS",19,"bold"))

my_canvas.create_text(700,180,text="Select a vedio file to convert", font=("Trebuchet MS",12))


def OpenFile():
    fpath= filedialog.askopenfilename(title="select a video to convert.", filetype=( ("MP4","*.mp4"), ("AVI","*.avi"), ("MKV","*.mkv"), ("MOV","*.mov"), ("WMV","*.wmv"), ("FLV","*.flv"), ("3GP","*.3gp")  ))
    video = moviepy.editor.VideoFileClip(fpath)
    messagebox.showinfo('Selected', fpath+' has been selected!')

    my_canvas.create_text(700,260,text="Video Selected", font=("Trebuchet MS",9))

    def Convert_vid():
        apath = filedialog.asksaveasfilename(title="Select file to store audio.")
        format='.mp3'
        aud=video.audio
        aud.write_audiofile(f'{apath}{format}')
        messagebox.showinfo('Done','Video converted and saved successfully!!')
        my_canvas.create_text(700,350,text="Completed!", font=("Trebuchet MS",9))


    btn02=Button(win,text="Convert", font=("Trebuchet MS",9,'bold'), command=Convert_vid, width=15, bg='#C3B6F4', border=0)
    btn02_window=my_canvas.create_window(700,300,window=btn02)

    
btn01=Button(win,text="Open", font=("Trebuchet MS",9,'bold'), command=OpenFile, width=15, bg='#C3B6F4', border=0) 
btn01_window=my_canvas.create_window(700,220,window=btn01)


win.mainloop()
