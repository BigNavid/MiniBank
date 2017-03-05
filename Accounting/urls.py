from django.conf.urls import url

from Accounting import views

urlpatterns = [
    url(r'^ShowCreditCard/', view=views.ShowCreditCard, name='ShowCreditCard'),
    url(r'^add_income_source/', view=views.add_income_source, name='HomePage'),
    url(r'^ShowCostsGraphical/', view=views.show_costs_graphical, name='ShowCosts'),
]
