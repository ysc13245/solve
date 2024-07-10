class Solution {
    public int solution(int n) {
        n = n%2==0?n:n-1;
        // 2 => 2
        // 4 => 6 => (4 + 2) * 1
        // 6 => 12 => (6 + 2) * 1.5
        // 8 => 20 => (8 + 2) * 2
        return (n + 2) * n / 4; 
        
        
        
    }
}