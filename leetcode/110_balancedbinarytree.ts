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

function isBalanced(root: TreeNode | null): boolean {
    if (!root) return true
    const res = goDown(root, 1)
    if (typeof res === 'boolean') return false
    return true
};

function goDown(root: TreeNode | null, currDepth: number): number | boolean {
    if (!root) return currDepth - 1
    const leftDepth = goDown(root.left, currDepth + 1)
    const rightDepth = goDown(root.right, currDepth + 1)
    if (typeof leftDepth === 'number' && typeof rightDepth === 'number') {
        if (Math.abs(leftDepth - rightDepth) > 1) return false
        return Math.max(leftDepth, rightDepth)
    } else {
        return false
    }
    
}
