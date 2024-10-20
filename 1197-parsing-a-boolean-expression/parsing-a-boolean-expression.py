class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operators = []
        values_stack = []

        for char in expression:
            if char in 't':
                values_stack.append(True)
            elif char in 'f':
                values_stack.append(False)
            elif char in '&|!':
                operators.append(char)
            elif char == '(':
                # Start a new level of expression
                values_stack.append('(')  # Placeholder to mark the start
            elif char == ')':
                # Process the expression inside this level
                expr_values = []
                # Pop values until we reach '('
                while values_stack and values_stack[-1] != '(':
                    expr_values.append(values_stack.pop())
                values_stack.pop()  # Remove '('

                # Now, apply the operator to expr_values
                operator = operators.pop()
                if operator == '&':
                    result = all(expr_values)  # AND operation
                elif operator == '|':
                    result = any(expr_values)  # OR operation
                elif operator == '!':
                    result = not expr_values[0]  # NOT operation, should only have 1 value

                # Push the result back to values_stack
                values_stack.append(result)

        # The final result should be the only value left in values_stack
        return values_stack[0]
