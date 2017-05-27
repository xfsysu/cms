from union.models import Member
from haystack import indexes

class MemberIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.CharField(model_attr='name')
	member_id = indexes.CharField(model_attr='member_id')
	major = indexes.CharField(model_attr='major')
	#sex = indexes.CharField(model_attr='sex')

	def get_model(self):
		return Member

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
