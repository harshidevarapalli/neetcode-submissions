class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a,b):
            nums[a],nums[b]=nums[b],nums[a]
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            swap(i, min_idx)