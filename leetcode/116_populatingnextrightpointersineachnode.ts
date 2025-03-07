/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     left: _Node | null
 *     right: _Node | null
 *     next: _Node | null
 *     constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function connect(root: _Node | null): _Node | null {
    let q = [root]

    while (q.length) {
        const l = q.length
        for (let i = 0; i < l; i++) {
            const curr = q.shift()
            if (!curr) continue
            curr.next = i === l - 1 ? null : q[0]
            q.push(curr.left)
            q.push(curr.right)
        }
    }
    return root
};
