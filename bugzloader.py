#!/usr/bin/python
#####
# Program to take csv file in format of
# Product,component,title,description,assigned_to,cc,blocked
# and turn into bugs
import csv
from bugz import bugzilla



bugsource=csv.reader(open('buglist.csv'),delimiter=',')
bz=bugzilla.Bugz(base="",user="",password="")

for bug in bugsource:
    if bug[0] == "PRODUCT":
        continue
    bugid=bz.post(product=bug[0], component=bug[1], title=bug[2], description=bug[3], assigned_to=bug[4], blocked=bug[6], cc=bug[5])
    print "Bug %s submitted with id= %i" % (bug[2],bugid)
    
