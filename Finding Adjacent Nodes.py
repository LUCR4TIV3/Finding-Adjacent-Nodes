import \
    numpy as np  # I imported numpy so I could use advanced mathematical functions with huge, multidimensional arrays and matrices.

nodenum = (input("provide a number between 3 and 30 to decide how many nodes you want the adjacency matrix to have"))
while not (nodenum.isdigit() and 3 <= int(
        nodenum) <= 30):  # I use isdigit as my check system, making sure the user enter a valid input and the code doesn't crash.
    nodenum = input("Invalid input, please enter an integer between 3 and 30: ")

nodenum = int(nodenum)  # I change the nodenum value into an integer as isdigit only works with strings.
matrix = nodenum ** 2  # By squaring the number of nodes together we get the amount of possible paths between, aka matrix size.

arr = np.random.randint(0, 2,
                        matrix)  # This function creates an array with as many total values as the matrix value and randomized with 1s and 0s.
arr2 = arr.reshape(nodenum,
                   nodenum)  # This function reshapes the one long array into multiple smaller arrays as long as the original node num. This also makes it into a 2d array.
for i in range(nodenum):
    arr2[i, i] = 0  # This loop puts a zero where the nodes match up as the same nodes cant be adjacent to each other.

print(arr2)

print(f"GREAT! Above, you have randomly generated a {nodenum}-Node adjacency matrix array\n")
print("To check if 2 different nodes are adjacent to each other within the undirectional graph, output them below.")

node1 = input(f"What's the first node that you would like to check between 1-{nodenum}? ")
while not (node1.isdigit() and 1 <= int(node1) <= nodenum):
    node1 = input(f"Incorrect input. Please enter the first node between 1-{nodenum}: ")

node2 = input(f"What's the first node that you would like to check between 1-{nodenum}? ")
while not (node2.isdigit() and 1 <= int(node2) <= nodenum):
    node2 = input(f"Incorrect input. Please enter the first node between 1-{nodenum}: ") # Here I have asked for the 2 nodes that are being checked and also authenticated the input.

node1 = int(node1)
node2 = int(node2)
node1 = node1 - 1
node2 = node2 - 1 # I minus 1 off my input as the first node is in position zero within the array


def is_adjacent(y, x):
    if (arr2[y, x]) == 1:
        print("these two nodes in the adjacency matrix are adjacent")
    else:
        print("these two nodes in the adjacency matrix are not adjacent")


print(is_adjacent(node1, node2))
