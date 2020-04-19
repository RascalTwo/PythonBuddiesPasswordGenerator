import tkinter as tk
import tkinter.colorchooser as tkColorChooser
import tkinter.messagebox as tkMessageBox
from styled_widgets import Button, Entry
import json
from PIL import ImageColor
import colorsys


class Main(tk.Tk):
    def __init__(self):

        self.config_file = 'config.json'
        self.load_config(self.config_file)

        tk.Tk.__init__(self)
        # basic config
        tk.Tk.wm_geometry(self, '450x700')
        tk.Tk.wm_resizable(self, False, False)
        tk.Tk.wm_title(self, 'Python Buddies - Password Generator')
        try:
            tk.Tk.config(self, bg = self.style_config['background'])
            tk.Tk.fg = self.style_config['foreground']
        except:
            tkMessageBox.showwarning('Warning', 'Failed to load config')
            self.destroy()
        # create variable
        self.current_frame = None
        # set home frame
        self.switch_frame(MainMenu)
    
    # this function switches the current frame for the frame entered
    def switch_frame(self, frame):
        try:
            self.current_frame.destroy()
        except:
            pass
        self.current_frame = frame(self)
        self.current_frame.pack()

    def load_config(self, cfg_file):
        _file = open(cfg_file, 'r')
        text = _file.read()
        self.style_config = json.loads(text)
    


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = master['bg'])

        self.config_file = 'config.json'
        self.load_config(self.config_file)

        try:
            tk.Tk.config(self, bg = self.style_config['background'])
            tk.Tk.fg = self.style_config['foreground']
        except:
            tkMessageBox.showwarning('Warning', 'Failed to load config')
            self.destroy()

        self._master = master
        container = tk.Frame(self, bg = self.style_config['background'])
        container.pack()

        tk.Label(container, text = "Background", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 0, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("background")).grid(row = 0, column = 1)

        tk.Label(container, text = "Foreground", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 1, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("foreground")).grid(row = 1, column = 1)

        tk.Label(container, text = "Entry Background", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 2, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("entry_background")).grid(row = 2, column = 1)

        tk.Label(container, text = "Entry Foreground", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 3, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("entry_foreground")).grid(row = 3, column = 1)

        tk.Label(container, text = "Entry Alt Foreground", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 4, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("entry_alt_foreground")).grid(row = 4, column = 1)

        tk.Label(container, text = "Button Foreground", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 5, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("button_foreground")).grid(row = 5, column = 1)

        tk.Label(container, text = "Button Active Foreground", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 6, column = 0)
        tk.Button(container, text = "Select", font = ("Arial", 20, "bold"), command = lambda: self.select_color("button_active_foreground")).grid(row = 6, column = 1)

        self.button_colors = ["Red", "Yellow", "Green", "Cyan", "Light Blue", "Blue", "Purple", "Pink"]
        self.button_color = tk.StringVar(self)
        tk.Label(container, text = "Button Color", font = ("Arial", 20, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).grid(row = 7, column = 0)
        tk.OptionMenu(container, self.button_color, *self.button_colors, command = lambda x: self.select_color("button_color")).grid(row = 7, column = 1)

        tk.Label(self, text = "Preview", font = ("Arial", 35, "bold"), bg = self.style_config['background'], fg = self.style_config['foreground']).pack()
        self.btn = Button(self, text = "Button")
        self.btn.pack(pady = 5)
        self.ent1 = Entry(self, alt_text = "Alternate text")
        self.ent1.pack(pady = 5)
        self.ent2 = Entry(self, alt_text = "Alternate text")
        self.ent2.pack(pady = 5)
        tk.Label(self, font = ("Arial", 50, "bold"), bg = self.style_config['background']).pack(side = "bottom")

        #------------------------------------
    def select_color(self, key):
        if key != "button_color":
            color = tkColorChooser.askcolor()[1]
            if color == None:
                tkMessageBox.showwarning('Warning', 'No color selected')
                return
        else:
            hues = [0, 30, 70, 100, 130, 160, 190, 220]
            index = self.button_colors.index(self.button_color.get())
            color = hues[index]
            print(color, "=", self.button_color.get())

        

        self.style_config[key] = color
        _file = open(self._master.config_file, 'w')
        _file.write(json.dumps(self.style_config))
        _file.close()
        self._master.switch_frame(MainMenu)
        self.reset_custom_widgets()
        tkMessageBox.showinfo('Info', 'Some changed will take effect only when you restart the program')
        

    def load_config(self, cfg_file):
        _file = open(cfg_file, 'r')
        text = _file.read()
        self.style_config = json.loads(text)

    def reset_custom_widgets(self):
        self.btn.pack_forget()
        self.ent1.pack_forget()
        self.ent2.pack_forget()

        self.btn = Button(self, text = "Button", command = lambda:  self._master.switch_frame(MainMenu))
        self.btn.pack(pady = 5)
        self.ent1 = Entry(self, alt_text = "Alternate text")
        self.ent1.pack(pady = 5)
        self.ent2 = Entry(self, alt_text = "Alternate text")
        self.ent2.pack(pady = 5)


if __name__ == "__main__":
    window = Main()
    window.mainloop()