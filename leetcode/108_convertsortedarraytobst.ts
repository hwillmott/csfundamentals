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

function sortedArrayToBST(nums: number[]): TreeNode | null {
    if (nums.length === 0) return null
    const middleIndex = Math.floor(nums.length / 2)
    const root = new TreeNode(nums[middleIndex])
    root.left = sortedArrayToBST(nums.slice(0, middleIndex))
    root.right = sortedArrayToBST(nums.slice(middleIndex+1))
    return root
};
