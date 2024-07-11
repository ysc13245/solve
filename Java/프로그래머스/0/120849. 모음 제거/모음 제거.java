class Solution {
    public String solution(String my_string) {
        String [] vowels = new String[] {"a", "i", "e", "o", "u"};
        
        for (String s : vowels) {
            my_string = my_string.replaceAll(s, "");
        }
        
        return my_string;
    }
}