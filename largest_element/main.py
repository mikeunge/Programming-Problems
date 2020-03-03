#!/bin/usr/python3 *

def findLargestElement(elements):
    """ Pass a list of integers. Find the largest (biggest) element. """
    biggest_elem = 0

    for elem in elements:
        if elem > biggest_elem:
            biggest_elem = elem
            print("[NEW] Biggest elem:", biggest_elem)
    return biggest_elem


def createNewList(SIZE):
    """ Create a reandom list of integers. """
    import random
    new_list = []   # Create new list.
    i = 0
    while i != SIZE:
        # Add new item to list.
        new_list.append(random.randint(1, 100))
        i = i + 1
    # Return the list.
    return new_list


def main():
    new_list = createNewList(10)
    biggest = findLargestElement(new_list)
    print(f"============\n Statistics\n============\nList size: {len(new_list)}\nBiggest Item: {biggest}")
    



if __name__ == '__main__':
    main()