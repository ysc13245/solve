class Solution {
    public int solution(int n) {
        double answer = Math.pow(n,0.5);
        return answer == (int)answer?1:2;
    }
}