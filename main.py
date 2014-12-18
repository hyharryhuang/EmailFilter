def filterEmails(emailList, name):
	nameParts = name.split(' ')

	def filterFunc(x): 
		for part in nameParts:
			if part.lower() in x.lower():
				return True

		return False

	return filter(filterFunc, emailList)