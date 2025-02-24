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

function isValidBST(root: TreeNode | null): boolean {
    if (!root) return true
    const validLeft = ivb(root.left, root.val, null)
    const validRight = ivb(root.right, null, root.val)
    return validLeft && validRight
};

function ivb(curr: TreeNode | null, parentMax: number | null, parentMin: number | null): boolean {
    if (!curr) return true

    const isLessThanMin = parentMin !== null && (curr.val <= parentMin)
    const isMoreThanMax = parentMax !== null && (curr.val >= parentMax)

    // console.log({curr: curr.val, parentMax, parentMin, isLessThanMin, isMoreThanMax})

    if (isLessThanMin || isMoreThanMax) return false

    const validLeft = ivb(curr.left, curr.val, parentMin)
    const validRight = ivb(curr.right, parentMax, curr.val)
    return validLeft && validRight
}
