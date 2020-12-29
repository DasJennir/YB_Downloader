from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 


Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please, Choose a Directory !!!",fg="#D10D0D")


list_entries = []


def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
    total_urls = 0
    result = str(ytdEntry.get())
    list_entries.append(result)
    for num in list_entries:
        total_urls += 1
    resultLabel.config(text=total_urls)
    print(list_entries)
    ytdEntry.delete(0,END)



#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    
    try: 
        text_file = open(f"{Folder_Name}/Urls.txt", "a")
        text_file.write("All Your Urls: %s\n" % list_entries)

    except:
        ytdError.config(text = "Select a location to download the file.")

    for url in list_entries:

        try:
            if(len(url)>5):
                ytdError.config(text="")
                yt = YouTube(url)


                if(choice == choices[0]):
                    select = yt.streams.filter(resolution='1080p').first()

                elif(choice == choices[1]):
                    select = yt.streams.filter(progressive=True).last()

                elif(choice == choices[2]):
                    select = yt.streams.filter(progressive=True,file_extension='mp4').last()
                    
                elif(choice == choices[3]):
                    select = yt.streams.filter(only_audio=True).first()

                else:
                    ytdError.config(text="A network error has occured. Please, try again.",fg="#D10D0D",font=("jost bold",10,))


            
                #download function
                select.download(Folder_Name)
                ytdError.config(text="Download Completed !!!",fg="green",font=("jost bold",15,))
                downloadbtn.config(bg="green")

            elif(len(url)<5):

                ytdError.config(text="Your url is too short !!!", fg="#D10D0D",font=("jost bold",15,))

            else:
                ytdError.config(text="You haven't selected any url !!!", fg="#D10D0D",font=("jost bold",15,))
        except:
            ytdError.config(text="The url is invalid !!!", fg="#D10D0D",font=("jost bold",15,))

    

root = Tk()
root.title("Pocket Downloader ")
root.geometry("400x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.
root.configure(bg='#49A')

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URLs",font=("jost",15, 'bold'))
ytdLabel.grid(row=0,column=0, columnspan=5)
ytdLabel.configure(bg='#49A')
#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid(row=1,column=0,columnspan=5)


# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry,bg="#FF0000",fg="white",width=8)
enterEntry.grid(row=1,column=4)


#Asking save file label
saveLabel = Label(root,text="File Location",font=("jost",15, 'bold'))
saveLabel.grid(row=3, column=0, pady=20)
saveLabel.configure(bg='#49A')


#btn of save file
saveEntry = Button(root,width=10,bg="#FF0000",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid(row=4, column=0)

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15, 'bold'))
ytdQuality.grid(row=3, column=2,columnspan=3, pady=20)
ytdQuality.configure(bg='#49A')

#combobox
choices = ["1080p","720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid(row=4, column=2,columnspan=3, padx=20, pady=20)


#Error Msg location
locationError = Label(root,text="", fg="red",font=("jost bold",10,'bold'))
locationError.grid(row=7, column=0,columnspan=2)
locationError.configure(bg='#49A')


#donwload btn
downloadbtn = Button(root,text="Download",width=10,bg="#FF0000",fg="white",command=DownloadVideo)
downloadbtn.grid(row=8, column=0,columnspan=5, padx=20, pady=20)


urlLabel = Label(root, text = "Total Number of Urls: ",width=50,font=("jost bold",10, 'bold'))
urlLabel.grid(row=9, column=0,columnspan=5)
urlLabel.configure(bg='#49A')
resultLabel = Label(root, text = "",width=50,font=("jost bold",10))
resultLabel.grid(row=10, column=0,columnspan=5,pady = 10, padx = 10)
resultLabel.configure(bg='#49A')


#Error Msg
ytdError = Label(root,text="Thanks for using Pocket Downloader !!!",fg="black",font=("jost bold",15, 'bold'))
ytdError.grid(row=11,column=0,columnspan=5)
ytdError.configure(bg='#49A')





#developer Label
root.mainloop()