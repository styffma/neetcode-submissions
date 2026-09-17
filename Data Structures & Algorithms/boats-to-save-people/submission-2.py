class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        liste = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if liste[left] + liste[right] > limit:
                right -=1
                boats +=1
            else:
                right-=1
                left+=1
                boats+=1        

        return boats   