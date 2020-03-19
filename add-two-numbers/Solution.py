
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def print_list(n: ListNode):
    current_value = n
    s = ''
    while current_value is not None:
        s += str(current_value.val)
        current_value = current_value.next
    print(s)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        current_result = None
        is_add_tens = False
        while l1 is not None or l2 is not None:
            ll1 = l1.val if l1 else 0
            ll2 = l2.val if l2 else 0
            current_sum = ll1 + ll2 + (1 if is_add_tens else 0)
            is_add_tens = current_sum >= 10
            new_result_node = ListNode(current_sum % 10)
            if result is None:
                result = new_result_node
                current_result = result
            else:
                current_result.next = new_result_node
                current_result = new_result_node

            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        if is_add_tens:
            new_result_node = ListNode(1)
            current_result.next = new_result_node
            current_result = new_result_node
        return result
            
if __name__ == "__main__":
    l11 = ListNode(5)
    l21 = ListNode(5)
    print_list(l11)
    print_list(l21)
    print_list(Solution().addTwoNumbers(l11, l21))