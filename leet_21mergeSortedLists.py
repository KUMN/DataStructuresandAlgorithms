#Runtime: 36 ms, faster than 59%
#Memory Usage: 12.6 MB, less than 100.00%
#21 Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeTwoLists(l1, l2)
        i=l1
        j=l2
        o_l=ListNode(None)
        olp=o_l
        if not l1 and not l2:
            return olp.next
        elif not l1 and l2:
            while j:
                o_l.next=ListNode(j.val)
                o_l=o_l.next
                j=j.next
            return olp.next
        elif l1 and not l2:
            while i:
                o_l.next=ListNode(i.val)
                o_l=o_l.next
                i=i.next
            return olp.next
        else:
            l1_e=i.val
            l2_e=j.val
            while True:
                if l1_e<l2_e:
                    o_l.next=ListNode(l1_e)
                    o_l=o_l.next
                    i=i.next
                    try:
                        l1_e=i.val
                        continue
                    except:
                        while j:
                            o_l.next=ListNode(j.val)
                            o_l=o_l.next
                            j=j.next
                        break
                else:
                    o_l.next=ListNode(l2_e)
                    o_l=o_l.next
                    j=j.next
                    try:
                        l2_e=j.val
                        continue
                    except:
                        while i:
                            o_l.next=ListNode(i.val)
                            o_l=o_l.next
                            i=i.next
                        break
            return olp.next


#Merge multiple lists
def mergeKLists2(l1, l2):
    ll=[l1,l2]
    pdict={}
    ctr=0
    op=ListNode(None)
    opp=op

    for i in ll:
        if i:
            pdict[ctr]=i
            ctr=ctr+1
    x=None

    while len(pdict) > 0:
        for i in pdict.keys():
            if x is not None:
                if pdict[i].val<pdict[x].val:
                    x=i
            else:
                x=i
                
        op.next=ListNode(pdict[x].val)
        op=op.next
        pdict[x]=pdict[x].next
        if pdict[x] is None:
            pdict.pop(x, None)
            x=None

    return opp.next

#23 Merge multiple lists
#Time limit Exceeded
#BubbleSort
def mergeKLists(klist):
    ll=lists
    pdict={}
    ctr=0
    op=ListNode(None)
    opp=op

    for i in ll:
        if i:
            pdict[ctr]=i
            ctr=ctr+1

    def fn(i):
        return pdict[i].val

    while len(pdict)>0:
        q=sorted(pdict, key=fn)
        op.next=ListNode(pdict[q[0]].val)
        op=op.next
        if pdict[q[0]].next is not None:
            pdict[q[0]]=pdict[q[0]].next
        else:
            pdict.pop(q[0], None)

    return opp.next

#Divide and Conquer
def mergeKLists(lists):
    ll=lists
    l=len(lists)
    mid=int(l/2)

    if l<=0:
        return None
    elif l==1:
        return ll[0]
    elif l==2:
        return mergeTwoLists(ll[0], ll[1])
    else:
        left_l=mergeKLists(ll[:mid])
        right_l=mergeKLists(ll[mid:])
        return mergeTwoLists(left_l, right_l)




