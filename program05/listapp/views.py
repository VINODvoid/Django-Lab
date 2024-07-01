from django.shortcuts import render

# Create your views here.
def list_func(req):
    students = ['Somu','Supe','God']
    fruits = ['apple','mango','grapes','orange']
    return render (req,'index.html',{"students":students,'fruits':fruits})
