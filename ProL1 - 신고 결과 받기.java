import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        answer = new int[id_list.length];
        Map <String, HashSet<String>> temp = new HashMap<>();
        Map <String, Integer> ans = new HashMap<>();
        for (int i =0; i < id_list.length; i ++){
            HashSet<String> tmp = new HashSet<>();
            temp.put(id_list[i], tmp);
            ans.put(id_list[i],0);
        }
        for(String s : report){
            String[] re = s.split(" ");
            String first = re[0];
            String sec = re[1];
            temp.get(sec).add(first);
        }
        for(String t : temp.keySet()){
            HashSet<String> tmp2 = temp.get(t);
            if(tmp2.size() >= k){
                for(String t2 : tmp2){
                    ans.put(t2, ans.get(t2) + 1);
                }
            }
        }
        for(int i =0; i < id_list.length; i ++){
            answer[i] = ans.get(id_list[i]);
        }
        return answer;
    }
}