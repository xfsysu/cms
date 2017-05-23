import datetime
from haystack import indexes
from .models import Member

class MemberIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	
	name = indexes.CharField(model_attr='name')
	member_id = indexes.IntegerField(model_attr='member_id')
	major = indexes.CharField(model_attr='major')
	add_time = indexes.DateTimeField(model_attr='add_time')

	def get_model(self):
		return Member

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(add_time__lte=datetime.datetime.now())