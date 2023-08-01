from .Field import Field

class AnswerField(Field):
	def __init__(self, fieldData):
		super().__init__(fieldData)

	def getResponse(self):
		return {
			"_id": self._id,
			"fieldType": self.fieldType,
      		"question": self.title,
		}
