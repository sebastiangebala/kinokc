from django.shortcuts import render

def start(request):
    return render(request, 'kinokc/start.html', {'start': start})
def repertuar(request):
    return render(request, 'kinokc/repertuar.html', {'repertuar': repertuar})
def bilety(request):
    return render(request, 'kinokc/bilety.html', {'bilety': bilety})
def rezerwacje(request):
    return render(request, 'kinokc/rezerwacje.html', {'rezerwacje': rezerwacje})
def partnerzy(request):
    return render(request, 'kinokc/partnerzy.html', {'partnerzy': partnerzy})
def kontakt(request):
    return render(request, 'kinokc/kontakt.html', {'kontakt': kontakt})

