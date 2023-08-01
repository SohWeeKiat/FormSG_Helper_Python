from .AnswerField import AnswerField

class SingleAnswerField(AnswerField):
	def __init__(self, fieldData):
		super().__init__(fieldData)
		if not hasattr(self, 'fieldValue'):
			self.fieldValue = ''

	def setFieldValue(self, value):
		self.fieldValue = value

	def getResponse(self):
		response = super().getResponse()
		if self.fieldValue == '':
			response['answer'] = ''
		else:
			response['answer'] = str(self.fieldValue)
		return response
