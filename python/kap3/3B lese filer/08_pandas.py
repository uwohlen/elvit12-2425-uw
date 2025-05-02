import math
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
    
file_path_c = "innvandring.csv"

#read and analyse using pandas dataframes
dfc = pd.read_csv(file_path_c, encoding = "Windows 1252", skiprows=1, sep = ";")

heads = dfc.columns.to_list()
#debugging: un-comment this print statement
#print(heads)

#Dictionary to contain various information and booleans
countries = {}
for c in dfc[heads[0]]:
    if c not in countries.keys():
        countries[c] = {"show": True, "imm_sum": 0}
years = []
for y in dfc[heads[1]]:
    if y not in years:
        years.append(y)

years.sort()
#print(years)
sums = {}

i = 0
while True:    
    try:
        for c in countries.keys():
            #print(c)
            if dfc.loc[i][heads[0]]==c:
                countries[c]["imm_sum"] +=int(dfc.loc[i][heads[2]])

                if dfc.loc[i][heads[0]] not in sums.keys():
                    sums[c]=0
                    #print(f"starter nytt land: {c}")
                else:
                    #print(dfc.loc[i][heads[2]])
                    sums[c] += int(dfc.loc[i][heads[2]])
            else:
                pass
    except:
        break
    i +=1

#debugging: un-comment this print statement
print(countries)
print(sums)
for k,v in sums.items():
    print(f"For {k} er verdien {int(v)}")

#debugging: un-comment this print statement
#print(countries)

#make sure that the dataframe displays all rows in the data set
pd.options.display.max_rows = 9999

def oppgave1():
    #oppgave 1: Tabell-liknende struktur
    print(dfc)
    x = []
    y = []

    for k, v in sums.items():
        x.append(k[:12])
        y.append(v)
    fig, ax = plt.subplots(1,1)
    ax.bar(x,y,)
    ax.set_xticklabels(x, rotation=90, ha='center', va='top')
    ax.set_ylabel("Land")
    ax.set_xlabel("Antall folk")
    ax.set_title("Sum av innvandring fra land siden 1970")
    #fig = plt.figure()
    #ax.title("Hei")
    #ax.legend()
    #fig.legend()
    plt.show()

#Oppgave: Grafisk fremstilling av noen valgte verdensdeler
def oppgave2():
    #run this to solve this task
    
    x = dfc[dfc[heads[0]]=="Afrika"][heads[1]]
    y = []
    fig, ax = plt.subplots(1,1)
    for c in countries.keys():
        yy = dfc[dfc[heads[0]]==c][heads[2]]
        y.append(yy)
        ax.plot(x, yy, label = c)
        #ax.set_ylabel(c)
    plt.grid()
    plt.legend()
    plt.show()

class tk_btn():

    def __init__(self, root, country, label, main_app):
        self.root = root
        self.strv = tk.StringVar()
        self.country = country
        self.strv.set(country)
        self.intv = tk.IntVar()
        self.intv.set(1)
        self.label = label
        self.main_app = main_app
        self.btn = ttk.Button(master = self.root, command = self.show, textvariable=self.strv)

    def show(self):
        print(f"btn.intv = {self.intv.get()}")
 
        self.intv.set(self.intv.get()*(-1))

        if self.intv.get()<0:
            self.label.strv.set("OFF")
        else:
            self.label.strv.set("ON")
        self.main_app.update()
                
class tk_combo():

    def __init__(self, root, label, main_app, years):
        self.root = root
        self.strv = tk.StringVar()
        self.strv.set("Choose year")
        self.intv = tk.IntVar()
        #self.intv.set(years[0])
        self.label = label
        self.main_app = main_app
        self.btn = ttk.Combobox(master = self.root, values = years, textvariable=self.intv)                

class tk_lbl():

    def __init__(self, root):
        self.root = root
        self.strv = tk.StringVar()
        self.strv.set("ON")
        self.lbl = ttk.Label(master = self.root, textvariable=self.strv)

class tk_lbl2():

    def __init__(self, root, text: str = ""):
        self.root = root
        self.strv = tk.StringVar()
        self.strv.set(text)
        self.lbl = ttk.Label(master = self.root, textvariable=self.strv)

