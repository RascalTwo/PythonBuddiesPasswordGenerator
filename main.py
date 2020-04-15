# tkinter is used for the user interface
import tkinter as tk
import tkinter.messagebox as tkMessageBox
# custom classes made to create good looking buttons and entries
from class_buttons import Button
from class_entry import Entry
# backend
from backend.BetterPassword import passwordIncorporatesName
from backend.random_password import passwordFullyRandom
# copy
import pyperclip
# open links
import webbrowser


# this is the class called when the program starts
# it inherits a tkinter window
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # basic config
        tk.Tk.wm_geometry(self, '450x700')
        tk.Tk.minsize(self, 450, 700)
        tk.Tk.wm_title(self, 'Python Buddies - Password Generator')
        tk.Tk.config(self, bg = '#333333') # hex color #333333 is dark gray
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
    


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Password Generator', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        # using custom buttons for the ui
        Button(root = self, text='Start', command = lambda x: master.switch_frame(SelectMode)).pack(pady = 15)
        Button(root = self, text='Help', command = lambda x: master.switch_frame(Help)).pack(pady = 15)
        Button(root = self, text='Exit', command = lambda x: master.destroy()).pack(pady = 15)

    

class Help(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Help', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        github_link = "https://github.com/RascalTwo/PythonBuddiesPasswordGenerator"
        discord_link = "https://discord.gg/ED8kU5K"

        Button(root = self, text='GitHub', command = lambda x: webbrowser.open(github_link)).pack(pady = 15)
        Button(root = self, text='Discord', command = lambda x: webbrowser.open(discord_link)).pack(pady = 15)
        Button(root = self, text='Back', command = lambda x: master.switch_frame(MainMenu)).pack(pady = 15)



class SelectMode(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Select mode', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        # using custom buttons for the ui
        Button(root = self, text='Fully Random', command = lambda x: master.switch_frame(FullyRandom)).pack(pady = 15)
        Button(root = self, text='Easy to Remember', command = lambda x: master.switch_frame(EasyToRemember)).pack(pady = 15)
        Button(root = self, text='Back', command = lambda x: master.switch_frame(MainMenu)).pack(pady = 15)



class EasyToRemember(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Easy to remember', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        self.entry_length = Entry(self, alt_text='Password length')
        self.entry_length.pack(pady = 10)

        self.entry_name = Entry(self, alt_text='Your name')
        self.entry_name.pack(pady = 10)

        self.entry_year = Entry(self, alt_text='Your birth year')
        self.entry_year.pack(pady = 10)

        Button(root = self, text='Confirm', command = lambda x: self.generate_password(None)).pack(pady = 15)

        self.entry_password = tk.Entry(self, font = ("Arial", 18, "bold"), bg = "#a8a8a8", fg = "#181818", borderwidth = 2, relief = "solid")
        self.entry_password.pack(pady = 15)

        Button(root = self, text='Copy', command = lambda x: pyperclip.copy(self.entry_password.get())).pack(pady = 15)
        Button(root = self, text='Back', command = lambda x: master.switch_frame(SelectMode)).pack(pady = 15)

    
    def generate_password(self, temp):
        try:
            length = int(self.entry_length.get())
        except:
            tkMessageBox.showwarning('Warning', 'Length must be a valid integer')
            return

        birth_year = self.entry_year.get()
        user_name = self.entry_name.get()

        if length < 6:
            tkMessageBox.showwarning('Warning', "Length must be greater than or equal 6")
            return

        if length < len(birth_year) + len(user_name):
            tkMessageBox.showwarning('Warning', 'Length must be equal to or loger than your name and birth year')
            return

        password = passwordIncorporatesName(length = length, name = user_name, birth_year = birth_year)

        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(tk.END, password)




class FullyRandom(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg = '#333333')

        tk.Label(self, text = 'Fully Random Password', font = ('Arial', 25, 'bold'), bg = '#333333', fg = '#ffffff').pack(pady = 30)
        tk.Label(self, bg = '#333333').pack(pady = 25) # spacing

        self.entry_length = Entry(self, alt_text='Password length')
        self.entry_length.pack(pady = 10)

        self.entry_digits = Entry(self, alt_text='Number of digits')
        self.entry_digits.pack(pady = 10)

        self.entry_special = Entry(self, alt_text='Number of special')
        self.entry_special.pack(pady = 10)

        Button(root = self, text='Confirm', command = self.generate_password).pack(pady = 15)

        self.entry_password = tk.Entry(self, font = ("Arial", 18, "bold"), bg = "#a8a8a8", fg = "#181818", borderwidth = 2, relief = "solid")
        self.entry_password.pack(pady = 15)

        Button(root = self, text='Copy', command = lambda x: pyperclip.copy(self.entry_password.get())).pack(pady = 15)
        Button(root = self, text='Back', command = lambda x: master.switch_frame(SelectMode)).pack(pady = 15)

    
    def generate_password(self, temp):
        try:
            length = int(self.entry_length.get())
            digits = int(self.entry_digits.get())
            special = int(self.entry_special.get())
        except:
            tkMessageBox.showwarning('Warning', 'All inputs must be valid integers')
            return

        if length < 0 or digits < 0 or special < 0:
            tkMessageBox.showwarning('Warning', "Inputs can't be negative")
            return

        if length < digits + special:
            tkMessageBox.showwarning('Warning', "Number of digits and number of special characters must be less than or equal to the length")
            return

        if length < 6:
            tkMessageBox.showwarning('Warning', "Length must be greater than or equal 6")
            return

        password = passwordFullyRandom(length, digits, special)

        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(tk.END, password)

        

if __name__ == '__main__':
    window = Main()
    window.mainloop()