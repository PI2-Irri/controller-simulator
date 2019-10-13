from django_cron import CronJobBase, Schedule

from .utils import create_module_measurement


class ModuleMeasurementCronJob(CronJobBase):
    RUN_EVERY_MINS = 0
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'measurements.cronjob.ModuleMeasurementCronJob'

    def do(self):
        create_module_measurement()
