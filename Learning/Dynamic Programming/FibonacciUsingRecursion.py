# memoization


def fib(n: int) -> int:   
    if (n<=1):
        return 1
    else :
        #return fib(n-1) + fib(n-2) #O(n^n)
        return fib(n-2) #O(n)
    
def fibonacci_series(n: int) -> None:
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(fib(i))
    return fib_sequence    

if __name__ == "__main__":
    print(fib(50))
