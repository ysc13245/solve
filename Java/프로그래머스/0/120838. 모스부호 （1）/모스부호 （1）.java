class Solution {
    public String solution(String letter) {
    String [] morses = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    
        StringBuilder sb = new StringBuilder();
        
        for (String s:letter.split(" ")) {
            
            for (int i=0;i<26;i++) {
                if (s.equals(morses[i])) sb.append((char)(i+'a'));
            }
        }
        return sb.toString();
    }
}
