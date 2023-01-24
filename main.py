from deta import app
import time
import concurrent.futures
from CyberpeckerCronJob import CyberPeckerCronJob

@app.lib.cron()
def cron_task():
    cron_job: CyberPeckerCronJob = CyberPeckerCronJob()
    routes: list = cron_job._get_news_route()

    total_time_start: float = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=cron_job.WORKERS) as executor:
        futures = {executor.submit(cron_job.get_news_response, route) for route in routes}
        concurrent.futures.wait(futures)

    total_time_end = time.time()        
    
    return f'Successfully completed cronjob in : {round(total_time_end - total_time_start, 2)}s'