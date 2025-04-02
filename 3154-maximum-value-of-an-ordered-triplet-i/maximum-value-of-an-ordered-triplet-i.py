from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxx = 0
        # Our prefix state: we use three variables:
        #   left  – stores the best “left” candidate (largest element seen in a prefix pair)
        #   center – stores the second element in the prefix pair
        #   right – optionally stores an additional element when updating the prefix
        left = None
        center = None
        right = None
        count = 0  # number of elements processed in the prefix
        
        for num in nums:
            # When we have at least two elements in the prefix (i.e. left and center set),
            # we treat the current num as the “right” candidate of the triplet.
            if count >= 2 and left is not None and center is not None:
                candidate = (left - center) * num
                if candidate > maxx:
                    maxx = candidate

            # Update the prefix state using only if/else conditions
            if center is None:
                # No element in the prefix yet; set center to current number.
                center = num
            elif left is None:
                # Exactly one element in prefix; shift center to left and update center.
                left = center
                center = num
            else:
                # We already have a pair (left, center).
                cur_value = left - center
                # Determine potential_new_left as the maximum among left, center, and right (if set)
                potential_new_left = left
                if center > potential_new_left:
                    potential_new_left = center
                if right is not None and right > potential_new_left:
                    potential_new_left = right

                # Decide whether to update right or to shift the prefix pair.
                if (potential_new_left - num) < cur_value:
                    # The drop from potential_new_left to current num is smaller than the current pair difference.
                    if right is None:
                        right = num
                    else:
                        if num > right:
                            right = num
                else:
                    # Otherwise, update the prefix: shift the best candidate into left and set center to current num.
                    left = potential_new_left
                    center = num
                    right = None
            count += 1
        return maxx if maxx > 0 else 0


