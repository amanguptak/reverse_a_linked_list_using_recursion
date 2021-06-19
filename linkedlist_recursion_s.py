class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def insert():
    l= [int(ele) for ele in input().split()]
    head=None
    temp=None
    for i in l:
        if i==-1:
            break
        newnode = Node(i)
        if head==None:

            head=newnode
            temp=newnode
        else:

            temp.next=newnode
            temp=newnode

    return head

def printl(head):
     cur=head
     while cur is not None:
            print(f"{cur.data} ->",end="")
            cur = cur.next
     print("None")

     return

def rev(head):
    if head is None or head.next is None:
        return head,head
    shead,stail=rev(head.next)
    stail.next=head
    head.next=None
    return shead,head



head=insert()
printl(head)
head , tail= rev(head)
print("reversed linked list is" )
printl(head)
