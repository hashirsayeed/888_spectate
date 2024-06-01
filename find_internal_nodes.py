def count_internal_node(given_list):
    #making a dictionary to map the children with its node
    children = {} 
    #traversing through the list
    for i in range(len(given_list)):
        #assigning value as a parent ot find the children
        parent = given_list[i]
        #checking if the value it -1 as it is the root node and root node does not have parent
        if parent == -1:
            continue 
        #checking for parents in the dictionary
        if parent in children:
            #adding the childrent to the parent
            children[parent].append(i)
        else:
            #creating a parent node in the dictionary
            #value of children is a list to store multiple children
            children[parent] = [i]

    #the parent nodes which have atleast more than 1 child
    internal_node = [node for node in children if len(children[node]) > 0]

    #output count of all the node which have atleast one child
    return len(internal_node)

given_list = [4, 4, 1, 5, -1, 4, 5]
print(f"Total number of internal node is {count_internal_node(given_list)}")

