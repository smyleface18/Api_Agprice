from apscheduler.schedulers.background import BackgroundScheduler;
from task import dowload_save;

scheduler = BackgroundScheduler();

   
scheduler.add_job(dowload_save, 'interval', seconds = 30)

