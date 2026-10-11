
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)
    second.next = first

    return second


def create_list(values):
    if not values:
        return None

    return Node(values[0], create_list(values[1:]))


def to_list(head):
    if head is None:
        return []

    return [head.val] + to_list(head.next)


head = create_list([1, 2, 3, 4])
head = swap_pairs(head)

print("Результат:", to_list(head))
