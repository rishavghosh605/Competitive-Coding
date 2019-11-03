"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""
def create_Hash_Map(flight_plan):
    hmap={}
    for origin,destination in flight_plan:
        if origin not in hmap.keys():
            hmap[origin]=[destination]
        else:
            hmap[origin]+=destination
            hmap[origin]=sorted(hmap[origin])
             
    print(hmap)
    return hmap

def find_itinerary(flight_plan,origin):
    hmap=create_Hash_Map(flight_plan)
    itinerary=list()
    itinerary.append(origin)
    while(True):
        
        if origin not in hmap.keys() or hmap[origin] == []:
            break
        destination = hmap[origin][0]
        itinerary.append(destination)
        hmap[origin]=hmap[origin][1:]
        origin=destination
    return itinerary if len(itinerary)-1 == len(flight_plan) else None
        

if __name__=="__main__":

    flight_plan=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    origin=input("Enter the origin of the intinerary: ")
    itinerary=find_itinerary(flight_plan,origin)
    print(itinerary)
