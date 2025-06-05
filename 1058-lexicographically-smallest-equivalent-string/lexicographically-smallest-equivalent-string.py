from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_to_slot = {}
        slot_min_char = []
        cur_slot = 0

        for a, b in zip(s1, s2):
            slot_a = char_to_slot.get(a)
            slot_b = char_to_slot.get(b)

            if slot_a is not None and slot_b is not None:
                if slot_a != slot_b:
                    # Merge slot_b into slot_a (lower index preferred)
                    if slot_min_char[slot_b] < slot_min_char[slot_a]:
                        slot_a, slot_b = slot_b, slot_a
                    for ch in char_to_slot:
                        if char_to_slot[ch] == slot_b:
                            char_to_slot[ch] = slot_a
                    slot_min_char[slot_a] = min(slot_min_char[slot_a], slot_min_char[slot_b])
            elif slot_a is not None:
                char_to_slot[b] = slot_a
                slot_min_char[slot_a] = min(slot_min_char[slot_a], a, b)
            elif slot_b is not None:
                char_to_slot[a] = slot_b
                slot_min_char[slot_b] = min(slot_min_char[slot_b], a, b)
            else:
                char_to_slot[a] = char_to_slot[b] = cur_slot
                slot_min_char.append(min(a, b))
                cur_slot += 1

        result = []
        for ch in baseStr:
            if ch in char_to_slot:
                result.append(slot_min_char[char_to_slot[ch]])
            else:
                result.append(ch)
        return "".join(result)
