/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     next: _Node | null
 *     random: _Node | null
 * 
 *     constructor(val?: number, next?: _Node, random?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */


function copyRandomList(head: _Node | null): _Node | null {
    if (!head) return null
    const nodeMap = new Map()
    let copyHead = new _Node(head.val)
    nodeMap.set(head, copyHead)
    let c = copyHead

    // first pass: make dictionary
    let n = head.next
    while (n) {
        const n2 = new _Node(n.val)
        nodeMap.set(n, n2)
        n = n.next
        c.next = n2
        c = c.next
    }

    // second pass: add random pointers
    n = head
    c = copyHead
    while (n) {
        const r = n.random
        const r2 = nodeMap.get(r)
        c.random = r2
        n = n.next
        c = c.next
    }

    return copyHead
};

function printList(head: _Node | null) {
    const res = []
    while (head) {
        res.push(head.val)
        head = head.next
    }
    console.log(res)
}
