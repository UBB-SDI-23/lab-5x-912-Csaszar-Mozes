
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

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







urlpatterns = [
    re_path('api/people/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))', PeopleView.as_view(), name="people_list"),
    path('api/people/<int:id>/', PeopleIDView.as_view(), name="people_detail"),
    path('api/people/<int:person_id>/companies/', PeopleIDCompaniesView.as_view(), name="peopleidcompanies"),
    path('api/people/<int:person_id>/companies/<int:comp_id>/', PeopleIDCompaniesIDView.as_view(), name="peopleidcompaniesid"),
    re_path('api/locations/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))', LocationsView.as_view(), name="locations_list"),
    path('api/locations/<int:id>/', LocationsIDView.as_view(), name="locations_detail"),
    re_path('api/companies/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))', CompaniesView.as_view(), name="companies_list"),
    path('api/companies/<int:id>/', CompaniesIDView.as_view(), name="companies_detail"),
    path('api/companies/<int:comp_id>/people/', CompaniesIDPeopleView.as_view(), name="companiesidpeople"),
    path('api/companies/<int:comp_id>/people/<int:person_id>/', CompaniesIDPeopleIDView.as_view(), name="companiesidpeopleid"),
    re_path('api/companies/reputation-greater-than/<int:reputation>/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))',
            CompanyReputationGTView.as_view(), name="companies_reputation_gt"),
    re_path('api/pc/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))', PersonCompanyView.as_view(), name="pc_list"),
    path('api/pc/<int:id>/', PersonCompanyIDView.as_view(), name="pc_detail"),
    re_path('api/companies/avg-salary/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))',
            CompanyByAvgSalaryView.as_view(), name="companies_avg_salary"),
    re_path('api/companies/nr-locations/(?:page-(?P<page_nr>\d+)),(?:size-(?P<page_size>\d+))',
            CompanyByNrLocationsView.as_view(), name="companies_nr_locations"),
    path('api/swagger-plain/', get_schema_view(title='Swagger documentation',description='Guide for the REST API'), name='swagger_plain'),
    path('api/swagger-html/', TemplateView.as_view(template_name='swagger.html',extra_context={'schema_url':'swagger_plain'}), name='swagger_html'),
]
