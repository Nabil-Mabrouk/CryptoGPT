from __future__ import absolute_import, unicode_literals  # for python2
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptokilla.settings')

app = Celery('cryptokilla')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Paris')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')