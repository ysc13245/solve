class Solution {
    public int solution(int n) {
        int fac=1;
        for (int i= 1;true;i++) {
            fac *= i;
                if (fac>n) return i-1;
        }
    }
}