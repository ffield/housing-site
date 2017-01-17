from django.contrib.auth import authenticate

class UserButtons:
	loginButtonText = ""
	loginButtonPath = ""
	logoutButtonText = ""
	logoutButtonPath = ""
	def __init__(self,request):
		if request.user.is_authenticated():
			self.loginButtonText = "Hello " + str(request.user)
			#make a meaningful path for this eventually
			self.loginButtonPath = '/'
			self.logoutButtonText = "Logout"
			self.logoutButtonPath = '/logout'
		else:
			self.loginButtonText = "Login"
			self.loginButtonPath = '/login'
			self.logoutButtonText = "Register"
			self.logoutButtonPath = '/register'


class StarAmount:
	numFullStars = 0
	numEmpyyStars = 0

	def __init__(self,rating):
		numFullStars = int(rating)
		numEmptyStars = 5 - numFullStars