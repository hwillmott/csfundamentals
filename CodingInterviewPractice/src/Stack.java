
public class Stack 
{
	Node top;
	int stacksize;
	
	public Stack()
	{
		stacksize = 0;
		top = null;
	}
	
	void push(int n)
	{
		if(stacksize == 0)
		{
			top = new Node(n);
		}
		Node newNode = new Node(n);
		newNode.next = top;
		top = newNode;
		stacksize++;
	}
	
	int pop()
	{
		if (stacksize == 0) return -1;
		int temp = top.data;
		top = top.next;
		stacksize--;
		return temp;
	}
	
	int peek()
	{
		if (top == null) return -1;
		return top.data;
	}
	
}
