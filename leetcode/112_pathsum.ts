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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    return generate(root, targetSum, 0)
};

function generate(root: TreeNode | null, targetSum: number, currSum: number): boolean {
    if (root === null) return false
    const newSum = currSum + root.val
    if (newSum === targetSum && root.left === null && root.right === null) return true
    const leftSum = generate(root.left, targetSum, newSum)
    const rightSum = generate(root.right, targetSum, newSum)
    return leftSum || rightSum
}
