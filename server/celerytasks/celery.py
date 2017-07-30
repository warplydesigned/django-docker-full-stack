import os

from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.config.settings')

# , broker='amqp://admin:mypass@rabbit', backend='redis://redis'
app = Celery('djangoapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# class CeleryConfig(AppConfig):
#     name = 'celerytasks'
#     verbose_name = 'Celery Config'

#     def ready(self):
#         app.config_from_object('django.conf:settings', namespace='CELERY')
#         installed_apps = [app_config.name for app_config in apps.get_app_configs()]
#         app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request)) # pragma: no cover
