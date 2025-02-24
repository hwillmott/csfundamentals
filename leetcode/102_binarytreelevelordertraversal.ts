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

function levelOrder(root: TreeNode | null): number[][] {
    const q = [root]
    const res = []

    while (q.length > 0) {
        const currLevelLength = q.length
        const level = []
        for (let i = 0; i < currLevelLength; i++) {
            const curr = q.shift()
            if (!curr) continue
            q.push(curr.left, curr.right)
            level.push(curr.val)
        }

        if (level.length > 0) res.push(level)
    }
    return res   
};
