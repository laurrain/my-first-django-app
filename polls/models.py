from django.db import models
import datetime
from django.utils import timezone


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'

    def _unicode_(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#def clean(self):
    #cleaned_data = self.cleaned_data
    #pub_date = cleaned_data.get('pub_date')
    #cleaned_data = Poll(self).clean()
    #if not cleaned_data['date']
        #cleaned_data['date'] = None
    #return cleaned_data


def _unicode_(self):
    return self.question


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    #@property

    def _unicode_(self):
        #return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
        return self.choice_text
    poll = models.ForeignKey(Poll)
    votes = models.IntegerField(default=0)

        # create your models here.
