from deta import app
import time
from threading import Thread
from cyberpeckerCronJob import cyberPeckerCronJob


@app.lib.cron()
def cron_task(event):
    cronJob = cyberPeckerCronJob()
    routes = cronJob._getNewsRoute()

    totalTimeStart = time.time()


    threads = [Thread(target=cronJob.worker) for _ in range(cronJob.WORKERS)]    

    [cronJob.tasks.put(route) for route in routes]
    [thread.start() for thread in threads]
    cronJob.tasks.join()
            
    totalTimeEnd = time.time()        
    
    return f'Successfully completed cronjob in : {round(totalTimeEnd - totalTimeStart, 2)}s'