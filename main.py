from deta import app
import os, time, concurrent.futures
from CyberpeckerCronJob import CyberPeckerCronJob
from dotenv import load_dotenv
load_dotenv()

@app.lib.cron()
def cron_task(event):
    url = os.getenv("BASE_URL")
    cron_job: CyberPeckerCronJob = CyberPeckerCronJob()
    routes: list = cron_job._get_news_route()

    total_time_start: float = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=cron_job.WORKERS) as executor:
        futures = {executor.submit(cron_job.get_news_response, route) for route in routes}
        concurrent.futures.wait(futures)

    total_time_end = time.time()     
    
    return f'Successfully completed cronjob in : {round(total_time_end - total_time_start, 2)}s with {cron_job.WORKERS} workers and {len(routes)} routes to hit for {url}'