class main_app():
    
    def __init__(self):
        pass

    def add_gui(self):

        self.fig, self.ax = plt.subplots(1,1)
        
        self.widgets = []
        self.frames = []
        self.tk_btns = []
        self.tk_lbls = []
        self.tk_combos = []
        self.tk_lbl2s = []

        self.root = tk.Tk()
        self.root.wm_title("Embedded in Tk")
        self.root.geometry("1000x800")

        #container for the buttons to choose countries. I want to have them in a rectangular grid
        frame_countries = ttk.Frame(master = self.root, padding = 10)
        self.frames.append(frame_countries)
        frame_years = ttk.Frame(master =self.root, padding = 40)
        self.frames.append(frame_years)

        frame_graph = ttk.Frame(master =self.root, padding = 40)
        self.frames.append(frame_graph)
        n = len(list(countries.keys()))

        #print(len(n))

        cols = 3
        rows = math.ceil(n/cols)
        print(f"Rader: {rows}. Kolonner: {cols}")

        rc = 0
        cc = 0
        i = 0
        for c in countries.keys():
            print(f"Country = {c}")
            self.tk_lbls.append(tk_lbl(frame_countries))
            self.tk_btns.append(tk_btn(frame_countries,c, self.tk_lbls[i], self))
            if cc>=6:
                cc = 0
                rc +=1

            self.tk_btns[i].btn.grid(row = rc, column = cc)
            cc +=1
            self.tk_lbls[i].lbl.grid(row = rc, column = cc)
            cc +=1
            i +=1
        i = 0        
        self.tk_lbl2s.append(tk_lbl2(frame_years, "Fra år "))       
        self.tk_lbl2s[i].lbl.grid(row = 0,column = 0)

        self.tk_combos.append(tk_combo(frame_years, self.tk_lbl2s[i],self, years))
        self.tk_combos[i].btn.grid(row = 0,column = 1)
        i +=1
        self.tk_lbl2s.append(tk_lbl2(frame_years, "Til år "))       
        self.tk_lbl2s[i].lbl.grid(row = 1,column = 0)

        self.tk_combos.append(tk_combo(frame_years, self.tk_lbl2s[i],self, years))
        self.tk_combos[i].btn.grid(row = 1,column = 1)

        plot_button = ttk.Button(frame_years, command = self.update, text = "Tegn graf")
        plot_button.grid(row = 2,column = 0)
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_graph)  # A tk.DrawingArea.
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH)
        
        self.widgets.append(self.canvas.get_tk_widget())
        # pack_toolbar=False will make it easier to use a layout manager later on.
        self.toolbar = NavigationToolbar2Tk(self.canvas, frame_graph, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(side = tk.TOP, fill = tk.X)

        self.widgets.append(self.toolbar)
        for frame in self.frames:
            frame.pack()
        #plt.show()

        self.root.mainloop()

    def update(self):
        self.ax.clear()
        self.canvas.draw()


        for b in self.tk_btns:
            c = b.country
            print(f"In update... country = {c}")
            if b.intv.get()>0:
                condition1 = (dfc[heads[0]]==c) 
                condition2 = (dfc[heads[1]]>=self.tk_combos[0].intv.get()) & (dfc[heads[1]]<=self.tk_combos[1].intv.get())
                x = dfc[condition1 & condition2][heads[1]]
                print(x)
                y = dfc[condition1 & condition2][heads[2]]  
                #print(y)
                self.ax.plot(x, y, label = c[:15])
            #ax.set_ylabel(c)
        """# Example data for plotting
        x = list(sums.keys())  # X-axis labels: country names
        y = list(sums.values())  # Y-axis data: immigration sums
        
        self.ax.bar(x, y)  # Create a bar plot
        #ax.set_xticklabels(x, rotation=90, ha='center', va='top')
        self.ax.set_ylabel("Antall folk")
        self.ax.set_title("Sum av innvandring fra land siden 1970")
        self.fig.tight_layout(pad=2.0)  # Add a bit more padding between figure edges and elements"""
        self.canvas.draw()

        
def main():
    #oppgave1()
    #oppgave2()
    app = main_app()
    app.add_gui()

if __name__=="__main__":
    main()