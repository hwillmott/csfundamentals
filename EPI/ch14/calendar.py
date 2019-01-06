class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def findMaxSimultaneousEvents(events):
    endpoints = []
    for event in events:
        endpoints.append([event.start, True])
        endpoints.append([event.end, False])
    endpoints.sort(key=lambda x: x[0])
    
    count = 0
    maxCount = 0
    for point in endpoints:
        if point[1]:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count -= 1
    print maxCount

eventA = Event(2, 5)
eventB = Event(1, 3)
eventC = Event(4, 7)
eventD = Event(2, 6)

events = [eventA, eventB, eventC, eventD]

findMaxSimultaneousEvents(events)

