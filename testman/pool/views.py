from pool.models import Domain
from pool.serializers import DomainSerializer
from rest_framework import generics

class DomainList(generics.ListCreateAPIView):
	queryset = Domain.objects.all()
	serializer_class = DomainSerializer

class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Domain.objects.all()
	serializer_class = DomainSerializer

from pool.models import System
from pool.serializers import SystemSerializer

class SystemList(generics.ListCreateAPIView):
	queryset = System.objects.all()
	serializer_class = SystemSerializer

class DomainSystemList(generics.ListAPIView):
	queryset = System.objects.all()
	serializer_class = SystemSerializer

	def get_queryset(self):
		queryset = super(DomainSystemList, self).get_queryset()
		return queryset.filter(domain__id=self.kwargs.get('pk'))

class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = System.objects.all()
	serializer_class = SystemSerializer

from pool.models import Function
from pool.serializers import FunctionSerializer

class FunctionList(generics.ListCreateAPIView):
	queryset = Function.objects.all()
	serializer_class = FunctionSerializer

class SystemFunctionList(generics.ListAPIView):
	queryset = Function.objects.all()
	serializer_class = FunctionSerializer

	def get_queryset(self):
		queryset = super(SystemFunctionList, self).get_queryset()
		return queryset.filter(system__id=self.kwargs.get('pk'))

class FunctionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Function.objects.all()
	serializer_class = FunctionSerializer

from pool.models import Feature
from pool.serializers import FeatureSerializer

class FeatureList(generics.ListCreateAPIView):
	queryset = Feature.objects.all()
	serializer_class = FeatureSerializer

class FunctionFeatureList(generics.ListAPIView):
	queryset = Feature.objects.all()
	serializer_class = FeatureSerializer

	def get_queryset(self):
		queryset = super(FunctionFeatureList, self).get_queryset()
		return queryset.filter(function__id=self.kwargs.get('pk'))

class FeatureDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Feature.objects.all()
	serializer_class = FeatureSerializer


from pool.models import Requirement, TestCase
from pool.serializers import RequirementSerializer, TestCaseSerializer

class RequirementList(generics.ListCreateAPIView):
	queryset = Requirement.objects.all()
	serializer_class = RequirementSerializer

class FeatureRequirementList(generics.ListAPIView):
	queryset = Requirement.objects.all()
	serializer_class = RequirementSerializer

	def get_queryset(self):
		queryset = super(FeatureRequirementList, self).get_queryset()
		return queryset.filter(feature__id=self.kwargs.get('pk'))

class RequirementDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Requirement.objects.all()
	serializer_class = RequirementSerializer

class TestCaseList(generics.ListCreateAPIView):
	queryset = TestCase.objects.all()
	serializer_class = TestCaseSerializer

class FeatureTestCaseList(generics.ListAPIView):
	queryset = TestCase.objects.all()
	serializer_class = TestCaseSerializer

	def get_queryset(self):
		queryset = super(FeatureTestCaseList, self).get_queryset()
		return queryset.filter(feature__id=self.kwargs.get('pk'))

class TestCaseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = TestCase.objects.all()
	serializer_class = TestCaseSerializer 

# tree view preparation
from pool.serializers import TreeSerializer

class TreeView(generics.ListAPIView):
	queryset = Domain.objects.all()
	serializer_class = TreeSerializer

# test step mapping view
from pool.models import Composition
from pool.serializers import CompositionSerializer

class TestMapView(generics.ListCreateAPIView):
	queryset = Composition.objects.all()
	serializer_class = CompositionSerializer