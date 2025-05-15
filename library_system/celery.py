import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_overdue_loans': {'task': 'tasks.add', 'schedule': 30.0, 'args': (16, 16)},
}


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'check_overdue_loans': {
        'task': 'check_overdue_loans',
        'schedule': crontab(hour=0, minute=0,),
       
    },
}
app.conf.timezone = 'UTC'
