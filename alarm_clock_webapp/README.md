# alarm_clock_webapp

http://hilpisch.com/rpi/03_web_apps.html

Installazioni:
```
sudo pip install Flask
sudo pip install flask-wtf
sudo pip install tornado
```

Setting:
```
git clone https://github.com/GiuseppeFasanella/alarm_clock_webapp.git
chmod +x alarm_clock_webapp/run_alarm_setter.py
sudo /home/pi/alarm_clock_webapp/run_alarm_setter.py
(aggiungi `sudo /home/pi/alarm_clock_webapp/run_alarm_setter.py` nella lista dei programmi all'avvio (in /etc/rc.local)

chmod +x alarm_clock_webapp/change_cron.sh
(aggiungi change_cron.sh nella lista dei programmi che posso essere utilizzati dall'utente generico www-data di apache)
(Se vuoi: io non l'ho fatto) Reindirizza la porta del raspberry in modo che dall'esterno ci si possa accedere
```


Usage:
```
da Browser:
usersif.ddns.net:8888

Oppure: ho un link diretto nel mio sito apache
```

```
Se cambi qualcosa nel codice, uccidi il run_alarm e fallo ripartire per testare le modifiche fatte
pi@raspberrypi ~/alarm_clock_webapp $ ps aux | grep "run_alarm"
pi        6278  0.0  0.1   3552  1828 pts/0    S+   19:10   0:00 grep --color=auto run_alarm
pi       19367  0.0  1.6  18640 15692 ?        S    Mar17   0:02 /usr/bin/python ./run_alarm_setter.py
pi@raspberrypi ~/alarm_clock_webapp $ kill -9 19367
pi@raspberrypi ~/alarm_clock_webapp $ ./run_alarm_setter.py &
[1] 6279
se hai messo dei print e vuoi vederli a schermo
./run_alarm_setter.py (senza la e' commerciale)
```
