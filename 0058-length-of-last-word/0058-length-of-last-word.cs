public class Solution {
    public int LengthOfLastWord(string s) {
        string[] ss=s.Split(' ');
        for(int i=ss.Length-1;i>=0;i--)
            if(ss[i]!="")
                return ss[i].Length;
    return 0;
    }
}