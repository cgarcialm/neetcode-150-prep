from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in dict_nums.keys():
                dict_nums[n] = [i]
            else:
                dict_nums[n].append(i)

        for n in dict_nums.keys():
            diff = target - n
            if (diff == n and len(dict_nums.get(n)) > 1):
                return dict_nums.get(n)[:2]
            elif (diff != n and diff in dict_nums.keys()):
                return [dict_nums.get(n)[0], dict_nums.get(diff)[0]]
        
        return []