# This functions checks if two time intervals collide or not
def collide_lecture(lecture1,lecture2):
    # If the end time of lecture1 is less than start time of lecture2
    # or the end time of lecture2 is less than start time of lecture1 
    if lecture1[1]<lecture2[0] or \
        lecture2[1] < lecture1[0]:
        return False
    else:
        return True
# We need to iterate through all the intervals in the given room 
# and check if the given interval collides with any of them or not
def collide(room,lecture_time):
    # The variable collision keeps track of: if there is a collision or not
    collision=False
    for lecture in room:
        if collide_lecture(lecture,lecture_time):
            collision=True
        return collision

def find_num_rooms(list_lecture_time):
    # We need to initialize rooms a list of list of lists
    # thus better than initializing it by:[] 
    # its better to use the list method thrice
    # Yes we do need a list of list of lists but intializing rooms as list()
    # is as good as initializing it as list(list(list()))
    rooms=list()
    # Now we populate the rooms
    # Generally it is better to this population in two stages:
    # 1) We store the first element, here the time interval 
    # 2) Then we store the non first elements by looping through them
    # These two stage approach helps in getting insights and maybe decraese the search or comaprison time
    # by gaining meaningful insights
    for m_lecture_time in list_lecture_time:
        if len(rooms)==0:
            rooms=[[[None,None]]]
            rooms[0][0]=m_lecture_time
        else:
            # Checks if a room got place in any of the exsting rooms or not
            roomed=False
            for room in rooms:
                if  not collide(room,m_lecture_time):
                    room.append(m_lecture_time)
                    roomed=True
                    break
            if not roomed:
                # We add braceds to i as i is just a list with two elelemnts but
                # what we need is a new room having this particular interval thus
                # we need a list of lists thus the braces
                rooms.append([m_lecture_time])
    # Now we show some debug info
    count=0
    for room in rooms:
        count+=1
        print("Room",count,": ",room)
        print('\n')
    return len(rooms)

                


#client code
list_lecture_times=[[0,50],[30,75],[60,150]]
num_rooms=find_num_rooms(list_lecture_times)
print("No. of rooms needed: ",num_rooms)
