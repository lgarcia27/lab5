# CS2302 Data Structures
# Programmed by Luis Garcia.
# Last modified December 5, 2018.
# Instructor Diego Aguirre.
# Implementation of heaps and heap sort in order to sort a list
# and return the unsorted list followed by the sorted list
# Finding the smallest method and returning from smallest to biggest.

# Class and method given by professor.
# Some lines were missing of the code and
# I implemented whatever was left incomplete and necessary.
class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)
        self.percolateUp()

    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]

        newValue = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = newValue
            self.percolate_down(0)
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0
# This method is used to compare the parent and child node and if the comparision
# violates the heap property then they will be switched and done so until heap
# property is maintained.
# this is used when the min value in the heap is extracted.
    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i+child_index]
                    min_index = i + child_index
                i = i + 1

            if min_value == value:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                node_index = min_index
                child_index = 2 * node_index + 1
# this method is used to compare the parent and child node and if the comparision
# violates the heap property then
# they will be switched and done so until heap property is maintained at the root of
# the heap.
# this is used when a new node is added to the heap
    def percolateUp(self):
        node_index = len(self.heap_array) - 1
        if node_index == 0:
            return
        while node_index > 0:
            parent_index = (node_index-1)//2  # Compute the parent node's index
            if self.heap_array[node_index] < self.heap_array[parent_index]:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                node_index = parent_index

            else: # Heap property is maintained.
                break # Nothing else is required and program breaks
# A unsorted array is the expected input and the sorting is done by extraction of the min node,
# if percolate down is done correct then the result should be sorted with the min being at the beginning of the array
    def heap_sort(self):
        res = []
        while not self.is_empty():
            res.append(self.extract_min())
        return res

    def print_heap(self):
        for i in range(len(self.heap_array)):
            print(self.heap_array[i])

def main():
    smallestHeap = Heap()
    file_name = input("What's the name of the file that we are sorting today?\n")
    file = open(file_name, "r")
    print("Here are the results:")
    for line in file:
        curr = line.split(",")
        for number in curr:
            smallestHeap.insert(int(number))
    print("")
    print("This is the unsorted list:")
    smallestHeap.print_heap()
    sorted_min_heap = smallestHeap.heap_sort()
    print("This is the sorted list:")
    print(sorted_min_heap)
main()