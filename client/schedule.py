import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from client.derbit_client import main


def run_scheduler(time):
    """the function runs the script according to the schedule"""
    scheduler = AsyncIOScheduler()
    scheduler.add_job(main, 'interval', minutes=time)
    scheduler.start()

    asyncio.get_event_loop().run_forever()


run_scheduler(1)

