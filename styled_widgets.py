from collections import defaultdict

from class_buttons import ImageButton
from class_entry import CustomEntry


def get_master_style_config(master):
	"""Attempt to load style_config from master"""
	while not hasattr(master, 'style_config') and hasattr(master, 'master'):
		master = master.master

	return defaultdict(lambda: None, getattr(master, 'style_config', {}))

class Button(ImageButton):
	"""Dynamically-styled ImageButton"""
	def __init__(self, master, *args, **kwargs):
		style_config = get_master_style_config(master)

		super().__init__(
			master,
			image_paths=['images/normal_button.png', 'images/hovered_button.png', 'images/pressed_button.png'],
			bg=kwargs.pop('bg', style_config['background']),
			fg=kwargs.pop('fg', style_config['button_foreground']),
			activeforeground=kwargs.pop('activeforeground', style_config['button_active_foreground']),
			color=kwargs.pop('color', style_config['button_color']),
			*args,
			**kwargs
		)

class Entry(CustomEntry):
	"""Dynamically-styled CustomEntry"""
	def __init__(self, master, *args, **kwargs):
		style_config = get_master_style_config(master)

		super().__init__(
			master,
			alt_fg=kwargs.pop('alt_fg', style_config['entry_alt_foreground']),
			fg=kwargs.pop('fg', style_config['entry_foreground']),
			bg=kwargs.pop('bg', style_config['entry_background']),
			*args,
			**kwargs
		)
