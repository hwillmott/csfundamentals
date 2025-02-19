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

function swapPairs(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head
    let l = head
    let r = head.next

    printList(head)

    let p: ListNode | null
    head = r

    while (r) {
        // swap nodes
        if (p) p.next = r
        l.next = r.next
        r.next = l

        // printList(head)

        // move forwards
        p = l
        l = l.next
        r = l ? l.next : null
        // console.log({l: l ? l.val : "null", r: r ? r.val : "null", p: p ? p.val : "null"})
    }

    return head
};

function printList(head: ListNode | null) {
    const result = []
    while (head) {
        result.push(head.val)
        head = head.next
    }
    console.log(result)
}
