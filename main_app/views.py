from django.shortcuts import render
from .models import Cat
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),c
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    # render take first request from the functions delcation
    # next it take the template to render similar to ejs res.render
    return render(request, 'about.html')

def cat_index(request):
    # Get back all the cats from the database using our model
    cats = Cat.objects.all()
    # Send back those cats with a cats_index page
    return render(request, 'cats/index.html', {'cats': cats})

# CBV Class based Views

'''
    ListView - List stuff
    CreateView - Create stuff
    DeleteView - Delete stuff
    UpdateView - Update Stuff
    DetailView - Show Page

'''


# Listing
class CatList(ListView):
    model = Cat
    # By default Listview will look for a template in the path
    # templates/<your_app_name>/<modelname>_list.html
    # aka we made a tempalates/main_app/cat_list.html

    #or we override that default by providing a new path
    template_name = 'cats/index.html'

class CatCreate(CreateView):
    model = Cat
    # Lets createview know which fieds to use
    # fields = '__all__' 
    #or a list
    fields = ['name', 'breed', 'description', 'age']
    success_url='/cats/'
