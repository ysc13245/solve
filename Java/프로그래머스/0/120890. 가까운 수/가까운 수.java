import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        int m=0;
        int sub=100;
        Arrays.sort(array);
        
        for (int i=array.length-1;i>=0;i--) {
            if (Math.abs(array[i]-n)<=sub) {
                m = array[i];
                sub = Math.abs(m-n);
            }
        }
        return m;
    }
}