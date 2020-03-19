class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            val = int(str(x)[::-1]) 
        else:
            val = int('-' + str(-x)[::-1])
        return val if - 2 ** 31  <= val <= 2 ** 31 -1 else 0

if __name__ == "__main__":
    print(Solution().reverse(1534236469))