import osmdt
import osmhm
import datetime
import time

while True:
    sequence, readFlag = osmhm.fetchLast()

    if readFlag is False:
        data_stream = osmdt.fetch(sequence['sequencenumber'])
        data = osmdt.process(data_stream)
        changesets = osmdt.extract_changesets(data)
        objects = osmdt.extract_objects(data)
        users = osmdt.extract_users(data)

        osmhm.filters.suspiciousFilter(changesets)
        osmhm.filters.userFilter(users)
        osmhm.filters.objectFilter(objects)

    nextTime = datetime.datetime.strptime(sequence['timestamp'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(minutes=60)

    if datetime.datetime.utcnow() < nextTime:
        timeToSleep = (nextTime - datetime.datetime.utcnow()).seconds + 1200.0
    else:
        timeToSleep = 0.0
    print "Waiting %2.1f seconds for the next state file." % (timeToSleep)

    time.sleep(timeToSleep)

    result = osmhm.fetchNext(sequence)

    if not result:
        print "File was not able to be retrieved yet. Waiting another 60 seconds."
        time.sleep(60.0)
