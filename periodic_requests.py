import requests
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from twisted.internet import reactor


def send_request():
    requests.post("https://guarded-temple-96501.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })


if __name__ == '__main__':
        scheduler = BlockingScheduler(timezone="Africa/Lagos")
        scheduler.add_job(send_request,'cron', hour = '16', minute = '30')
        scheduler.start()
        reactor.run()
