class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left= self.sortArray(nums[:mid])
        right= self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self,Left: List[int],Right: List[int]) ->List[int]:
        sorted_arr = []
        i=j=0
        while i < len(Left) and j < len(Right):
            if Left[i]<Right[j]:
                sorted_arr.append(Left[i])
                i+=1
            else:
                sorted_arr.append(Right[j])
                j+=1
        sorted_arr.extend(Left[i:])
        sorted_arr.extend(Right[j:])
        return sorted_arr
