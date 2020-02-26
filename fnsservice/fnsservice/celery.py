from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
import logging
from django.conf import settings

logs_dir = settings.LOGS_DIR
logs_file_name = "celery.log"

log = logging.getLogger('celery_task')
log.setLevel(logging.INFO)
ch = logging.FileHandler(filename=os.path.join(logs_dir, logs_file_name))
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fnsservice.settings')

app = Celery('fns')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

#if __name__ == '__mail__':
#    app.start()

# celery -A fnsservice worker -l info -P eventlet
# -A fnsservice flower --port=5555 --brocker=redis://192.168.235.59:6379/0

# celery -A fnsservice worker -B -l info -P eventlet