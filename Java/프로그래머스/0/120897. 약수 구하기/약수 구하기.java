import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int [] divisors = new int[n];
        int cnt = 0;
        for (int i = 1;i<=n;i++) {
            if (n%i==0) divisors[cnt++] = i;
        }
        
        divisors = Arrays.copyOf(divisors, cnt);
        return divisors;
    }
}