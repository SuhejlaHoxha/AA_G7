# LeetCode 828 - Count Unique Characters of All Substrings of a Given String
# Jepet një string s. Për çdo substring të mundshëm, numëro sa karaktere shfaqen vetëm një herë. 
# Kthe shumen e këtyre numrave për të gjitha substringjet. 

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        index = {ch: [-1, -1] for ch in set(s)}
        res = 0

        for i, ch in enumerate(s):
            prev, last = index[ch]
            res += (i - last) * (last - prev)
            index[ch] = [last, i]

        for ch in index:
            prev, last = index[ch]
            res += (n - last) * (last - prev)

        return res

if __name__ == "__main__":
    sol = Solution()
    
    s1 = "ABC"
    print(f'Input: "{s1}" -> Output: {sol.uniqueLetterString(s1)}')  

    s2 = "ABA"
    print(f'Input: "{s2}" -> Output: {sol.uniqueLetterString(s2)}')  

    s3 = "LEETCODE"
    print(f'Input: "{s3}" -> Output: {sol.uniqueLetterString(s3)}')  
