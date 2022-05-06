from django.shortcuts import render

# Create your views here.

class Finch: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
  Finch('Smelly', 'flabby', 'foul little demon', 13),
  Finch('Sencha', 'yellow mix', 'diluted tortoise shell', 10),
  Finch('Sugar', 'mixed', '3 legged finch', 14)
]

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Finche Page</h1>')
def about(request):
    return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })

# Note that parens are optional if not inheriting from another class