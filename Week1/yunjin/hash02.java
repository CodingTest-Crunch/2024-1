import java.util.*;

class hash02 {
    // 풀이 1. 정렬과 배열로 풀기
    public String solution1(String[] participant, String[] completion) {
        Arrays.sort(participant); // a a b c
        Arrays.sort(completion);// a b c
        int i = 0;
        for (i = 0; i < completion.length; i++) {
            if (!completion[i].equals(participant[i])) {
                break;
            }
        }
        return participant[i];
    }

    // 풀이 2. 해시맵을 이용해서 풀기
    public String solution2(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String part : participant) {
            hm.put(part, hm.getOrDefault(part, 0) + 1);
        }
        for (String com : completion) {
            hm.put(com, hm.get(com) - 1);
        }

        for (String key : hm.keySet()) {
            if (hm.get(key) > 0) {
                answer = key;
                break;
            }
        }
        return answer;
    }
}
