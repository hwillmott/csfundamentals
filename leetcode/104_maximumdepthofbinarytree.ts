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

function getDepth(root: TreeNode | null, currentDepth) {
    if (!root) {
        return currentDepth
    }

    const leftDepth = getDepth(root.left, currentDepth+1)
    const rightDepth = getDepth(root.right, currentDepth+1)
    return Math.max(leftDepth, rightDepth)
}

function maxDepth(root: TreeNode | null): number {
    return getDepth(root, 0)
};
