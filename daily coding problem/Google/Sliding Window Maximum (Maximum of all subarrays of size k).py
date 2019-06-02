'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''
# Main Difference:
# maximum_of_subarrays does comparisons from the starting without storing any current max of any sort unlike FastetsSolution
# which does 1 comparsion before the following iterations thus letting it check for cases otherwise not possible in maximum_of_subarrays
def FastetsSolution(nums, k):
        if len(nums) == 0 or k==0: return [] # If the list or k is 0 then we return an empty array
        # Now the way maximum_of_subarrays is done is that the logic of both the functions are same but
        # but the difference between these two functions are that the FastestSolution method has two extra if conditons which
        # find two inferences from the approach of the solutions and it uses those inferences to add on the the solution list
        # without the k comparisons of the sliding window in O(1) solution for every iteration
        elif len(nums)<k:return [max(nums)] # If the length of the given list is lesser than k obviously we return the maximum of list elements
        max_value = max(nums[:k])
        res = [max_value]
        for i in range(len(nums)-k):
            if nums[i+k] > max_value:# If the element to be added to the sliding window next-nums[i+k] is greater than the max value of the previous sliding window- max_value
                                     # then we can just add nums[i+k] as it is obviously going to be the greatest number of the sliding wondow of the next iteration
                max_value = nums[i+k]
            elif nums[i] == max_value:# If the element removed from the sliding window at the next iteration is the max value then we have to find the maximum element by k comparisons
                max_value = max(nums[i+1:i+k+1])
            #Else we just append the previous maximum value as the next elelmnt added to the window is not greater than the maximum value of the previous list
            # and that maximum value exists inside the sliding window of the next Iteration
            res.append(max_value)
        return res
def maximum_of_subarrays(l,k):
    #We take upper value as 'l-k+1' as range  will give values from 0 to l-k not l-k+1 thus to get the subarray or sublist by using splice [:] we need l-k
    max_subarray=[]
    if len(nums)==0 or k==0:
            return []
    elif len(nums)<k:
        return [max(nums)]
    else:
        for i in range(len(nums)-k+1):
            subarray=nums[i:i+k]
            max_subarray.append(max(subarray))
        return max_subarray

if __name__=="__main__":

    k=int(input("Enter k: ")) # Takes input of k
    # Takes input of the the integers in string format then uses split function to sepearte them into a
    # list of strings which are then individually cnverted to an integer using the map function
    l=list(map(int,input("Enter the integers in the array seperated by a space: ").split(' ')))
    result=maximum_of_subarrays(l,k)# Computes the maximum of each subarray
    print("Result: ",result)
    result=FastetsSolution(l,k)# Computes the maximum of each subarray
    print("Result: ",result)
    
'''
Ouptut:

>>> 
 RESTART: E:/projects/coding/daily coding problem/google/Sliding Window Maximum (Maximum of all subarrays of size k).py 
Enter k: 3
Enter the integers in the array seperated by a space: 10 5 2 7 8 7
Result:  [10, 7, 8, 8]
'''

Fastest code

class Solution:
    
