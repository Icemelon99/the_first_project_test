from __future__ import absolute_import, unicode_literals
from celery import Celery
import time


celery_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@celery_app.task
def add_test():
	time.sleep(5)
	return '(x+y)'