def fib(num):
    arr = [0,1]
    for x in range(2,num+1):
        arr.append(arr[x-1]+arr[x-2])
    return arr

if __name__ == "__main__":
    print(fib(int(input("Put any num bigger than 1: "))))