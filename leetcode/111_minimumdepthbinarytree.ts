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

function minDepth(root: TreeNode | null): number {
    const q: TreeNode[] = []
    if (!root) return 0
    q.push(root)
    let depth = 1
    while(q.length > 0){
        const qLen = q.length
        for (let i = 0; i < qLen; i++) {
            const node = q.shift()

            // found a leaf node, return
            if (!node.left && !node.right) {
                return depth
            }
            if (node.left) q.push(node.left)
            if (node.right) q.push(node.right)
        }
        depth = depth + 1
    }
    return 0 // this will never happen with a valid tree
};
