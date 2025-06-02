class Solution {
    public boolean isPalindrome(String s) {
        if(s.isEmpty()){
            return true;
        }
        int first = 0;
        int last = s.length()-1;
        while(first <= last){
            char currF = s.charAt(first);
            char currl = s.charAt(last);
            if( !Character.isLetterOrDigit(currF) ){
                first ++;
            } else if( !Character.isLetterOrDigit(currl) ){
                last --;
            } else{
                if(Character.toLowerCase(currF) != Character.toLowerCase(currl)){
                    return false;
                }
                first++;
                last--;
            }
        }
        return true;

    }
}