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

function levelOrderBottom(root: TreeNode | null): number[][] {
    const q = [root]
    let res = []
    while (q.length > 0) {
        const qLen = q.length
        const level = []
        for (let i = 0; i < qLen; i++) {
            const curr = q.shift()
            if (!curr) continue
            level.push(curr.val)
            q.push(curr.left, curr.right)
        }
        if (level.length > 0) res.unshift(level)
    }
    return res
};
