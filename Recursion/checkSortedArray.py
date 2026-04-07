def isSorted(arr) -> bool:
        # code here
        n = len(arr)
        def check(i):
            if i >= n-1:
                return True
            if arr[i] > arr[i+1]:
                return False
            return check(i+1)
        return check(0)

arr = [1,2,3,4,5]
print(isSorted(arr))