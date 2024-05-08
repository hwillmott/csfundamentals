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

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function makeBST(head: ListNode, tail: ListNode) {
    if (head === tail) {
        return null
    }
    let fast = head
    let slow = head

    // find the middle of the list
    while (fast !== tail && fast.next != tail) {
        fast = fast.next.next
        slow = slow.next
    }

    // make a new TreeNode
    const middle = new TreeNode(slow.val)

    // make left and right trees
    middle.left = makeBST(head, slow)
    middle.right = makeBST(slow.next, tail)
    return middle
}

function sortedListToBST(head: ListNode | null): TreeNode | null {
    if (!head) return null
    return makeBST(head, null)
};
