import copy

class Field:
	def __init__(self, fieldData):
		self.required = True
		self.disabled = False
		for k, v in fieldData.__dict__.items():
			self.__dict__[k] = copy.deepcopy(v)

	def lock(self):
		self.disabled = True
