


django app on which user can search for restaurants, can see menu, place order.

#views
from .serializers import RestaurantMenuSerializer

def show_restaurants():
	data = Restaurants.objects.all()[:10]
	response = {'restaurants': []}
	for entry in data:
		response['restaurants'].append({'id': 1, 'name': entry.name, 'address': 'entry.short_address'})
	return render(response, 'home.html')

def get_menu(res_id):
	menu = RestaurantMenu.objects.filter(res_id = res_id)
	serialized_menu = RestaurantMenuSerializer(menu) 				# passing model object in serializer class instance -- it returns serializer object
	return JsonResponse(serialized_menu.data)



# models

class Restaurants(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=40)

class RestaurantMenu(models.Model):
	res = models.ForeignKey(Restaurants)
	item_name = models.CharField(max_length=20)
	item_cost = models.FloatField(max_length=20)



serializers --
from rest_framework import serializers
from .models import RestaurantMenu

class RestaurantMenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = RestaurantMenu
		fileds = '__all__'


the painful thing here is i need to get something from model - it comes in model object.
for returning i need to make it into python dict and then pass it to jsonresponse/htmlresponse.
model obj - what i want to return - cant it be done by django. serializer can help.
pass model objects to serializer and then return it.

pass the object to serializer . how the serializer knows about the mapping between the attributes of obect and its own attributes.
need to define 1 serializer for every object type.
but serializer and model looks same - modelserializer - define just model and mention the fields in serializer which we need to use.
