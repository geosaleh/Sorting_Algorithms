# @PY4ALL
import numpy as np
import matplotlib.pyplot as plt
import random

plt.ion()
x = np.arange(1,20)


fig,ax = plt.subplots(2,2,dpi=120)
plt.show()

my_list = np.arange(1,20)
random.shuffle(my_list)
bubble_rects = ax[0][0].bar(x,my_list, align='center')
insertion_rects = ax[0][1].bar(x,my_list, align='center')
selection_rects = ax[1][0].bar(x,my_list, align='center')
shell_rects = ax[1][1].bar(x,my_list, align='center')
plt.tight_layout()
ax[0][0].set_ylim(0,20)
ax[0][0].set_title('Bubble Sort', pad=-40)
ax[0][1].set_ylim(0,20)
ax[0][1].set_title('Insertion Sort', pad=-40)
ax[1][0].set_ylim(0,20)
ax[1][0].set_title('Selection Sort')
ax[1][1].set_ylim(0,20)
ax[1][1].set_title('Shell Sort')

def bubble_sort(inlist):
    n = len(inlist);
    out_list = [*inlist]
    for i in range(n-1):
        swapped = False
        for j in range(n-1):
            # Compare elements
            if out_list[j] > out_list[j+1]:
                # Swap elements
                out_list[j+1], out_list[j] = out_list[j], out_list[j+1]	 
                swapped = True
                # Update the plot after swapping the elemnts
                for rect, h in zip(bubble_rects, out_list):
                    rect.set_height(h)
                plt.draw()
                plt.pause(0.02)
        # Break the main loop if no more swap
        if not swapped:
            break
    return out_list

def insertion_sort(inlist):
    n = len(inlist);
    out_list = [*inlist]

    for i in range(n):
        # Select element to be inserted
        valueToInsert = out_list[i]
        holePosition = i

        # Locate hole position for the element to be inserted 
        while holePosition > 0 and out_list[holePosition-1] > valueToInsert:
            out_list[holePosition] = out_list[holePosition-1]
            holePosition = holePosition -1
            for rect, h in zip(insertion_rects, out_list):
                rect.set_height(h)
            plt.draw()
            plt.pause(0.02)
        # Insert the elemnt at hole position
        out_list[holePosition] = valueToInsert
        # Update the plot after inserting the elemnt
        for rect, h in zip(insertion_rects, out_list):
            rect.set_height(h)
        plt.draw()
        plt.pause(0.02)

    return out_list
	

def selection_sort(inlist):
    n = len(inlist);
    out_list = [*inlist]

    for i in range(n):
        # Set current element as minimum
        min = i
        # Check the elements to get the minimum
        for j in range(i+1, n):
            if out_list[j] < out_list[min]:
                min = j
        # Swap the minimum element with the current element
        if min != i:
            out_list[i], out_list[min] = out_list[min], out_list[i]
            # Update the plot after swapping the elemnts
            for rect, h in zip(selection_rects, out_list):
                rect.set_height(h)
            plt.draw()
            plt.pause(0.02)


            
    return out_list
        
        
def shell_sort(inlist):
    out_list = [*inlist]
    interval = 0
    # Calculate interval
    while interval < len(out_list):
        interval = interval * 3 + 1

    while interval > 0:
        for outer in range(interval, len(out_list)):
            # Select value to be inserted
            valueToInsert = out_list[outer]
            inner = outer;
            # Shift element toward right
            while inner > interval -1 and out_list[inner - interval] >= valueToInsert:
                out_list[inner] = out_list[inner - interval]
                inner = inner - interval
                # Update the plot after shifting the elemnt
                for rect, h in zip(shell_rects, out_list):
                    rect.set_height(h)
                plt.draw()
                plt.pause(0.02)
            # Insert the element at the hole position    
            out_list[inner] = valueToInsert
            # Update the plot after inserting the element
            for rect, h in zip(shell_rects, out_list):
                rect.set_height(h)
            plt.draw()
            plt.pause(0.02)
        interval = (interval -1) //3;
    return out_list

# Run all sorting algorithms
bubble_sort(my_list)
insertion_sort(my_list)
selection_sort(my_list)
shell_sort(my_list)
