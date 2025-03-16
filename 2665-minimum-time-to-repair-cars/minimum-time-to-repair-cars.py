# class Solution:
#     def repairCars(self, ranks: List[int], cars: int) -> int:
#         left=1
#         right=max(ranks)*cars*cars
#         n=len(ranks)
#         lookup=[0]*101
#         for i in ranks:
#             lookup[i]+=1
#         def isPossible(mid):
#             count=0
#             for i in range(1,len(lookup)):
#                 count+=(int(math.sqrt(mid//i))*lookup[i])
#                 if count>=cars:
#                     return True
#             return False

  
#         while left<=right:
#             mid=(left+right)//2
#             if isPossible(mid):
#                 right=mid-1
#             else:
#                 left=mid+1
#         return left

class Solution:
    def repairCars(self, rank: List[int], cars: int) -> int:
        # Count the frequency of each rank using a Counter
        count = Counter(rank)

        # Create a Min-heap storing [time, rank, n, count]:
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)

            # Deduct the number of cars repaired by this mechanic group
            cars -= count

            # Increment the number of cars repaired by this mechanic
            n += 1

            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])

        return time