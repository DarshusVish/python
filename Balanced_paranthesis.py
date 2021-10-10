def is_balanced(st):
    brackets = { "{" : "}", "(" : ")", "[" : "]" }
    open_bc = list(brackets.keys())
    close_bc = list(brackets.values())
    stack = []

    for s in st:
        if s in open_bc:
            stack.append(s)
        if s in close_bc:
            s_open = open_bc[close_bc.index(s)]
            if len(stack) > 0:
                if s_open != stack.pop():
                    return False
            else:
                return False
    if len(stack)>0:
        return False
    else:
        return True


check = is_balanced("}([()]){")

if check:
    print("Is balanced")
else:
    print("Is not balanced")
