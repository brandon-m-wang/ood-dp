class LispParser:
    
    def evaluate(self, expression: str) -> int:
        def tokenize(expression):
            tokens = []
            stack = 0
            subexpr = ""
            for char in expression:
                if char == "(":
                    stack += 1
                elif char == ")":
                    stack -= 1
                if stack == 0 and char == " ":
                    tokens.append(subexpr)
                    subexpr = ""
                else:
                    subexpr += char
            tokens.append(subexpr)
            return tokens
            
        def interpret(expression, stack):
            tokens = tokenize(expression)
            scope = stack[-1].copy()
            if tokens[0] == "let":
                for i in range(1, len(tokens)-1, 2):
                    if tokens[i+1][0] == "(":
                        tokens[i+1] = interpret(tokens[i+1][1:-1], stack + [scope])
                    elif not str(tokens[i+1]).lstrip("-").isnumeric():
                        tokens[i+1] = scope[tokens[i+1]]
                    scope[tokens[i]] = tokens[i+1]
                stack.append(scope.copy())
                if tokens[-1][0] == "(":
                    let_value = interpret(tokens[-1][1:-1], stack)
                    stack.pop()
                    return let_value
                else:
                    let_value = interpret(tokens[-1], stack)
                    stack.pop()
                    return let_value
            elif tokens[0] == "add" or tokens[0] == "mult":
                op, x1, x2 = tokens
                if x1[0] == "(":
                    x1 = interpret(x1[1:-1], stack)
                if x2[0] == "(":
                    x2 = interpret(x2[1:-1], stack)
                if not str(x1).lstrip("-").isnumeric():
                    x1 = scope[x1]
                if not str(x2).lstrip("-").isnumeric():
                    x2 = scope[x2]
                if op == "add":
                    return int(x1) + int(x2)
                if op == "mult":
                    return int(x1) * int(x2)
            else:
                x1 = tokens[0]
                if not str(x1).lstrip("-").isnumeric():
                    x1 = scope[x1]
                return x1
        
        return interpret(expression[1:-1], [{}])

# Test cases
# O(n)

lp = LispParser()
print(lp.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))
print(lp.evaluate("(let x 3 x 2 x)"))
print(lp.evaluate("(let x 1 y 2 x (add x y) (add x y))"))
print(lp.evaluate("(let z 2 (mult z (let x 3 y z (add x y))))"))
