class Solution {
    public int[] solution(int n, int [] numlist) {
        int cnt = numlist.length;
        for (int i = 0; i<numlist.length;i++) {
            if (numlist[i]%n!=0) {
                cnt--;
            }
        }
        int [] result = new int[cnt];
        int idx = 0;
        
        for (int m:numlist) {
            if (m%n == 0) result[idx++] = m;
        }
        return result;
    }
}