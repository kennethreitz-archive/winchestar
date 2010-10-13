from django.db import models
import django

CATEGORIES = (
	('top', 'Top News'),
	('bus', 'Business'),
	('lif', 'Life'),
	('spt', 'Sports'),
	('opn', 'Opinions')
)

# Create your models here.
class Article(models.Model):
	title = models.CharField('title', max_length=256, unique=True)
	subtitle = models.CharField('sub-title', null=True, blank=True, max_length=256)
	published = models.DateTimeField('date published')
	section = models.CharField(max_length=20, choices=CATEGORIES)
	author = models.CharField('author', max_length=256,  null=True, blank=True)
	content = models.TextField('content')


	def __unicode__(self):
		return '%s by %s' % (self.title, self.author)

	@property
	def today(self):
		return self.pub_date.date() == datetime.date.today()