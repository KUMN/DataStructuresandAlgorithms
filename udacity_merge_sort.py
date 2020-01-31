    """Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position<=0:
        return 0
    elif position==1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)

def get_fib(position):
    if position<=1:
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)

#Implement fibonacci series with a loop
def get_fib(pos):
    prev=0
    curr=1
    if pos==0:
        return prev
    if pos==1:
        return curr
    for i in range(2,pos+1):
        val=prev+curr
        prev=curr
        curr=val
    return val

#Implement fibonacci series by copying prior values in a hash map

#Implement merge sort
#Merge Sort
def merge_sort(input_list):
    output_list=[]
    l=len(input_list)
    if l <=1:
        output_list=input_list
    else:
        mid=int(l/2)
        left_half=merge_sort(input_list[:mid])
        right_half=merge_sort(input_list[mid:])
        ml=len(left_half) + len(right_half)
        i,j=0,0
        l_elem=left_half[i]
        r_elem=right_half[j]
        while True:
            if l_elem<r_elem:
                output_list.append(l_elem)
                i+=1
                try:
                    l_elem=left_half[i]
                except:
                    output_list=output_list+right_half[j:]
                    break
            else:
                output_list.append(r_elem)
                j+=1
                try:
                    r_elem=right_half[j]
                except:
                    output_list=output_list+left_half[i:]
                    break
    return output_list


