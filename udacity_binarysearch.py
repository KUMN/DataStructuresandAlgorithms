def binary_search_verbose(input_array, value):
    """Search until you get an array of legnth 2"""
    index_val=-1
    end=len(input_array)-1
    st=0
    while (end-st) > 1:
        mid = int((end+st)/2)
        if input_array[mid]==value:
            index_val=mid
            break
        elif value>input_array[mid]:
            st=mid
        else:
            end=mid

    if input_array[end]==value:
        index_val=end
    elif input_array[st]==value:
            index_val=st
    return index_val


def binary_search(input_array, value):
    """Search until array length is 1"""
    index_val=-1
    end=len(input_array)-1
    st=0
    while (end-st) >= 0:
        mid=int((end+st)/2)
        if input_array[mid]==value:
            index_val=mid
            break
        elif value>input_array[mid]:
            st=mid+1
        else:
            end=mid-1

    return index_val
