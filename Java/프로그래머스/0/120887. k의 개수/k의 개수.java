class Solution {
    public int solution(int i, int j, int k) {
        int cnt=0;
        for (i=i;i<=j;i++) {
            for (char c:(i+"").toCharArray()){
                if (c-'0'==k) cnt++;
            }
        }
        return cnt;
    }
}