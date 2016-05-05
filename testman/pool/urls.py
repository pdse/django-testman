from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from pool import views

urlpatterns = [
	url(r'^domains/$', views.DomainList.as_view(), name='domain-list'),
	url(r'^domains/(?P<pk>[0-9]+)/$', views.DomainDetail.as_view(), name='domain-detail'),
	url(r'^domains/(?P<pk>[0-9]+)/systems/$', views.DomainSystemList.as_view(), name='domainsystem-list'),
	url(r'^systems/$', views.SystemList.as_view(), name='system-list'),
	url(r'^systems/(?P<pk>[0-9]+)/$', views.SystemDetail.as_view(), name='system-detail'),
	url(r'^systems/(?P<pk>[0-9]+)/functions/$', views.SystemFunctionList.as_view(), name='systemfunction-list'),
	url(r'^functions/$', views.FunctionList.as_view(), name='function-list'),
	url(r'^functions/(?P<pk>[0-9]+)/$', views.FunctionDetail.as_view(), name='function-detail'),
	url(r'^functions/(?P<pk>[0-9]+)/features/$', views.FunctionFeatureList.as_view(), name='functionfeature-list'),
	url(r'^features/$', views.FeatureList.as_view(), name='feature-list'),
	url(r'^features/(?P<pk>[0-9]+)/$', views.FeatureDetail.as_view(), name='feature-detail'),
	url(r'^features/(?P<pk>[0-9]+)/requirements/$', views.FeatureRequirementList.as_view(), 
		name='featurerequirement-list'),
	url(r'^features/(?P<pk>[0-9]+)/testcases/$', views.FeatureTestCaseList.as_view(), 
		name='featuretestcase-list'),
	url(r'^requirements/$', views.RequirementList.as_view(), name='requirement-list'),
	url(r'^requirements/(?P<pk>[0-9]+)/$', views.RequirementDetail.as_view(), name='requirement-detail'),
	url(r'^testcases/$', views.TestCaseList.as_view(), name='testcase-list'),
	url(r'^testcases/(?P<pk>[0-9]+)/$', views.TestCaseDetail.as_view(), name='testcase-detail'),
	url(r'^tree/$', views.TreeView.as_view(), name="tree-view"),
	url(r'^testmap/$', views.TestMapView.as_view(), name="testmap-view"),
]

urlpatterns = format_suffix_patterns(urlpatterns)