import java.util.Hashtable;


public class MyLinkedList 
{
	public Node head;
	
	public MyLinkedList()
	{
		this.head = null;
	}
	
	public void PopulateList(int[] nums)
	{
		this.head = new Node(nums[0]);
		Node n = head;
		for(int i = 1; i < nums.length; i++)
		{
			Node tmp = new Node(nums[i]);
			n.next = tmp;
			n = n.next;
		}
	}
	
	public void RemoveDuplicatesWithHash(Node n)
	{
		Hashtable table = new Hashtable();
		Node previous = n;
		while(n != null)
		{
			if(table.containsKey(n.data))
			{
				previous.next = n.next;
			}
			else
			{
				table.put(n.data, true);
				previous = n;
			}
			n = n.next;
		}		
	}
	
	public void RemoveDuplicatesWithoutHash(Node n)
	{
		Node current = n.next;
		Node previous = n;
		while(current != null)
		{
			Node runner = n;
			while(runner != current)
			{
				if(runner.data == current.data)
				{
					previous.next = current.next;
					break;
				}
				runner = runner.next;
			}
			previous = previous.next;
			current = previous.next;
		}
	}
	
	public Node FindNthToLast(int n)
	{
		Node current = head;
		for(int i = 0; i < n; i++)
		{
			if (current == null) return null;
			current = current.next;
		}
		Node nthToLast = head;
		while(current != null)
		{
			current = current.next;
			nthToLast = nthToLast.next;
		}
		return nthToLast;
	}
	
	public MyLinkedList AddLists(MyLinkedList B)
	{
		MyLinkedList A = this;
		MyLinkedList C = new MyLinkedList();
		Node currA = A.head;
		Node currB = B.head;
		
		Node currC = new Node();
		C.head = currC;
		
		boolean carry = false;
		
		while((currA != null) && (currB != null))
		{
			int data = currA.data + currB.data;
			if(carry) data++;
			currA = currA.next;
			currB = currB.next;
			if (data > 9)
			{
				carry = true;
			}
			currC.data = data%10;
			currC.next = new Node();
			currC = currC.next;
		}
		if (currA != null)
		{
			currC = currA;
		}
		else if (currB != null)
		{
			currC = currB;
		}
		return C;
	}
}


