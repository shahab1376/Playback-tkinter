## Playback GUI by tkinter

# Importing libraries
import tkinter as tk
from tkinter import ttk
import json
import time
import math
import os


FONT= ("Verdana", 10)
FONT2 = ("Purisa",12)

# The main frame class inherits the tk.TK
class playback(tk.Tk):

    def __init__(self, *args, **kwargs):
        # initializing the tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        # Set title for frame
        tk.Tk.wm_title(self,'Playback GUI')
        # Packing the frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Adding the frame StartPage
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        
        

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        # playback counter variable
        self.c = 0
        # running flag
        self.running = False
        
        tk.Frame.__init__(self,parent)

        # Top Label
        mainlabel = tk.Label(self, text="Playback GUI", font=FONT)
        mainlabel.grid(row = 0,column = 1 ,padx = 6, pady = 9, sticky = 'nsew')
        # Labels for car#
        Label1 = ttk.Label(self,text = 'Car#',font = FONT)
        Label1.grid(row = 1,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label2 = ttk.Label(self,text = 'Car 1',font = FONT)
        Label2.grid(row = 2,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label3 = ttk.Label(self,text = 'Car 2',font = FONT)
        Label3.grid(row = 3,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label4 = ttk.Label(self,text = 'Car 3',font = FONT)
        Label4.grid(row = 4,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label5 = ttk.Label(self,text = 'Car 4',font = FONT)
        Label5.grid(row = 5,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label6 = ttk.Label(self,text = 'Car 5',font = FONT)
        Label6.grid(row = 6,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label7 = ttk.Label(self,text = 'Car 6',font = FONT)
        Label7.grid(row = 7,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label8 = ttk.Label(self,text = 'Car 7',font = FONT)
        Label8.grid(row = 8,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label9 = ttk.Label(self,text = 'Car 8',font = FONT)
        Label9.grid(row = 9,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label10 = ttk.Label(self,text = 'Car 9',font = FONT)
        Label10.grid(row = 10,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        Label11 = ttk.Label(self,text = 'Car 10',font = FONT)
        Label11.grid(row = 11,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        

        # Current Position Label
        Label12 = ttk.Label(self,text = 'Current Position',font = FONT)
        Label12.grid(row = 1,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        # Current Speed Label
        Label13 = ttk.Label(self,text = 'Current Speed',font = FONT)
        Label13.grid(row = 1,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        # Labels for indicating position
        self.CarLabel1 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel1.grid(row = 2,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel2 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel2.grid(row = 3,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel3 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel3.grid(row = 4,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel4 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel4.grid(row = 5,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel5 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel5.grid(row = 6,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')

        self.CarLabel6 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel6.grid(row = 7,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel7 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel7.grid(row = 8,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel8 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel8.grid(row = 9,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel9 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel9.grid(row = 10,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel10 = ttk.Label(self,text = 'lat =\nlon =',font = FONT2)
        self.CarLabel10.grid(row = 11,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        # Labels for indicating velocity
        self.CarLabel11 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel11.grid(row = 2,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel12 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel12.grid(row = 3,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel13 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel13.grid(row = 4,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel14 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel14.grid(row = 5,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel15 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel15.grid(row = 6,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')

        self.CarLabel16 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel16.grid(row = 7,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel17 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel17.grid(row = 8,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel18 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel18.grid(row = 9,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel19 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel19.grid(row = 10,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        self.CarLabel20 = ttk.Label(self,text = '',font = FONT2)
        self.CarLabel20.grid(row = 11,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        # Start button
        self.button1 = ttk.Button(self,text = 'Play',command = lambda: self.Play())
        self.button1.grid(row = 12,column = 0 ,padx = 6,pady = 9, sticky = 'nsew')
        
        # Pause button
        self.button2 = ttk.Button(self,text = 'Pause',state = 'disabled',command = lambda: self.Pause())
        self.button2.grid(row = 12,column = 1 ,padx = 6,pady = 9, sticky = 'nsew')
        
        #Restart button
        self.button3 = ttk.Button(self,text = 'Restart',state = 'disabled',command = lambda: self.Restart())
        self.button3.grid(row = 12,column = 2 ,padx = 6,pady = 9, sticky = 'nsew')
        
        
    # Play command
    def Play(self):
        self.running = True
        self.button1['state']='disabled'
        self.button2['state']='normal'
        self.button3['state']='normal'
        self.Run()

    # Pause command
    def Pause(self):
        self.button1['state']='normal'
        self.button2['state']='disabled'
        self.button3['state']='normal'
        self.running = False

    # Restart command  
    def Restart(self):
        self.c = 0
        self.button1['state']='disabled'
        self.button2['state']='normal'
        self.button3['state']='normal'
        
    # Main command to run
    def Run(self):
        lat, lon = LoadData()
        if self.running:
            if self.c < (len(lat[0])//CarNum):
                self.CarLabel1.config(text = f'lat = {lat[0][self.c]} \nlon = {lon[0][self.c]}')
                self.CarLabel2.config(text = f'lat = {lat[1][self.c]} \nlon = {lon[1][self.c]}')
                self.CarLabel3.config(text = f'lat = {lat[2][self.c]} \nlon = {lon[2][self.c]}')
                self.CarLabel4.config(text = f'lat = {lat[3][self.c]} \nlon = {lon[3][self.c]}')
                self.CarLabel5.config(text = f'lat = {lat[4][self.c]} \nlon = {lon[4][self.c]}')
                self.CarLabel6.config(text = f'lat = {lat[5][self.c]} \nlon = {lon[5][self.c]}')
                self.CarLabel7.config(text = f'lat = {lat[6][self.c]} \nlon = {lon[6][self.c]}')
                self.CarLabel8.config(text = f'lat = {lat[7][self.c]} \nlon = {lon[7][self.c]}')
                self.CarLabel9.config(text = f'lat = {lat[8][self.c]} \nlon = {lon[8][self.c]}')
                self.CarLabel10.config(text = f'lat = {lat[9][self.c]} \nlon = {lon[9][self.c]}')

                self.CarLabel11.config(text = f'{round(math.sqrt((lat[0][self.c+1] - lat[0][self.c])**2 + (lon[0][self.c+1] - lon[0][self.c])**2),2)}')
                self.CarLabel12.config(text = f'{round(math.sqrt((lat[1][self.c+1] - lat[1][self.c])**2 + (lon[1][self.c+1] - lon[1][self.c])**2),2)}')
                self.CarLabel13.config(text = f'{round(math.sqrt((lat[2][self.c+1] - lat[2][self.c])**2 + (lon[2][self.c+1] - lon[2][self.c])**2),2)}')
                self.CarLabel14.config(text = f'{round(math.sqrt((lat[3][self.c+1] - lat[3][self.c])**2 + (lon[3][self.c+1] - lon[3][self.c])**2),2)}')
                self.CarLabel15.config(text = f'{round(math.sqrt((lat[4][self.c+1] - lat[4][self.c])**2 + (lon[4][self.c+1] - lon[4][self.c])**2),2)}')
                self.CarLabel16.config(text = f'{round(math.sqrt((lat[5][self.c+1] - lat[5][self.c])**2 + (lon[5][self.c+1] - lon[5][self.c])**2),2)}')
                self.CarLabel17.config(text = f'{round(math.sqrt((lat[6][self.c+1] - lat[6][self.c])**2 + (lon[6][self.c+1] - lon[6][self.c])**2),2)}')
                self.CarLabel18.config(text = f'{round(math.sqrt((lat[7][self.c+1] - lat[7][self.c])**2 + (lon[7][self.c+1] - lon[7][self.c])**2),2)}')
                self.CarLabel19.config(text = f'{round(math.sqrt((lat[8][self.c+1] - lat[8][self.c])**2 + (lon[8][self.c+1] - lon[8][self.c])**2),2)}')
                self.CarLabel20.config(text = f'{round(math.sqrt((lat[9][self.c+1] - lat[9][self.c])**2 + (lon[9][self.c+1] - lon[9][self.c])**2),2)}')

                self.button1.after(1000,self.Run)
                self.c += 1
        else:
            self.CarLabel1.config(text = f'lat = {lat[0][self.c]} \nlon = {lon[0][self.c]}')
            self.CarLabel2.config(text = f'lat = {lat[1][self.c]} \nlon = {lon[1][self.c]}')
            self.CarLabel3.config(text = f'lat = {lat[2][self.c]} \nlon = {lon[2][self.c]}')
            self.CarLabel4.config(text = f'lat = {lat[3][self.c]} \nlon = {lon[3][self.c]}')
            self.CarLabel5.config(text = f'lat = {lat[4][self.c]} \nlon = {lon[4][self.c]}')
            self.CarLabel6.config(text = f'lat = {lat[5][self.c]} \nlon = {lon[5][self.c]}')
            self.CarLabel7.config(text = f'lat = {lat[6][self.c]} \nlon = {lon[6][self.c]}')
            self.CarLabel8.config(text = f'lat = {lat[7][self.c]} \nlon = {lon[7][self.c]}')
            self.CarLabel9.config(text = f'lat = {lat[8][self.c]} \nlon = {lon[8][self.c]}')
            self.CarLabel10.config(text = f'lat = {lat[9][self.c]} \nlon = {lon[9][self.c]}')

            self.CarLabel11.config(text = f'{round(math.sqrt((lat[0][self.c+1] - lat[0][self.c])**2 + (lon[0][self.c+1] - lon[0][self.c])**2),2)}')
            self.CarLabel12.config(text = f'{round(math.sqrt((lat[1][self.c+1] - lat[1][self.c])**2 + (lon[1][self.c+1] - lon[1][self.c])**2),2)}')
            self.CarLabel13.config(text = f'{round(math.sqrt((lat[2][self.c+1] - lat[2][self.c])**2 + (lon[2][self.c+1] - lon[2][self.c])**2),2)}')
            self.CarLabel14.config(text = f'{round(math.sqrt((lat[3][self.c+1] - lat[3][self.c])**2 + (lon[3][self.c+1] - lon[3][self.c])**2),2)}')
            self.CarLabel15.config(text = f'{round(math.sqrt((lat[4][self.c+1] - lat[4][self.c])**2 + (lon[4][self.c+1] - lon[4][self.c])**2),2)}')
            self.CarLabel16.config(text = f'{round(math.sqrt((lat[5][self.c+1] - lat[5][self.c])**2 + (lon[5][self.c+1] - lon[5][self.c])**2),2)}')
            self.CarLabel17.config(text = f'{round(math.sqrt((lat[6][self.c+1] - lat[6][self.c])**2 + (lon[6][self.c+1] - lon[6][self.c])**2),2)}')
            self.CarLabel18.config(text = f'{round(math.sqrt((lat[7][self.c+1] - lat[7][self.c])**2 + (lon[7][self.c+1] - lon[7][self.c])**2),2)}')
            self.CarLabel19.config(text = f'{round(math.sqrt((lat[8][self.c+1] - lat[8][self.c])**2 + (lon[8][self.c+1] - lon[8][self.c])**2),2)}')
            self.CarLabel20.config(text = f'{round(math.sqrt((lat[9][self.c+1] - lat[9][self.c])**2 + (lon[9][self.c+1] - lon[9][self.c])**2),2)}')

                
        
            
            
global CarNum; CarNum = 10

# Loading json file
def LoadData():
    lat = [[] for i in range(CarNum)]
    lon = [[] for i in range(CarNum)]
    with open('Dataset.json') as json_file:
        data = json.load(json_file)
    for i in range(CarNum):
        for j in range(len(data)//CarNum):
            if j%CarNum == i:
                lat[i].append(data[j]['position']['latitude'])
                lon[i].append(data[j]['position']['longitude'])
    return lat,lon

# Run the app!
app = playback()
app.geometry("320x720")
app.mainloop()