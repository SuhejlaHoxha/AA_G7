from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(start, path):
            if len(path) >= 2:
                res.add(tuple(path))  
            
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return [list(seq) for seq in res]
    
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [4,6,7,7]
    print("Input:", nums1)
    print("Output:", sol.findSubsequences(nums1))
    print()
    
    nums2 = [4,4,3,2,1]
    print("Input:", nums2)
    print("Output:", sol.findSubsequences(nums2))
    print()
