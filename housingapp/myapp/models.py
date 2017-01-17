from django.db import models


class University(models.Model):
    universityTag = models.CharField(max_length=100)
    universityName = models.CharField(max_length = 100)
    universityTown = models.CharField(max_length = 100)
    def __str__(self):
        return self.universityName

    #Not the best implementation but we eatin, but also it might be fine?     
    def compilePropertyRatingsDict(self):
    	allProperties = Property.objects.filter(propertyUniversity = self)
    	ratingDict = {}
    	for p in allProperties:
    		ratingList = p.compileRatings()
    		ratingDict[p.id] = ratingList[0]
    	return ratingDict

    def compileLandlordRatingsDict(self):
    	allProperties = Property.objects.filter(propertyUniversity = self)
    	ratingDict = {}
    	for p in allProperties:
    		ratingList = p.compileRatings()
    		ratingDict[p.id] = ratingList[1]
    	return ratingDict



class Property(models.Model):
    propertyUniversity = models.ForeignKey(University)
    propertyAddress = models.CharField(max_length=200)
    propertyDescription = models.CharField(max_length=250)
    propertyNumRooms = models.IntegerField(default = 0)
    propertyNumBaths = models.IntegerField(default = 0)
    propertyNumPersons = models.IntegerField(default = 0)
    propertyAC = models.BooleanField(default = False)
    propertyHeat = models.BooleanField(default = False)
    propertyPorch = models.BooleanField(default = False)
    propertyBackyard = models.BooleanField(default = False)
    propertyWasherDryer = models.BooleanField(default = False)
    propertyRating = models.FloatField(default = 0.0)
    landlordRating = models.FloatField(default = 0.0)


    def __str__(self):
        return self.propertyAddress

    def compileRatings(self):
		pertinentReviews = Review.objects.filter(reviewProperty = self)
		propRating = 0.0
		llRating = 0.0
		count = 0
		for r in pertinentReviews:
			propRating = propRating + r.reviewPropertyRating
			llRating = llRating + r.reviewLandlordRating
			count = count + 1
		if count != 0:
			ratingList = []
			propRating = propRating / count
			llRating = llRating / count
			ratingList.append(propRating)
			ratingList.append(llRating)
			self.propertyRating = propRating
			self.landlordRating = llRating
			self.save()
		else:
			ratingList = []
			self.propertyRating = 0
			self.landlordRating = 0
			ratingList.append(0)
			ratingList.append(0)
			self.save()
		return ratingList
    

class Review(models.Model):
	reviewPropertyRating = models.IntegerField(default = 0)
	reviewLandlordRating = models.IntegerField(default = 0)
	reviewProperty = models.ForeignKey(Property)
	reviewDescription = models.CharField(default = "",max_length = 1000)
	reviewTitle = models.CharField(default = "", max_length = 50)
