from . import *

class RadioField(SingleAnswerField):
	def __init__(self, fieldData):
		super().__init__(fieldData)

	def setFieldValue(self, value):
		if value in self.fieldOptions:
			super().setFieldValue(value)
			
