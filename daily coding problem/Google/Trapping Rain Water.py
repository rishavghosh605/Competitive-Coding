'''
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


'''

def find_total_water(elevation_map):
    left_max=0
    right_max=len(elevation_map)-1
    l=0
    r=len(elevation_map)-1
    total_water_count=0
    while l<=r:
        print("l",l)
        print("r",r)
        print(elevation_map[left_max],elevation_map[right_max])
        if elevation_map[left_max] <= elevation_map[right_max]:
            total_water_count+=(elevation_map[left_max]-elevation_map[l]) if elevation_map[left_max]-elevation_map[l]>=0 else 0
            print("addition: ",elevation_map[left_max],elevation_map[l])
            if elevation_map[l]>elevation_map[left_max]:
                left_max=l
            l+=1
        else:
            total_water_count+=(elevation_map[right_max]-elevation_map[r]) if elevation_map[right_max]-elevation_map[r]>=0 else 0
            print("addition: ",elevation_map[right_max],elevation_map[r])
            if elevation_map[r]>elevation_map[right_max]:
                right_max=r
            r-=1
    print(total_water_count)
            

if __name__=="__main__":

     elevation_map=list(map(int,input("Enter the elevation map: ").split()))
     find_total_water(elevation_map)
