import java.util.ArrayList;
import java.util.LinkedList;


public class BinaryTreeTester 
{
	public static void main(String[] args)
	{
		BinaryTree tree = new BinaryTree();
		int[] data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		tree.root = tree.BuildBalanced(data, 0, 9);
		System.out.print("PreOrderTraversal: ");
		tree.PreOrderTraversal(tree.root);
		System.out.print("InOrderTraversal: ");
		tree.InOrderTraversal(tree.root);
		System.out.print("PostOrderTraversal: ");
		tree.PostOrderTraversal(tree.root);
		
		System.out.println();
		ArrayList<LinkedList<TreeNode>> levelList = tree.findLevelNodes();
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
		
		TreeNode commonAncestor = tree.FindCommonAncestor(tree.Search(0, tree.root), tree.Search(2, tree.root));
		System.out.println("common ancestor of 0 and 2: " + commonAncestor.data);
	}
}
