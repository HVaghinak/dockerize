from datetime import datetime, date, timedelta
from celery.task.base import PeriodicTask


class CeleryTask(PeriodicTask):

    run_every = timedelta(seconds=1)

    def run(self, *args, **kwargs):
        print('running' + str(datetime.today().second))
