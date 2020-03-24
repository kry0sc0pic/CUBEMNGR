
def averager(times):
    avgTimes = times
    lowest = times[0]
    tottime = 0
    for x in times:
        if x < lowest:
            lowest = x

    avgTimes.remove(lowest)

    highest = times[0]

    for y in times:
        if y > highest:
            highest = y

    avgTimes.remove(highest)

    for z in avgTimes:
        tottime += z
    elements = len(avgTimes)
    avgsec = tottime/elements
    avgsec=round(avgsec)
    '''print(lowest)
    print(highest)
    print(avgTimes)
    print(avgsec)
'''
    #TODO : The tough part ( convert seconds into minutes and milliseconds)
    min = avgsec // 60
    t1 = min * 60
    sec = avgsec - t1

    return(min , sec)
