
from math import *
class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0

        for i in range(n//2 + 1):
            b = n - 2*a
            cnt +omb(a + b, b)
        
        return cnt




    def getRow(self, rowIndex: int) -> List[int]:
        cnt = []
        
        for i in range(rowIndex + 1):
            cnt.append(comb(rowIndex,i))
        
        return cnt + 1
         
  


        