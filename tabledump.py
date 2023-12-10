from dataclasses import dataclass, field
# from typing import 

TAB = '\t'

@datacclass
class TableBuilder:

	headtext: str = ''
	tailtext: str = ''
	content: str = ''
	page_wide: bool = False
	centering: bool = True
	rowcolor_swap: bool = False


	# def __post_init__(self): pass

	def add_head(self): pass

	def output(self): pass


	