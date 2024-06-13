def remove_duplicates(n, arr):
    seen = set()
    result = []
    
    # Traverse the array from the end to the beginning
    for i in range(n-1, -1, -1):
        if arr[i] not in seen:
            seen.add(arr[i])
            result.append(arr[i])
    
    # Reverse the result to maintain the original order
    result.reverse()
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = remove_duplicates(n, arr)
    print(" ".join(map(str, result)))

# Uncomment the following lines to run as a script
if __name__ == "__main__":
    main()
