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

 // 3, even, q: 9 20
 // 20, odd, q: 15, 7, 9
 // 9, odd, q: 6, 8, 15, 7
 // 6, even, q: 8, 15, 7
 // 8, even, q: 15, 7, 12
 // 15, even, q: 7, 12, 1, 2
 // even: take from the end, add to the front, left node then right
 // odd: take from the front, add to the end, right node then left

function zigzagLevelOrder(root: TreeNode | null): number[][] {
    const q = [root]
    let level = 0
    const res = []
    while (q.length) {
        const len = q.length
        const even = level % 2 === 0
        const levelNodes = []
        for (let i=0; i<len; i++) {
            const curr = even ? q.pop() : q.shift()
            if (curr === null) continue
            levelNodes.push(curr.val)
            if (even) {
                q.unshift(curr.left)
                q.unshift(curr.right)
            } else {
                q.push(curr.right)
                q.push(curr.left)
            }
        }
        level += 1
        if (levelNodes.length > 0) res.push(levelNodes)
    }
    return res
};
