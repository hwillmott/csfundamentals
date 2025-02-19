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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let h = head
    let t = head
    for (let i = 0; i < n; i++) {
        h = h.next
        console.log("h", h ? h.val: "null")
    }
    if (!h) return head.next

    while (h.next != null) {
        h = h.next
        t = t.next
        console.log({h: h ? h.val: "null", t: t ? t.val : "null"})
    }

    t.next = t.next.next
    return head
};
