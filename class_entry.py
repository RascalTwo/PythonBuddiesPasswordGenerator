import tkinter as tk

class Entry(tk.Entry):
	def __init__(self, root = None, *args, **kwargs):
		self.alt_text = kwargs.pop('alt_text', None)
		self.fg = kwargs.pop('fg', '#505050')
		self.active_fg = kwargs.pop('active_fg', '#181818')
		self.bg = kwargs.pop('bg', '#a8a8a8')

		super().__init__(master = root, font=kwargs.pop('font', ('Arial', 18, 'bold')), bg=self.bg, fg=self.fg, borderwidth=kwargs.pop('borderwidth', 2), relief=kwargs.pop('relief', 'solid'))
		
		self.bind('<FocusIn>', self.on_focus)
		self.bind('<FocusOut>', self.on_defocus)

		if self.alt_text:
			self.insert(tk.END, self.alt_text)

	def on_focus(self, _):
		if self.alt_text and self.get().strip() != self.alt_text and self.cget('fg') != self.fg:
			return

		self.config(fg = self.active_fg)
		self.delete(0, tk.END)

	def on_defocus(self, _):
		if not self.alt_text or self.get().strip():
			return

		self.delete(0, tk.END)
		self.config(fg = self.fg)
		self.insert(tk.END, self.alt_text)