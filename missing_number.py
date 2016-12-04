def find_missing(arr1 , arr2):
    if len(arr1) and len(arr2) == 0:
        return "should return 0 for empty list"
    elif arr1 == arr2:
        return "should return 0 for lists with the same entries"
    else:
        for a in arr1:
            if a in arr2:
                pass
            else:
                return a
