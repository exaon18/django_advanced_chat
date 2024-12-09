from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method=="POST":
        room=request.POST['room']
        username=request.POST['username']
        return redirect("room", room=room,username=username)
    else:
        return render(request,"index.html")
def room(request, room,username):
    return render(request,"room.html",{
        "room":room,
        "username":username
    })

