class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ty, tn = 0, 0
        n = len(customers)

        for i in customers:
            if i == "Y":
                ty += 1
            else:
                tn += 1

        penalty = float("inf")

        # Edge cases
        if ty == n:
            return n
        elif tn == n:
            return 0

        ans = 0
        lefty, leftn = 0, 0

        for i in range(n):
            # Current penalty = 'N' before closing + 'Y' after closing
            ptemp = leftn + (ty - lefty)
            if ptemp < penalty:
                penalty = ptemp
                ans = i

            # Update counts for next step
            if customers[i] == "Y":
                lefty += 1
            else:
                leftn += 1

     
        ptemp = leftn  
        if ptemp < penalty:
            ans = n

        return ans
