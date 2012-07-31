from django.db import models

class UploadSliderImg(models.Model):
	img = models.ImageField(upload_to='uploads')
	sort = models.IntegerField()
	
	def __unicode__(self):
		return '%s %s' % (self.img, self.sort)
