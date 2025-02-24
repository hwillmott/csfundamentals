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

function detectCycle(head: ListNode | null): ListNode | null {
    if (!head) return null

    // two pointers, one fast, one slow
    let slow = head
    let fast = head.next
    let cycle = false
    while (fast && fast.next) {
        if (fast === slow) {
            cycle = true
            break
        }
        fast = fast.next.next
        slow = slow.next
    }

    if (!cycle) return null

    // found a cycle, measure how long it is
    let count = 1
    fast = fast.next
    while (fast !== slow) {
        fast = fast.next
        count = count + 1
    }

    // give fast a cycle-length headstart, when they meet, they're at the beginning
    fast = head
    slow = head
    for (let i = 0; i < count; i++) {
        fast = fast.next
    }

    while (fast != slow) {
        fast = fast.next
        slow = slow.next
    }

    return fast
};
