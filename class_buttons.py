import tkinter as tk

class ImageButton(tk.Label):
	def __init__(self, root, image_paths, *args, **kwargs):
		self.normal_image = tk.PhotoImage(file = image_paths[0])
		self.hovered_image = tk.PhotoImage(file = image_paths[1])
		self.pressed_image = tk.PhotoImage(file = image_paths[2])
		self.command = kwargs.pop('command', None)
		disabled = kwargs.pop('state', None) == tk.DISABLED

		super().__init__(master = root, image=self.normal_image, font=kwargs.pop('font', ('Arial', 18, 'bold')), bg=kwargs.pop('bg', '#333333'), compound=kwargs.pop('compound', 'center'), *args, **kwargs)
		self.disabled = disabled

	@property
	def disabled(self):
		return self['state'] == tk.DISABLED

	@disabled.setter
	def disabled(self, value):
		self['state'] = tk.DISABLED if value else tk.NORMAL
		self['cursor'] = 'X_cursor' if value else 'hand1'
		self.bind('<Button-1>',
			lambda _: self.config(image = self.pressed_image) if not value else lambda _: None
		)
		self.bind('<ButtonRelease-1>',
			self.on_release if not value else lambda _: None
		)
		self.bind('<Enter>',
			lambda _: self.config(image = self.hovered_image) if not value else lambda _: None
		)
		self.bind('<Leave>',
			lambda _: self.config(image = self.normal_image) if not value else lambda _: None
		)

	def on_release(self, arg):
		self.config(image = self.normal_image)
		if self.command:
			self.command(self)


class Button(ImageButton):
	def __init__(self, root = None, text = '', command = None, *args, **kwargs):
		super().__init__(root = root, image_paths = ('images/normal_button.png', 'images/hovered_button.png', 'images/pressed_button.png'), text = text, command = command, *args, **kwargs)

