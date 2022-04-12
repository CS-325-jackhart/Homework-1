import random
import time
from stoogesort import StoogeSort

def createlist(n):
    Data = [None] * n
    for i in range(n):
        Data[i] = random.randint(0, 10000)
    return Data


def main():
    
    for i in range(1, 11):
        list = createlist(5000 * i)
        past = time.time()
        StoogeSort(list, 0, len(list)-1)
        current = time.time()
        print(f"Time for list with {len(list)} elements:\t{current - past}")



if __name__ == "__main__":
    main()