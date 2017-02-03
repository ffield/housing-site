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


class googleAPI:
    @staticmethod
    def generateURL(address,width,height):
        initialURL = "https://maps.googleapis.com/maps/api/streetview?"
        key = "AIzaSyC3lmdEJprjiAlDc_xixs0DNvndamMjRYw"
        address.replace(" ",'+')
        initialURL = initialURL + 'location=' + address + '&'
        sizeString = str(width) + 'x' + str(height)
        initialURL = initialURL + 'size=' + sizeString + '&'
        initialURL = initialURL + 'key=' + key
        return initialURL


class stringIssues:
    @staticmethod
    def truncatePostComma(address):
        for char in range(len(address)):
            if address[char] == ',':
                finalWord = address[:char]
                return finalWord
        return address

