from math import comb

MOD = 10**9 + 7

def numOfWays(nums):
    def helper(arr):
        if len(arr) <= 2:
            return 1
        left = [x for x in arr[1:] if x < arr[0]]
        right = [x for x in arr[1:] if x > arr[0]]
        return comb(len(left) + len(right), len(left)) * helper(left) * helper(right) % MOD
    
    return (helper(nums) - 1) % MOD

if __name__ == "__main__":
    examples = [
        [2,1,3],
        [3,4,5,1,2],
        [1,2,3]
    ]

    for nums in examples:
        print(f"Input: {nums}, Output: {numOfWays(nums)}")
