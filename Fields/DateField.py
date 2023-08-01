from . import *
from datetime import datetime
import pytz

class DateField(SingleAnswerField):
	def __init__(self, fieldData):
		super().__init__(fieldData)
		if not hasattr(self, 'fieldValue'):
			self.fieldValue = datetime.now().astimezone(
			pytz.timezone("Asia/Singapore"))
		self.modelOptions = { 'timezone': 'GMT+8' }

	def setFieldValue(self, value):
		self.fieldValue = datetime.strptime(value,"%d %b %Y")

	def getResponse(self):
		response = super().getResponse()
		if self.fieldValue is not None:
			response['answer'] = self.fieldValue.strftime("%d %b %Y")
		else:
			response['answer'] = ''
		return response
