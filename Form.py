import copy
from FormSG.Fields import FieldFactory
import json
import nacl.utils
from nacl.public import PrivateKey, Box, PublicKey
from nacl.encoding import Base64Encoder

ENCRYPT_VERSION = 1

class Form:
	def __init__(self, form):
		for k, v in form.__dict__.items():
			self.__dict__[k] = copy.deepcopy(v)
		actual_form_fields = []
		for fieldData in self.form_fields:
			actual_form_fields.append(FieldFactory.createFieldFromData(fieldData))
		self.form_fields = actual_form_fields

	def _getResponses(self):
		return [field.getResponse() for field in self.form_fields]

	def GetJSONResponse(self):
		return json.dumps(self._getResponses(),separators=(',', ':'))

	def _getEncryptedContent(self):
		if self.responseMode == 'encrypt':
			OurKey = PrivateKey.generate()
			nonce = nacl.utils.random(Box.NONCE_SIZE)
			public_key = PublicKey(Base64Encoder.decode(self.publicKey.encode('utf-8')))
			Ourbox = Box(OurKey, public_key)
			encrypted = Ourbox.encrypt(bytes(self.GetJSONResponse(),'utf-8'), nonce)
			return OurKey.public_key.encode(Base64Encoder).decode('utf8') + ";" + Base64Encoder.encode(nonce).decode('utf8') + ":" + Base64Encoder.encode(encrypted.ciphertext).decode('utf8')
		return ''

	def getSubmissionContent(self):
		submissionContent = {
	      'attachments': {},
	      'isPreview': False,
	      'responses': [],
	    }
		if self.responseMode == 'encrypt':
			submissionContent['encryptedContent'] = self._getEncryptedContent()
			submissionContent['version'] = ENCRYPT_VERSION
		return submissionContent
