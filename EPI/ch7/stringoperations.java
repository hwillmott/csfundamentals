class stringoperations
{
    public static void main(String[] args)
    {
        char[] arr = {'a','c','b','a','a','_','_','_'};
        char[] arr2 = replaceAndRemove(arr);
        System.out.println("result " + new String(arr2));
    }

    public static char[] replaceAndRemove(char[] s)
    {
        int writeIndex = 0;
        int strLen = 0;
        for (char c: s)
        {
            if (c != 'b')
            {
                s[writeIndex] = c;
                writeIndex++;
            }
            if (c == 'a')
            {
                strLen++;
            }
            if (c == '_') break;
        }
        writeIndex--;
        strLen += writeIndex;
        System.out.println(strLen);
        while (writeIndex >= 0)
        {
            if (s[writeIndex] == 'a')
            {
                s[strLen--] = 'd';
                s[strLen--] = 'd';
            }
            else
            {
                s[strLen--] = s[writeIndex];
            }
            writeIndex--;
        }
        return s;
    }
}
