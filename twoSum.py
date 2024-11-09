from typing import List

class Solution():
    def twoSum(nums:List[int], target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Holding Keys and Values after running through the loop
        index = {}
        for i, num in enumerate(nums):
            # checking the if differnce is target has a value in the list
            diff = target - num
            # check if the value is in the empty dictionary, if not store it in
            #  the dictionary and repeat the process until all the values in the list has been checked
            if diff in index:
                # Display the index of the values if found
                print([index[diff], i])
            # else, assign sore the value and it index in the dictionary
            index[num] = i



# Testing  
mylist = [1,2,3,5]
target = 8
Solution.twoSum(mylist,target)