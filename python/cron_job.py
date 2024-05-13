from apscheduler.schedulers.background import BackgroundScheduler;
from task import dowload_save;
from task import alert_price;




cron_dowload_save = BackgroundScheduler();
cron_save_price = BackgroundScheduler();
cron_alert_price = BackgroundScheduler();

   
cron_dowload_save.add_job(dowload_save, 'interval', seconds = 300000)
cron_alert_price.add_job(alert_price, 'interval', seconds = 86400)

