from . import *
from .Form import Form
import requests
import json
from types import SimpleNamespace

class FormSGHelper:
	def __init__(self, form_id, *answers):
		self.answers = answers
		self.form_id = form_id
		self.form = None
		self.submissionId = None

	def getFormLayout(self):
		x = requests.get(f'{FormSG_BaseURL}/{self.form_id}/publicform')
		j = json.loads(x.content, object_hook=lambda d: SimpleNamespace(**d))
		self.form = Form(j.form)
		return True

	def IsAnswerEnough(self):
		return len(self.answers) == len(self.form.form_fields)

	def SetFieldValues(self):
		index = 0
		for field in self.form.form_fields:
			field.setFieldValue(self.answers[index])
			index = index + 1

	def getSubmissionId(self):
		return self.submissionId

	def Submit(self):
		json = self.form.getSubmissionContent()
		x = requests.post(f'{FormSG_BaseURL}/v2/submissions/encrypt/{self.form_id}?captchaResponse=null', json = json)
		if x.status_code == 200:
			self.submissionId = x.json()['submissionId']
		return x.status_code == 200
