class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        return z == 0 or (x + y >= z and z % (gcd(x, y)) == 0)
