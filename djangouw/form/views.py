from django.shortcuts import render, redirect
from .models import Poengliste

# Create your views here.

def forside(request):
  return render(request, 'forside.html')

def quiz(request):
  context = {
    'spmliste': [
      {
        'spm': "Hva er en CPU?",
        'alternativer': [
          "Central Processing Unit",
          "Core Primary Unicode",
          "Hovedprosessor"
        ],
        'fasit': 1
      },
      {
        'spm': "Hva er hovedkortet?",
        'alternativer': [
          "Kretskort som binder sammen komponentene i datamaskinen",
          "Bruksanvisningen til datamaskinen"
        ],
        'fasit': 1
      },
      {
        'spm': "Hvorfor brukes totallsystemet i forbindelse med datamaskiner?",
        'alternativer': [
          "Datamaskinen kan bare telle til 2",
          "Datamaskinen baserer seg på to tilstander: strøm på og strøm av, i ledningene som går mellom komponentene",
          "Inne i datamaskinen brukes to tall: 0 og 1"
        ],
        'fasit': 2
      }
    ]
  }
  return render(request, 'quiz.html',context)


def lagrepoeng(request):
  navn = request.POST["navn"]
  if navn == "":
    navn = "Anonym"
  poeng = request.POST["poeng"]
  if poeng == "":
    poeng = 0
  ny_linje = Poengliste(navn=navn, poeng=poeng)
  try:
    ny_linje.save()
    return redirect('resultater')
  except:
    return render(request, 'feilmelding.html')



def resultater(request):
  resultatliste = Poengliste.objects.all().values()
  context = {
    'resultatliste': resultatliste,
  }
  return render(request, 'resultater.html',context)


def feilmelding(request):
  return render(request, 'feilmelding.html')


def adminside(request):
  resultatliste = Poengliste.objects.all().values()
  context = {
    'resultatliste': resultatliste,
  }
  return render(request, 'adminside.html',context)

def slettlinje(request):
  slettID = int(request.POST["slettID"])
  slett_info = Poengliste.objects.get(id=slettID)
  try:
    slett_info.delete()
    return redirect('adminside')
  except:
    return render(request, 'feilmelding.html')

def oppdater(request, id):
  oppdaterlinje = Poengliste.objects.get(id=id)
  context = {
    'oppdaterlinje': oppdaterlinje,
  }
  return render(request, 'oppdater.html',context)

def lagreoppdatering(request):
  oppdaterID = int(request.POST["oppdaterID"])
  navn = request.POST["navn"]
  poeng = request.POST["poeng"]
  oppdater_info = Poengliste.objects.get(id=oppdaterID)
  oppdater_info.navn = navn
  oppdater_info.poeng = poeng
  try:
    oppdater_info.save()
    return redirect('adminside')
  except:
    return render(request, 'feilmelding.html')

  