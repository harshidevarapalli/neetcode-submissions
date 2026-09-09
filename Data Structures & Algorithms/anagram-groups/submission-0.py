class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans= defaultdict(list)
        for n in strs:
            count = [0]*26
            for char in n:
                count[ord(char)- ord('a')]+=1

            ans[tuple(count)].append(n)
        return list(ans.values())