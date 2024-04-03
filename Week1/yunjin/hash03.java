package Week1.yunjin;

import java.util.*;

class hash03 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> hm = new HashMap<>();
        for (int i = 0; i < phone_book.length; i++) {
            hm.put(phone_book[i], 0);
        }
        // 123/ 12/ 5 가 hm에 저장되었을때
        // 1 12/ 1/ 이 hm에 존재하는지 확인하기
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 1; j < phone_book[i].length(); j++) {
                if (hm.containsKey(phone_book[i].substring(0, j))) {
                    answer = false;
                }

            }
        }
        return answer;
    }

    public static void main(String[] args) {
        hash03 h = new hash03();
        String[] phone_book = { "123", "12", "5", "12345" };
        boolean result = h.solution(phone_book);
        if (result) {
            System.out.println("해당 전화번호부에는 접두어가 없다");
        } else {
            System.out.println("해당 전화번호부에는 접두어가 존재한다");
        }
    }
}