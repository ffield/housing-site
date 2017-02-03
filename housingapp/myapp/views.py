 # myapp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Property, University, Review
from .forms import ReviewForm, LoginForm, RegisterForm, SortForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as session_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .helperClasses import UserButtons, googleAPI, stringIssues

# Create your views here.
def index(request):
	#do this with tuples later so less queries
	if request.method == 'POST':
		yes = request.POST.get('uni_tag')
		print(yes)
		return HttpResponseRedirect('/' + yes)
	else:
		university_list = University.objects.all()
	headerButtons = UserButtons(request)
	print(headerButtons.loginButtonText)
	context = {
		'university_list': university_list, 'request' : request, 'user_buttons':headerButtons
		}

	return render(request, 'index.html',context)

def college(request, universityTag):
	if request.method == 'POST':
		form = SortForm(request.POST)
        # check whether it's valid:
	    	if form.is_valid():
	    		sort_list = request.POST.getlist('sortBy')
	    		print(sort_list)
	    		return HttpResponseRedirect('/' + universityTag + '?sort=' + sort_list[0])
	college = University.objects.get(universityTag = universityTag)
	propertyRatingsDict = college.compilePropertyRatingsDict()
	landlordRatingsDict = college.compileLandlordRatingsDict()
	propertyTitlesDict = college.compilePropertyTitlesDict()
	propertyThumbnailsDict = college.compilePropertyThumbnailURLDict()
	page = request.GET.get('page')
	sort = request.GET.get('sort', '')
	print(sort)
	if sort != '':
		if sort == 'People':
			property_list = Property.objects.filter(propertyUniversity = college).order_by('propertyNumPersons')
		elif sort == 'Rooms':
			property_list = Property.objects.filter(propertyUniversity = college).order_by('propertyNumRooms')
		else:
			#implement price based sorting at some point
			property_list = Property.objects.filter(propertyUniversity = college).order_by('propertyNumPersons')
	else:
		property_list = Property.objects.filter(propertyUniversity = college)
	headerButtons = UserButtons(request)
	paginator = Paginator(property_list,15)
	try:
	    properties = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    properties = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    properties = paginator.page(paginator.num_pages)
	form = SortForm()
	context = {'form':form,'property_list': property_list,'university_tag' : universityTag,'ratings_dictionary' : propertyRatingsDict, 'titles_dictionary': propertyTitlesDict, 
	'landlord_ratings_dictionary' : landlordRatingsDict, 'thumbnail_dict':propertyThumbnailsDict, 'university':college,'properties':properties,'user_buttons':headerButtons}
	return render(request,'college.html',context)

def detail(request, universityTag, id):
	if request.method == 'POST':
		print("Gotta recognize")
	current_property = get_object_or_404(Property, pk=id)
	reviews = Review.objects.filter(reviewProperty = current_property)
	headerButtons = UserButtons(request)
	viewURL = googleAPI.generateURL(current_property.propertyAddress, 500, 400)
	propertyTitle = stringIssues.truncatePostComma(current_property.propertyAddress)
	context = {'property' : current_property, 'property_title':propertyTitle,
	'university_tag' : universityTag, 'imageURL' : viewURL, 'id' : id, 'reviews' : reviews, 'user_buttons':headerButtons}
	return render(request, 'property.html', context)


@login_required
def rate(request, universityTag, id):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = ReviewForm(request.POST)
        # check whether it's valid:
	    	if form.is_valid():
				currentProperty = Property.objects.get(id = id)
				propertyReviewTitle = form.cleaned_data['reviewTitle']
				propertyReview = form.cleaned_data['review']
				propertyRating = form.cleaned_data['propertyRating']
				landlordRating = form.cleaned_data['landlordRating']
				review = Review(reviewPropertyRating = propertyRating, reviewLandlordRating = landlordRating, 
					reviewDescription = propertyReview, reviewProperty = currentProperty, reviewTitle = propertyReviewTitle )
				review.save()
				return HttpResponseRedirect('/' + universityTag)

    # if a GET (or any other method) we'll create a blank form
	else:
		form = ReviewForm()
	headerButtons = UserButtons(request)
	current_property = get_object_or_404(Property, pk=id)
	return render(request, 'rate_property.html', {'form': form,'university_tag' : universityTag,'id' : id,'property'
		: current_property,'user_buttons':headerButtons})


	## AUTHENTICATION VIEWS


def login(request):
	# if this is a POST request we need to process the form data
	unext = request.GET.get('next', '/')
	#any unext and contex stuff is me trying to handle the loging redirects
	#cant really figure this out so I'm gonna get high and think on it
	print(unext)
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = LoginForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			if user is not None:
				user_login(request, user)
				print("Even got past login")
				if unext != None:
					print("unext")
					return HttpResponseRedirect(unext)
				else:
					print("index lol")
					return HttpResponseRedirect('/')
			else:
				return render(request, 'login.html', {'form': form})
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form, 'next' : unext})




def register(request):
		# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = RegisterForm(request.POST)
        # check whether it's valid:
	    	if form.is_valid():
				username = form.cleaned_data['username']
				email = username
				password = form.cleaned_data['password']
				user = User.objects.create_user(username, email, password)
				return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = RegisterForm()

	return render(request, 'register.html', {'form': form})


def logout(request):
	session_logout(request)
	return HttpResponseRedirect('/')

		
