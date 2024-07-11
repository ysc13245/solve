class Solution {
    public int solution(int n) {
        if (n < 1 || n > 1000000) throw new IllegalArgumentException();
        
        
        int answer = 0;
        
        for (int i = 1 ; i <= Math.pow(n, 0.5); i++) {
            if (n % i == 0) {
                answer += 2;
            }
        }
        if (Math.pow(n, 0.5) == (int)Math.pow(n, 0.5)) answer--;
        return answer;
    }
}