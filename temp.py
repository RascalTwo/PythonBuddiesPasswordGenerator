import tkinter as tk

wn = tk.Tk()
wn.geometry("500x500")
wn.config(bg = "#333333")
photo = tk.PhotoImage(file = "images/normal_button.png")
hov = tk.PhotoImage(file = "images/hovered_button.png")

but = tk.Button(wn, text = "Text", image=photo, bg = "#ff0000", fg = "#ffffff", command = lambda: print("one"), borderwidth=0, relief=tk.SUNKEN, highlightthickness = 0, bd = 0, background=wn['background'], activebackground=wn['background'])
but.pack()
two = tk.Button(wn, text = "Other", image=photo, bg = "#ff0000", fg = "#ffffff", command = lambda: print("two"), borderwidth=0, relief=tk.SUNKEN, highlightthickness = 0, bd = 0, background=wn['background'], activebackground=wn['background'], font=('Arial', 18, 'bold'), compound='center')
two.pack()

but.bind('<Enter>',
    lambda _: but.configure(image=hov)
)
but.bind('<Leave>',
    lambda _: but.configure(image=photo)
)
but.bind('<FocusIn>',
    lambda _: but.configure(image=hov)
)
but.bind('<FocusOut>',
    lambda _: but.configure(image=photo)
)
two.bind('<Enter>',
    lambda _: two.configure(image=hov)
)
two.bind('<Leave>',
    lambda _: two.configure(image=photo)
)
two.bind('<FocusIn>',
    lambda _: two.configure(image=hov)
)
two.bind('<FocusOut>',
    lambda _: two.configure(image=photo)
)

wn.mainloop()