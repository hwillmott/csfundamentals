import java.util.ArrayList;
import java.util.LinkedList;


public class BinaryTree 
{
	TreeNode root;
	
	public BinaryTree()
	{
		
	}
	
	public TreeNode BuildBalanced(int[] data, int start, int end)
	{
		if (end < start) return null;
		
		int middleIndex = (start + end)/2;
		TreeNode root = new TreeNode(data[middleIndex]);
		
		root.left = BuildBalanced(data, start, middleIndex - 1);
		root.right = BuildBalanced(data, middleIndex + 1, end);
		
		return root;
	}
	public ArrayList<LinkedList<TreeNode>> findLevelNodes()
	{
		int level = 0;
		ArrayList<LinkedList<TreeNode>> levelList = new ArrayList<LinkedList<TreeNode>>();
		LinkedList<TreeNode> list = new LinkedList<TreeNode>();
		list.add(root);
		levelList.add(level,list);
		while(true)
		{
			list = new LinkedList<TreeNode>();
			for(int i = 0; i < levelList.get(level).size(); i++)
			{
				TreeNode curr = levelList.get(level).get(i);
				if (curr != null)
				{
					if (curr.left != null) list.add(curr.left);
					if (curr.right != null) list.add(curr.right);
				}
			}
			if (list.size() > 0)
			{
				levelList.add(level + 1, list);
			}
			else break;
			level++;
			
		}
		return levelList;
	}
	
	public TreeNode FindCommonAncestor(TreeNode A, TreeNode B)
	{
		if(Search(A.data, root) == null || Search(B.data, root) == null) return null;
		TreeNode ancestor = root;
		while(true)
		{
			if(Search(A.data, ancestor.left) != null && Search(B.data, ancestor.left) != null) ancestor = ancestor.left;
			else if(Search(A.data, ancestor.right) != null && Search(B.data, ancestor.right) != null) ancestor = ancestor.right;
			else break;
		}		
		return ancestor;
	}
	
	public TreeNode Search(int n, TreeNode root)
	{
		if (root == null) return null;
		if (n == root.data) return root;
		if (n < root.data) return Search(n, root.left);
		else return Search(n, root.right);
	}
	
	public void InOrderTraversal(TreeNode root)
	{
		if (root == null) return;
		InOrderTraversal(root.left);
		System.out.print(root.data + " ");
		InOrderTraversal(root.right);
	}
	
	public void PreOrderTraversal(TreeNode root)
	{
		if (root == null) return;
		System.out.print(root.data + " ");
		PreOrderTraversal(root.left);
		PreOrderTraversal(root.right);
	}
	
	public void PostOrderTraversal(TreeNode root)
	{
		if (root == null) return;
		PostOrderTraversal(root.left);
		PostOrderTraversal(root.right);
		System.out.print(root.data + " ");
	}
}
