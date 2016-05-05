from django.db import models

STATUS_CHOICES = (
	('INI', 'Initialized'),
	('DRT', 'Drafted'),
	('RVW', 'Reviewed'),
	('RLS', 'Released'),
)

class BaseElement(models.Model):
	name = models.CharField(max_length=200, default='')
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		ordering = ('-created',)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Domain(BaseElement):
	pass

class System(BaseElement):
	domain = models.ForeignKey(Domain, related_name='systems')

class Function(BaseElement):
	system = models.ForeignKey(System, related_name='functions')

class Feature(BaseElement):
	function = models.ForeignKey(Function, related_name='features')

class Requirement(BaseElement):
	feature = models.ForeignKey(Feature, related_name='requirements')
	req_id = models.CharField(max_length=20, default='REQ_0000_0000_0000')
	functional = models.BooleanField(default=True)

class TestStep(BaseElement):
	TYPE_CHOICES = (
		('PRE', 'Pre-condition'),
		('TS', 'Test-step'),
		('POS', 'Post-condition'),
	)
	step_type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='TS')
	action = models.TextField()
	reaction = models.TextField()

class TestCase(BaseElement):
	feature = models.ForeignKey(Feature, related_name='testcases')
	test_id = models.CharField(max_length=20, default='TS_0000_0000_0000')
	title = models.CharField(max_length=128, default='dummy test case')
	status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='INI')
	steps = models.ManyToManyField(TestStep, through='Composition')

	def __str__(self):
		return self.title

class Composition(models.Model):
	teststep = models.ForeignKey(TestStep, on_delete=models.CASCADE)
	testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
	sequence = models.PositiveIntegerField(default=0)
	class Meta:
		ordering = ('testcase', 'sequence',)

	def __str__(self):
		return "test case: {0} has Nr.{2} test step-> {1} ".format(self.testcase, self.teststep, self.sequence)

# class TestResult(BaseElement):
# 	execution_time = models.DateTimeField(blank=True, null=True)
# 	status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='INI')
# 	protocol = models.TextField()


