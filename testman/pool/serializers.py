from pool.models import Domain, System, Function, Feature, Requirement, TestCase
from rest_framework import serializers

class DomainSerializer(serializers.HyperlinkedModelSerializer):
	systems = serializers.HyperlinkedIdentityField(view_name='domainsystem-list')
	class Meta:
		model = Domain
		fields = ('id', 'name', 'description', 'systems')

class SystemSerializer(serializers.HyperlinkedModelSerializer):
	# domain = serializers.HyperlinkedIdentityField(view_name='domain-detail')
	functions = serializers.HyperlinkedIdentityField(view_name='systemfunction-list')
	class Meta:
		model = System
		fields = ('id', 'name', 'description', 'domain', 'functions')

class FunctionSerializer(serializers.HyperlinkedModelSerializer):

	features = serializers.HyperlinkedIdentityField(view_name='functionfeature-list')
	class Meta:
		model = Function
		fields = ('id', 'name', 'description', 'system', 'features')

class FeatureSerializer(serializers.HyperlinkedModelSerializer):

	requirements = serializers.HyperlinkedIdentityField(view_name='featurerequirement-list')
	testcases = serializers.HyperlinkedIdentityField(view_name='featuretestcase-list')
	class Meta:
		model = Feature
		fields = ('id', 'name', 'description', 'function', 'requirements', 'testcases')

class RequirementSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Requirement
		fields = ('id', 'name', 'description', 'feature', 'req_id', 'functional')

# class FeatureField(serializers.RelatedField):
# 	# def get_attribute(self, obj):
# 	# 	return obj

# 	def to_representation(self, obj):
# 		return obj.name
# 	# def to_internal_value(self, data):
# 	# 	print (data)
# 	# 	feature = Feature.objects.get(feature__name=data.feature)
# 	# 	data.feature=feature
# 	# 	return Feature(data)

class TestCaseSerializer(serializers.ModelSerializer):

	feature = serializers.SlugRelatedField(queryset=Feature.objects.all(), slug_field='name')
	steps = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = TestCase
		fields = ('id', 'name', 'description', 'feature', 'test_id', 'steps')


class FeatureElement(serializers.ModelSerializer):
	class Meta:
		model = Feature 
		fields = ("id", 'name')

class FunctionElement(serializers.ModelSerializer):

	features = FeatureElement(many=True, read_only=True)
	class Meta:
		model = Function
		fields = ("id", "name", "features")

class SystemElement(serializers.ModelSerializer):

	functions = FunctionElement(many=True, read_only=True)
	class Meta:
		model = System
		fields = ("id", "name", "functions")

class TreeSerializer(serializers.ModelSerializer):

	systems = SystemElement(many=True, read_only=True)
	class Meta:
		model = Domain
		fields = ("id", "name", "systems")

from pool.models import TestStep, Composition

class CompositionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Composition
		fields = ('id', 'testcase', 'teststep', 'sequence')


