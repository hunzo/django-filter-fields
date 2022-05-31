from django.shortcuts import redirect, render
from .forms import BlogForm
from .models import Blog, Entry
from django import forms
# Create your views here.


def BlogView(request):

    # post = Blog.objects.all()
    post = Blog.objects.filter(entry__author=request.user)

    if request.method == "POST":
        form = BlogForm(request.POST)
        # print(form.fields)

        if form.is_valid():
            form.save()
            return redirect("Home")

    myForm = BlogForm()
    # myForm.fields["entry"] = forms.ModelChoiceField(User.objects.filter(username=request.user))
    myForm.fields["entry"] = forms.ModelChoiceField(
        Entry.objects.filter(author=request.user))

    print(myForm.fields["entry"])

    context = {

        "title": "Blog",
        "form": myForm,
        "post": post,
    }
    return render(request, "index.html", context)
