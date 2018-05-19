from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input


class Setter(object):
    def __init__(self, name):
        self.name = name

    def set(self, times):
#        print("This is {0}.".format(self.name))
        self.setMins(times)
        self.setHours(times)
        self.setDay(times)
        print("Settings applied.")
        times.printTimes()
        times.setAlarm()
        print("Alarm set.")

    def setMins(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("mins? ").strip()
        print(val)
        if val:
            times.setMinutes(val)

    def setHours(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("hours? ").strip()
        if val:
            times.setHours(val)

    def setDay(self, times):
        print("Current settings:")
        times.printTimes()
        val = input("day? ").strip()
        if val:
            times.setDay(val)

