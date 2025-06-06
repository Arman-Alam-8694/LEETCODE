class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        n = len(num)

        def backtrack(index: int, path: str, eval_val: int, prev_num: int):
            if index == n:
                if eval_val == target:
                    result.append(path)
                return

            for i in range(index, n):
                # Current operand string
                curr_str = num[index:i+1]

                # Skip if the number has leading zeros
                if len(curr_str) > 1 and curr_str[0] == '0':
                    break

                curr = int(curr_str)

                if index == 0:
                    # First number, no operator before it
                    backtrack(i+1, curr_str, curr, curr)
                else:
                    # '+'
                    backtrack(i+1, path + '+' + curr_str, eval_val + curr, curr)

                    # '-'
                    backtrack(i+1, path + '-' + curr_str, eval_val - curr, -curr)

                    # '*'
                    backtrack(i+1, path + '*' + curr_str,
                              eval_val - prev_num + prev_num * curr,
                              prev_num * curr)

        backtrack(0, "", 0, 0)
        return result
