from __future__ import print_function
import Pyro4
import os

class Times(object):
    def __init__(self):
        self.minutes = '30'
        self.hours   = '6'
        self.day     = '*'

    def list_contents(self):
        return self.minutes,self.hours,self.day

    def setMinutes(self, mins):
#        print(mins)
        self.minutes = mins
#        print(self.minutes)
        print("Minutes set to {0}.".format(self.minutes))

    def setHours(self, hs):
        self.hours = hs
        print("Hours set to {0}.".format(self.hours))

    def setDay(self, d):
        self.day = d
        print("Day set to {0}.".format(self.day))

    def printTimes(self):
        print("Current settings are day {0}, at {1}:{2}".format(self.day, self.hours, self.minutes))

    def setAlarm(self):
        os.system('crontab -l | { cat; echo "'+str(self.minutes)+' '+str(self.hours)+' * * '+str(self.day)+' echo HelloWorld"; } | crontab -')

def main():
    times = Times()
    Pyro4.Daemon.serveSimple(
        {
            times: "example.times"
        },
        host = '192.168.0.249',
#        port = '2244',
        ns=True)


if __name__ == "__main__":
    main()
