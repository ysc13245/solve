class Solution {
    public int solution(int order) {
        int l = (int)Math.log10(order) + 1;
        int [] iarr = new int[l];
        for (int i = 0;i<l;i++) {
            iarr[i] = order % 10;
            order /= 10;
        }
        int sum = 0;
        for (int e: iarr) {
            sum += e == 3 || e==6 || e==9?1:0;
        }
        return sum;
    }
}