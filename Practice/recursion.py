"""Direct Recursion"""
def basics(n: int, sub):
    """Calculate factorial of n using recursion"""
    if n<0:
        return n
    
    print("n:", n)
    return basics(n-1, sub)

print("You have reached the end.")

print("Indirect recursion example:")
def function_a(n):
    if n <= 0:
        return
    print("Function A:", n)
    function_b(n - 1)

def function_b(n):
    if n <= 0:
        return
    print("Function B:", n)
    function_a(n - 1)

# Test the indirect recursion
function_a(5)

"""Tail Recursion"""
print("**Tail recursion example:**")
def tail_recursion(n: int,sub):
    if n<0:
        return n
    
    print("n:", n)
    return tail_recursion(n-1, sub)
tail_recursion(5)

print("**Head recursion example:**")
def head_recursion(n:int, sub):
    if n <= 0:
        return n