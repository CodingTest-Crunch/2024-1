import java.util.*;

class Solution {
    public int solution1(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        // [a 머리][b 머리][c 발]
        for (int i = 0; i < clothes.length; i++) {
            hm.put(clothes[i][1], hm.getOrDefault(clothes[i][1], 0) + 1); // [머리 2] [발 1]
        }
        // 1가지 경우 : 2C1 + 1C1 = 3 a/b/c
        // 2가지 경우 : 2C1*1C1 = 2 ac/bc/
        // 총 5가지 경우 = (2+1)*(1*1)-1 = 5

        for (String key : hm.keySet()) {
            answer *= (hm.get(key) + 1);
        }
        return (answer - 1); // 공집합 제외
    }

    public int solution2(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        // [a 머리][b 머리][c 발]
        for (int i = 0; i < clothes.length; i++) {
            hm.put(clothes[i][1], hm.getOrDefault(clothes[i][1], 0) + 1); // [머리 2] [발 1]
        }
        for (int key : hm.values()) {
            answer *= (key + 1);
        }
        return (answer - 1);
    }
}