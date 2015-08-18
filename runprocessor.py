from hallmonitor import *
import datetime
import time


while True:
    sequence, readFlag  = fetchLast()

    if not sequence:
        print 'Issues with database connection. Terminating program.'
        break

    if readFlag is False:
        process(sequence)

    nextTime = datetime.datetime.strptime(sequence['timestamp'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(minutes=60)

    if datetime.datetime.utcnow() < nextTime:
        timeToSleep = (nextTime - datetime.datetime.utcnow()).seconds + 1200.0
    else:
        timeToSleep = 0.0
    print "Waiting %2.1f seconds for the next state file." % (timeToSleep)

    time.sleep(timeToSleep)

    result = fetchNext(sequence)

    if not result:
        print "File was not able to be retrieved yet. Waiting another 60 seconds."
        time.sleep(60.0)
