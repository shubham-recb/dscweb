from django.shortcuts import render, get_object_or_404
from .forms import MemberForm
from .models import Member

def home_view(request):
    members = Member.objects.all()
    context = {"title": "DSC", "members": members}
    return render(request, 'home.html', context)

def about_view(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)

def register_view(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        obj = Member(username=data['username'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    mobile=data['mobile'],
                    email=data['email'],
                    password=data['password'])
        obj.save()
        form = MemberForm()
    context = {"form": form, "title":"Register"}
    return render(request, 'register-form.html', context)

def member_detailView(request, first_name):
    member = get_object_or_404(Member, first_name=first_name)
    context = {"member": member}
    return render(request, 'member-view.html', context)


