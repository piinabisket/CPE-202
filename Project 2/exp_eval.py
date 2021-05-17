from stack_array import *


class PostfixFormatException(Exception):
    pass


def reverse(string):
    """
    Reverse a string.
    Args:
        string(string): e.g. 'Forrest'.
    Returns:
        string: the previous string but reversed, e.g. 'tserroF'.
    """
    if string == "":
        return string
    else:
        return string[-1] + reverse(string[:-1])


def postfix_eval(input_str):
    """
    Takes in a postfix formatted string and calculates the solution.
    Args:
        input_str (string): a string in postfix format.
    Returns:
        int: solution to the input.
    """
    stack = StackLinked()
    input_fix = input_str.split()
    for val in input_fix:
        if val.isdigit():
            stack.push(int(val))
        else:
            if stack.num_items < 2:
                raise PostfixFormatException('Insufficient operands')
            elif val == '+':
                stack.push(stack.pop() + stack.pop())
            elif val == '-':
                minus = stack.pop()
                stack.push(stack.pop() - minus)
            elif val == '*':
                stack.push(stack.pop() * stack.pop())
            elif val == '/':
                if stack.top.val == 0:
                    raise ValueError
                dividend = stack.pop()
                stack.push(stack.pop() / dividend)
            elif val == '^':
                carat = stack.pop()
                x = stack.pop()
                y = x
                for i in range(carat-1):
                    y = y * x
                stack.push(y)
            else:
                raise PostfixFormatException('Invalid Token')
    if stack.num_items > 1:
        raise PostfixFormatException('Too many Operands')
    return stack.pop()


def infix_to_postfix(input_str):
    """
    Takes in an infix formatted string and returns a postfix formatted string.
    Args:
        input_str (string): a string in infix format.
    Returns:
        string: postfix formatted string.
    """
    RPN = []
    infix_stack = StackLinked()
    input_fix = input_str.split()
    for val in input_fix:
        if val.isdigit():
            RPN.append(val)
        elif val == '+ or -':
            infix_stack.push(val)
        elif val == '(':
            infix_stack.push(val)
        elif val == ')':
            while infix_stack.top.val != '(':
                RPN.append(infix_stack.pop())
            infix_stack.pop()
        elif val == '*' or val == '/':
            if infix_stack.is_empty() is False:
                if infix_stack.top.val == '*' or infix_stack.top.val == '/':
                    RPN.append(infix_stack.pop())
            infix_stack.push(val)
        else:
            infix_stack.push(val)
    while not infix_stack.is_empty():
        RPN.append(infix_stack.pop())
    return ' '.join(RPN)


def prefix_to_postfix(input_str):
    """
    Takes in a prefix formatted string and returns a postfix formatted string.
    Args:
        input_str (string): a string in prefix format.
    Returns:
        string: postfix formatted string.
    """
    prefix_stack = StackLinked()
    input_str = reverse(input_str)
    input_fix = input_str.split()
    for val in input_fix:
        if val.isdigit():
            prefix_stack.push(val)
        else:
            prefix_stack.push('%s %s %s' % (prefix_stack.pop(), prefix_stack.pop(), val))
    return ''.join(prefix_stack.pop())
