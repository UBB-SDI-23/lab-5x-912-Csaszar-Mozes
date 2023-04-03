
from django.urls import path, include
from views.PersonListApiView import *
from views.PersonDetailApiView import *
from views.LocationListApiView import *
from views.LocationDetailApiVew import *
from views.CompanyListApiView import *
from views.CompanyDetailApiView import *
from views.CompanyFilterApiView import *
from views.PersonCompanyListApiView import *
from views.PersonCompanyDetailApiView import *
from views.CompanyByAvgSalaryApiView import *
from views.CompanyNrLoacationsApiView import *



urlpatterns = [
    path('people/', PersonListApiView.as_view(), name="people_list"),
    path('people/<int:person_id>/', PersonDetailApiView.as_view(), name="people_detail"),
    path('locations/', LocationListApiView.as_view(), name="locations_list"),
    path('locations/<int:loc_id>/', LocationDetailApiView.as_view(), name="locations_detail"),
    path('companies/', CompanyListApiView.as_view(), name="companies_list"),
    path('companies/<int:comp_id>/', CompanyDetailApiView.as_view(), name="companies_detail"),
    path('companies/reputation-greater-than/<int:reputation>/', CompanyFilterApiView.as_view(), name="companies_reputation_gt"),
    path('pc/', PersonCompanyListApiView.as_view(), name="pc_list"),
    path('pc/<int:pc_id>/', PersonCompanyDetailApiView.as_view(), name="pc_detail"),
    path('companies/avg-salary/', CompanyByAvgSalaryApiView.as_view(), name="companies_avg_salary"),
    path('companies/nr-locations/', CompanyNrLocationsApiView.as_view(), name="companies_nr_locations")
]