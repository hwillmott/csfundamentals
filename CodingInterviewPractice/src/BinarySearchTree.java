import java.util.ArrayList;
import java.util.*;

public class BinarySearchTree 
{
	TreeNode root;
	
	public BinarySearchTree(){}
	
	public void Insert(int n)
	{
		if (root == null)
		{
			root = new TreeNode(n);
			return;
		}
		TreeNode curr = root;
		// get to leaf or parent of leaf
		while(true)
		{
			if (n < curr.data)
			{
				if (curr.left == null) 
				{
					curr.left = new TreeNode(n);
					return;
				}
				curr = curr.left;
			}
			else 
			{
				if (curr.right == null)
				{
					curr.right = new TreeNode(n);
					return;
				}
				curr = curr.right;
			}
		}
	}
	
	public TreeNode InsertRecursive(int n, TreeNode root)
	{
		if (root == null)
		{
			return new TreeNode(n);
		}
		if (n < root.data)
		{
			root.left = InsertRecursive(n, root.left);
		}
		else
		{
			root.right = InsertRecursive(n, root.right);
		}
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
