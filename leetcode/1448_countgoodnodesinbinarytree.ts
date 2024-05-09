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

function countNodes(root: TreeNode | null, maximum: number | null) {
    if (root === null) return 0
    const isGood = maximum === null || root.val >= maximum 
    const newMax = maximum === null ? root.val : Math.max(root.val, maximum)

    console.log(`node ${root.val}  newMax ${newMax}`)

    const leftCount = countNodes(root.left, newMax)
    const rightCount = countNodes(root.right, newMax)
    return leftCount + rightCount + (isGood ? 1 : 0)
}


function goodNodes(root: TreeNode | null): number {
    return countNodes(root, null)
};
