
public class LinkedListTester 
{
	public static void main(String[] args)
	{
		MyLinkedList myList = new MyLinkedList();
		int[] nums = {1,2,3,4,5,6,6,7,8,7,8,9,10};
		myList.PopulateList(nums);
//		myList.RemoveDuplicatesWithHash(myList.head);
//		myList.PopulateList(nums);
//		myList.RemoveDuplicatesWithoutHash(myList.head);
//		Node n = myList.FindNthToLast(3);
//		System.out.println("Nth to last: " + n.data);
//		System.out.println("Success");
		
		MyLinkedList listA = new MyLinkedList();
		MyLinkedList listB = new MyLinkedList();
		int[] numsA = {1, 2, 3};
		int[] numsB = {2, 9, 4, 5};
		listA.PopulateList(numsA);
		listB.PopulateList(numsB);
		MyLinkedList listC = listA.AddLists(listB);
		System.out.println("Success");
		
		
	}
}
