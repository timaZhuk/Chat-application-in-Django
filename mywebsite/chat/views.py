from django.shortcuts import render

# ------------Create view----------
def lobby(request):
    return render(request, 'chat/lobby.html')
