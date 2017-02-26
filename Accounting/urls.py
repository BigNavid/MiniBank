from django.conf.urls import url

from Accounting import views

urlpatterns = [
    url(r'^ShowCreditCard/', view=views.ShowCreditCard, name='ShowCreditCard'),

]
