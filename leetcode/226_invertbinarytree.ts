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

// function invertTree(root: TreeNode | null): TreeNode | null {
//     const q = [root]
//     while (q.length) {
//         const curr = q.shift()
//         if (!curr) continue
//         const temp = curr.left
//         curr.left = curr.right
//         curr.right = temp
//         q.push(curr.left)
//         q.push(curr.right) 
//     }
//     return root
// };

function invertTree(root: TreeNode | null): TreeNode | null {
    if (!root) return root
    const temp = root.left
    root.left = root.right
    root.right = temp 
    invertTree(root.left)
    invertTree(root.right)
    return root
}
