class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False

# had this problem giving me the right answers but didnt factor in edge cases where we are looking at the begining or end
# of the list and i was using a count to track the planting but really i should have just deducted n and then checked to 
# see if i ran out of plants to plant. looked at solution and changed some code but was 80% there id say. its good just
# getting the reps in.