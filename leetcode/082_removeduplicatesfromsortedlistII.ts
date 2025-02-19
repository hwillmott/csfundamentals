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

function deleteDuplicates(head: ListNode | null): ListNode | null {
    let left = new ListNode(0, head)
    let head2 = left
    let first = head
    let last = head

    while (last) {
        while (last && last.val === first.val) {
            last = last.next
        }
        if (first.next === last) { // no duplicates
            left = first
        } else {
            left.next = last
        }

        first = last
    }
    return head2.next
};

function printList(head: ListNode | null) {
    const result = []
    while (head) {
        result.push(head.val)
        head = head.next
    }
    console.log(result)
}
