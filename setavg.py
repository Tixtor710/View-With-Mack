def average(array):
    x=set(array)
    sum1=sum(x)
    average=sum1/len(x)
    return average
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)