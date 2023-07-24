# QUESTION 5
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')


# QUESTION 6

# def postfix_to_prefix(postfix):
#     stack = []
#     for char in postfix:
#         if char.isalnum():
#             stack.append(char)
#         else:
#             operand1 = stack.pop()
#             operand2 = stack.pop()
#             expression = char + operand2 + operand1
#             stack.append(expression)
#     return stack.pop()

# postfix = input("Enter postfix expression: ")
# prefix = postfix_to_prefix(postfix)
# print("Prefix expression:", prefix)

