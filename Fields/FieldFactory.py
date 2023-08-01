from .TextField import TextField
from .DateField import DateField
from .RadioField import RadioField
from .DecimalField import DecimalField
from .SingleAnswerField import SingleAnswerField

def createFieldFromData(fieldData):
	if fieldData.fieldType == "date":
		return DateField(fieldData)
	elif fieldData.fieldType == "decimal":
		return DecimalField(fieldData)
	elif fieldData.fieldType == "radiobutton":
		return RadioField(fieldData)
	elif fieldData.fieldType == "textfield":
		return TextField(fieldData)
	elif fieldData.fieldType == "yes_no":
		return SingleAnswerField(fieldData)
	return None
