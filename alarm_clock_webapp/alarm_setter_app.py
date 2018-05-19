#!/usr/bin/python

from flask import Flask, request, render_template, redirect, url_for
import os
import string

app = Flask(__name__)

# Define a route for the default URL, which loads the form   
@app.route('/')
def main():
    return render_template('form_submit.html')

@app.route('/results/', methods=['POST'])
def results():
    day=request.form['day']
    h=request.form['h']
    m=request.form['m']
    dir_to_play=request.form['dir_to_play']
    #if you passed the http link --> substitute http with /var/www and "%20"(space in html) with "\ "
    dir_to_play=string.replace(dir_to_play,"http://usersif.ddns.net","/var/www")
    #dir_to_play=string.replace(dir_to_play, "%20","\ ") #In principle this works, but awk gets confused 
    #--> I leave %20 for awk, then after installing the cron task I use sed to change "%20" in "\ "
    os.system("/bin/bash /home/pi/alarm_clock_webapp/change_cron.sh "+h+" "+m+" "+day+" "+dir_to_play)
    os.system("crontab -l | /bin/sed 's/%20/\\\ /g' | crontab -") ##html space in bash language
    os.system("crontab -l > /home/pi/alarm_clock_webapp/static/cron_jobs.txt")
    os.system("/bin/sed -i '/alarm/!d' /home/pi/alarm_clock_webapp/static/cron_jobs.txt") #you just care about alarm settings                    

    return render_template('results.html', day=day, h=h, m=m)

if __name__ == '__main__':
    app.run(debug=True)
