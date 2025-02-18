/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let c1 = l1
    let c2 = l2 
    let result: ListNode = new ListNode()
    let r = result
    let carry = 0
    while (c1 !== null || c2 !== null || carry) {
        const sum = (c1 ? c1.val : 0) + (c2 ? c2.val : 0) + carry
        const remainder = sum % 10
        carry = sum / 10 >= 1 ? 1 : 0
        r.next = new ListNode(remainder)
        r = r.next
        if (c1) c1 = c1.next
        if (c2) c2 = c2.next
    }
    return result.next
};
