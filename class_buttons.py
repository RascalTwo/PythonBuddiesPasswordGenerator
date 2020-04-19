"""Custom image-based buttons with animations"""

import tkinter as tk
import colorsys

# To avoid creating a new image for each state, this opt-out cache is available.
IMAGE_CACHE = {}


def get_cache_name(filepath, desired, master):
	return filepath + '_' + str(id(master)) + '_' + str(desired)

def load_images(desired, normal=None, hover=None, pressed=None, cache=True, master=None):
	"""Return images - either from cache or from filepaths

	The type of desired determines how to set the image colors:
		int: Hue
		sequence: RGBA
	"""
	filepaths = normal, hover, pressed

	try:
		from PIL import ImageTk, Image
		if desired is None:
			raise Exception()
	except (ModuleNotFoundError, Exception) as exception:
		if isinstance(exception, ModuleNotFoundError):
			print('Unable to use custom image colors as "Pillow" has not been installed')

		return (
			[IMAGE_CACHE.setdefault(get_cache_name(filepath, desired, master), tk.PhotoImage(file=filepath, master=master)) for filepath in filepaths]
			if cache else
			[tk.PhotoImage(file=filepath, master=master) for filepath in filepaths]
		)

	# Attempt to use cache
	cache_names = [get_cache_name(filepath, desired, master) for filepath in filepaths]
	if all(cache_name in IMAGE_CACHE for cache_name in cache_names):
		return [IMAGE_CACHE[cache_name] for cache_name in cache_names]

	is_hue = isinstance(desired, int)

	adjusted = []
	for image in (Image.open(filepath).convert('RGBA') for filepath in filepaths):
		if is_hue:
			# Extract alpha channel, convert to HSV, set H to hue, convert to RGB, merge alpha channel back in
			alpha = image.getchannel('A')
			image = image.convert('HSV')

			pixels = image.load()
			for i in range(image.size[0]):
				for j in range(image.size[1]):
					# Only change hue
					pixels[i,j] = (desired, *pixels[i,j][1:])

			rgb = image.convert('RGB').split()
			image = Image.merge('RGBA', (*rgb, alpha))

		else:
			# Get RGB difference between center pixel and desired color, only factoring in Hue,
			# then modify all pixels by that difference.
			pixels = image.load()
			center = pixels[tuple(cord // 2 for cord in image.size)]
			print(center)

			# Get H from desired and SL from center
			_, saturation, lightness = colorsys.rgb_to_hsv(center[0], center[1], center[2])
			hue, _, __ = colorsys.rgb_to_hsv(desired[0], desired[1], desired[2])

			# Convert HSV floats to ints, calculate diff between colors
			rgb = map(int, colorsys.hsv_to_rgb(hue, saturation, lightness))
			changes = tuple(offset - center[i] for i, offset in enumerate((*rgb, desired[3])))

			for i in range(image.size[0]):
				for j in range(image.size[1]):
					pixels[i,j] = tuple(pixels[i,j][k] + changes[k] for k in range(4))

		adjusted.append(image)

	# Add to cache
	photo_images = [ImageTk.PhotoImage(image, master=master) for image in adjusted]
	for i in range(len(filepaths)):
		IMAGE_CACHE[cache_names[i]] = photo_images[i]
	return photo_images


class ImageButton(tk.Button):
	"""Button with image-based animations"""

	_focus_losing = ('<ButtonRelease-1>', '<Leave>', '<FocusOut>')

	def __init__(self, *args, image_paths=None, disable_cache=False, cursors=['hand1', 'X_cursor'], color=None, **kwargs):
		image_paths = image_paths or []

		normal, hover, pressed = load_images(image_paths, color, not disable_cache, kwargs.get('master', args[0]))
		self.image_events = {
			normal: self._focus_losing,
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
			activeforeground=kwargs.pop('activeforeground', kwargs.get('fg', bg)),
			compound=kwargs.pop('compound', 'center'),
			borderwidth=0,
			highlightthickness=0,
			*args,
			**kwargs
		)
		self.disabled = disabled
		self.bind('<Return>', lambda _: self.invoke())
		self.bind('<KP_Enter>', lambda _: self.invoke())

	def _handle_event(self, event, image):
		"""Handle event, properly handling mutiple interactions while focused"""
		if self.focus_get() == self and event in self._focus_losing:
			return
		self.configure(image=image)

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
				self.bind(event, lambda _, event=event, image=image: self._handle_event(event, image))
