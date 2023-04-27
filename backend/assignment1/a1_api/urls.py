from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .api_views.CompanyNameAutoView import CompanyNameAutoView
from .api_views.PeopleView import PeopleView
from .api_views.PeopleIDView import PeopleIDView
from .api_views.LocationsView import LocationsView
from .api_views.LocationsIDView import LocationsIDView
from .api_views.CompaniesView import CompaniesView
from .api_views.CompaniesIDView import CompaniesIDView
from .api_views.PersonCompanyView import PersonCompanyView
from .api_views.PersonCompanyIDView import PersonCompanyIDView
from .api_views.CompanyByAvgSalaryView import CompanyByAvgSalaryView
from .api_views.CompanyByNrLocationsView import CompanyByNrLocationsView
from .api_views.CompanyReputationGTView import CompanyReputationGTView
from .api_views.PeopleIDCompaniesView import PeopleIDCompaniesView
from .api_views.PeopleIDCompaniesIDView import PeopleIDCompaniesIDView
from .api_views.CompaniesIDPeopleView import CompaniesIDPeopleView
from .api_views.CompaniesIDPeopleIDView import CompaniesIDPeopleIDView
from .api_views.PersonNameAutoView import PersonNameAutoView
from .api_views.NrTotalPages import NrTotalPages
from .api_views.UserProfileIDView import UserProfileIDView
from .api_views.RegisterView import RegisterView


urlpatterns = [
    path('api/people/', PeopleView.as_view(), name="people_list"),
    path('api/people/<int:id>/', PeopleIDView.as_view(), name="people_detail"),
    path('api/people/<int:person_id>/companies/', PeopleIDCompaniesView.as_view(), name="peopleidcompanies"),
    path('api/people/<int:person_id>/companies/<int:comp_id>/', PeopleIDCompaniesIDView.as_view(), name="peopleidcompaniesid"),
    path('api/people/name-autocomplete/', PersonNameAutoView.as_view(), name="people_name_autocomplete"),
    path('api/locations/', LocationsView.as_view(), name="locations_list"),
    path('api/locations/<int:id>/', LocationsIDView.as_view(), name="locations_detail"),
    path('api/companies/', CompaniesView.as_view(), name="companies_list"),
    path('api/companies/<int:id>/', CompaniesIDView.as_view(), name="companies_detail"),
    path('api/companies/<int:comp_id>/people/', CompaniesIDPeopleView.as_view(), name="companiesidpeople"),
    path('api/companies/<int:comp_id>/people/<int:person_id>/', CompaniesIDPeopleIDView.as_view(), name="companiesidpeopleid"),
    path('api/companies/reputation-greater-than/', CompanyReputationGTView.as_view(), name="companies_reputation_gt"),
    path('api/companies/name-autocomplete/', CompanyNameAutoView.as_view(), name="companies_name_autocomplete"),
    path('api/pc/', PersonCompanyView.as_view(), name="pc_list"),
    path('api/pc/<int:id>/', PersonCompanyIDView.as_view(), name="pc_detail"),
    path('api/companies/by-avg-salary/', CompanyByAvgSalaryView.as_view(), name="companies_avg_salary"),
    path('api/companies/by-nr-locations/', CompanyByNrLocationsView.as_view(), name="companies_nr_locations"),
    path('api/users/<int:id>/', UserProfileIDView.as_view(), name="user_by_id"),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/nr-total-pages/', NrTotalPages.as_view(), name="nr_total_pages"),
    path('api/swagger-plain/', get_schema_view(title='Swagger documentation',description='Guide for the REST API'), name='swagger_plain'),
    path('api/swagger-html/', TemplateView.as_view(template_name='swagger.html',extra_context={'schema_url':'swagger_plain'}), name='swagger_html'),
]
