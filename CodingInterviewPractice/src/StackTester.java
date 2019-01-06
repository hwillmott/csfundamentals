
public class StackTester 
{
	public static void main(String[] args)
	{
		Stack myStack = new Stack();
		int[] data = {1, 3, 5, 7, 2, 4, 6, 8, 0, 9, 2, 7, 4, 6};
		for (int i = 0; i < data.length; i++)
		{
			myStack.push(data[i]);
			System.out.println("Pushed: " + data[i]);
			//System.out.println("New min: " + myStack.mins.peek());
		}
		
		for(int i = 0; i < data.length; i++)
		{
			int temp = myStack.pop();
			System.out.println("Popped: " + temp);
			//System.out.println("New min: " + myStack.mins.peek());
		}
	}
}
