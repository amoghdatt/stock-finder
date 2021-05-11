### celery beat
- celery -A bhavcopy beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

### celery worker
- celery -A bhavcopy worker -l info -P solo

chmod +x /etc/init.d/celeryd
              /etc/init.d/celeryd start
              chmod +x /etc/init.d/celerybeat
              /etc/init.d/celerybeat start

touch /var/log/celery/bhavcopy-celeryd.log && 
              touch /var/log/celery/bhavcopy-celerybeat.log &&
              chmod 777 /var/log/celery/bhavcopy-celerybeat.log && 
              chmod 777 /var/log/celery/bhavcopy-celeryd.log && 