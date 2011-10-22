#!/usr/bin/python
#

from bugz import bugzilla
from xml.etree import ElementTree
import sys

bz=bugzilla.Bugz(base="",user="",password="")
#Setup Buglist, use command args, but if none exist use built in report
buglist=sys.argv
if len(buglist) == 1:
    print "Using Bugs worked Today report"
    for bug in bz.namedcmd('bugs worked today'):
        buglist.append(bug['bugid'])

FIELDS=(
        ('short_desc', 'Title'),
        ('assigned_to', 'Assignee'),
        ('creation_ts', 'Reported'),
        ('delta_ts', 'Updated'),
        ('bug_status', 'Status'),
        ('resolution', 'Resolution'),
        ('bug_severity', 'Severity'),
        ('priority', 'Priority'),
        )
print '--------------Bug Status Report-------------'
print '%d Bugs In Report' % len(buglist)
for bugnum in buglist[1:]:
    print '-----------------------------------------'
    bug=bz.get(bugnum)
    for field, name in FIELDS:
            try:
                value = bug.find('.//%s' % field).text
                if value is None:
                        continue
            except AttributeError:
                continue
            print '%-12s: %s' % (name, value)
    try:
        bug_comments=bug.findall('.//long_desc')
    except AttributeError:
        continue
    print '%-12s: %d' % ('Last Status', len(bug_comments))
    if len(bug_comments) > 1:
            comment_who=bug_comments[-1].find('.//who').text
            comment_when=bug_comments[-1].find('.//bug_when').text
            comment_text=bug_comments[-1].find('.//thetext').text
            print '%-12s at %s' % (comment_who,comment_when)
            print comment_text.strip()
    else:
        print "No status"
    print ''
    print ''
