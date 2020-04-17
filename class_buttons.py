"""Custom image-based buttons with animations"""

import tkinter as tk

# To avoid creating a new image for each state, this opt-out cache is available.
IMAGE_CACHE = {}

def load_images(normal=None, hover=None, pressed=None, cache=True):
	"""Return images - either from cache or from filepaths"""
	return (
		[IMAGE_CACHE.setdefault(filepath, tk.PhotoImage(file=filepath)) for filepath in (normal, hover, pressed)]
		if cache else
		[tk.PhotoImage(file=filepath) for filepath in (normal, hover, pressed)]
	)


class ImageButton(tk.Button):
	"""Button with image-based animations"""
	def __init__(self, *args, image_paths=None, disable_cache=False, cursors=['hand1', 'X_cursor'], **kwargs):
		image_paths = image_paths or []

		normal, hover, pressed = load_images(*image_paths, cache=not disable_cache)
		self.image_events = {
			normal: ('<ButtonRelease-1>', '<Leave>', '<FocusOut>'),
			hover: ('<Enter>', '<FocusIn>'),
			pressed: ('<Button-1>', )
		}

		self.cursors = cursors

		disabled = kwargs.pop('state', None) == tk.DISABLED
		bg = kwargs.pop('bg', "#333333")

		super().__init__(
			image=list(self.image_events.keys())[0],
			font=kwargs.pop('font', ('Arial', 18, 'bold')),
			bg=bg,
			activebackground=bg,
			compound=kwargs.pop('compound', 'center'),
			borderwidth=0,
			highlightthickness=0,
			*args,
			**kwargs
		)
		self.disabled = disabled
		self.bind('<Return>', lambda _: self.invoke())

	@property
	def disabled(self):
		"""Return disabled state of button"""
		return self['state'] == tk.DISABLED

	@disabled.setter
	def disabled(self, disabled):
		"""Set disabled state"""
		self['state'] = tk.DISABLED if disabled else tk.NORMAL
		self['cursor'] = self.cursors[int(disabled)]

		if disabled:
			for events in self.image_events.values():
				for event in events:
					self.unbind(event)
			return

		for image, events in ((image, events) for image, events in self.image_events.items() if image):
			for event in events:
				self.bind(event, lambda _, image=image: self.config(image=image))


class Button(ImageButton):
	"""Pre-styled image button"""
	def __init__(self, *args, **kwargs):
		super().__init__(image_paths=['images/normal_button.png', 'images/hovered_button.png', 'images/pressed_button.png'], *args, **kwargs)
