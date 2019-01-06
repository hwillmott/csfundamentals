import java.util.HashMap;


public class Strings {
	
	public static void main(String[] args)
	{
		String a = "abcdefg";
		String b = "abcdeff";
		String c = "aabcdef";
		String d = "abcdefghijklmnopqrstuvwxyz";
		
		System.out.println("Hash Test:");
		System.out.println(a + ": " + UniqueCharactersUsingHash(a));
		System.out.println(b + ": " + UniqueCharactersUsingHash(b));
		System.out.println(c + ": " + UniqueCharactersUsingHash(c));
		System.out.println(d + ": " + UniqueCharactersUsingHash(d));
		
		System.out.println("Array Test:");
		System.out.println(a + ": " + UniqueCharactersUsingArray(a));
		System.out.println(b + ": " + UniqueCharactersUsingArray(b));
		System.out.println(c + ": " + UniqueCharactersUsingArray(c));
		System.out.println(d + ": " + UniqueCharactersUsingArray(d));
		
		System.out.println("Reverse Test:");
		System.out.println(a + ": " + Reverse(a.toCharArray()).toString());
		System.out.println(b + ": " + Reverse(b.toCharArray()).toString());
		System.out.println(c + ": " + Reverse(c.toCharArray()).toString());
		System.out.println(d + ": " + Reverse(d.toCharArray()).toString());
	}
	public static boolean UniqueCharactersUsingHash(String s)
	{
		HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();
		for(int i = 0; i < s.length(); i++)
		{
			if(charMap.containsKey(s.charAt(i))) return false;
			charMap.put(s.charAt(i), Character.getNumericValue(s.charAt(i)));
		}
		return true;
	}
	
	public static boolean UniqueCharactersUsingArray(String s)
	{
		boolean[] charUsed = new boolean[256];
		for(int i = 0; i < s.length(); i++)
		{
			if(charUsed[s.charAt(i)]) return false;
			charUsed[s.charAt(i)] = true;
		}
		return true;
	}
	
	public static char[] Reverse(char[] str)
	{
		char temp;
		for(int i = 0; i < str.length/2; i++)
		{
			temp = str[i];
			str[i] = str[str.length - i - 1];
			str[str.length - i - 1] = temp;
		}
		return str;
	}

}
