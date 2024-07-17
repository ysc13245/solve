class Solution {
    public int solution(int num, int k) {
        int l = (int)Math.log10(num)+1;
        int []iarr = new int[l];
        for (int i=l-1;i>=0;i--) {
            iarr[i]=num%10;
            num /= 10;
        }
        for (int i=0;i<l;i++) {
            if (iarr[i]==k) return i+1;
        }
        return -1;
    }
}