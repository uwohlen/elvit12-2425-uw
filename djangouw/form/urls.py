from django.urls import path
from . import views

urlpatterns = [
  path('', views.forside, name='forside'),
  path('quiz', views.quiz, name='quiz'),
  path('lagrepoeng', views.lagrepoeng, name='lagrepoeng'),
  path('resultater', views.resultater, name='resultater'),
  path('feilmelding', views.feilmelding, name='feilmelding'),
  path('adminside', views.adminside, name='adminside'),
  path('slettlinje', views.slettlinje, name='slettlinje'),
  path('oppdater/<int:id>', views.oppdater, name='oppdater'),
  path('lagreoppdatering', views.lagreoppdatering, name='lagreoppdatering'),
]