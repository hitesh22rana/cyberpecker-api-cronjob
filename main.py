from deta import app
import time
import concurrent.futures
from cyberpeckerCronJob import cyberPeckerCronJob

@app.lib.cron()
def cronTask(event):
    cronJob = cyberPeckerCronJob()
    routes = cronJob._getNewsRoute()

    totalTimeStart = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=cronJob.WORKERS) as executor:
        futures = {executor.submit(cronJob.getNewsResponse, route) for route in routes}
        concurrent.futures.wait(futures)

    totalTimeEnd = time.time()        
    
    return f'Successfully completed cronjob in : {round(totalTimeEnd - totalTimeStart, 2)}s'