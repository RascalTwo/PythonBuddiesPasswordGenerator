"""Custom entry fields capable of containing placeholder text"""

import tkinter as tk

class Entry(tk.Entry):
	"""Custom entry field with placeholder text"""
	def __init__(self, *args, alt_text=None, alt_fg='#505050', fg='#181818', bg='#a8a8a8', font=('Arial', 18, 'bold'), borderwidth=2, relief=tk.SOLID, **kwargs):
		self.alt_text = alt_text
		self.alt_fg = alt_fg
		self._fg = fg

		super().__init__(
			bg=bg,
			fg=self.alt_fg if self.alt_text else self._fg,
			font=font,
			borderwidth=borderwidth,
			relief=relief,
			*args,
			**kwargs
		)


		if self.alt_text:
			self.insert(tk.END, self.alt_text)
			self.bind('<FocusIn>', self.on_focus_in)
			self.bind('<FocusOut>', self.on_focus_out)

		self.has_user_content = False

	def on_focus_in(self, _):
		"""Remove placeholder text if exists"""
		# If text equals alt text, and there is no user content, delete alt text
		if self.get().strip() != self.alt_text or self.has_user_content:
			return

		self.configure(fg=self._fg)
		self.delete(0, tk.END)
		self.has_user_content = True


	def on_focus_out(self, _):
		"""Add placeholder text if no user content"""
		# If no text exists, and there is user content, insert alt text
		if self.get().strip() or not self.has_user_content:
			return

		self.delete(0, tk.END)
		self.configure(fg=self.alt_fg)
		self.insert(tk.END, self.alt_text)
		self.has_user_content = False
