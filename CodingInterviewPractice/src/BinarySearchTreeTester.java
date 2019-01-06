import java.util.*;

public class BinarySearchTreeTester 
{
	public static void main(String[] args)
	{
		BinarySearchTree tree = new BinarySearchTree();
		int[] data = {1, 3, 4, 2, 5, 7, 8, 9, 5, 6, 7};
		for(int i = 0; i < data.length; i++)
		{
			tree.Insert(data[i]);
			System.out.println("Inserted: " + data[i]);
			System.out.print("PreOrderTraversal: ");
			tree.PreOrderTraversal(tree.root);
			System.out.print("InOrderTraversal: ");
			tree.InOrderTraversal(tree.root);
			System.out.print("PostOrderTraversal: ");
			tree.PostOrderTraversal(tree.root);
			System.out.println();
		}
		System.out.println("Done");
		
		BinarySearchTree recursiveTree = new BinarySearchTree();
		for(int i = 0; i < data.length; i++)
		{
			recursiveTree.root = recursiveTree.InsertRecursive(data[i], recursiveTree.root);
			System.out.println("Inserted: " + data[i]);
			System.out.print("PreOrderTraversal: ");
			tree.PreOrderTraversal(recursiveTree.root);
			System.out.print("InOrderTraversal: ");
			tree.InOrderTraversal(recursiveTree.root);
			System.out.print("PostOrderTraversal: ");
			tree.PostOrderTraversal(recursiveTree.root);
			System.out.println();
		}
		System.out.println("Done");
		System.out.println("Search for 9: " + recursiveTree.Search(9, recursiveTree.root).data);
		System.out.println("Search for 3: " + recursiveTree.Search(3, recursiveTree.root).data);
		ArrayList<LinkedList<TreeNode>> levelList = recursiveTree.findLevelNodes();
		for (int i = 0; i < levelList.size(); i++)
		{
			System.out.print("Level " + i + ": ");
			for (int j = 0 ;j < levelList.get(i).size(); j++)
			{
				System.out.print(levelList.get(i).get(j).data + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
}
