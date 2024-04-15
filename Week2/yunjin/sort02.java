import java.util.*;

class sort02 {
    public String solution(int[] numbers) {
        String answer = "";
        String arr[] = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        // 두개의 문자열을 합친 결과를 사전 순서로 비교한다.
        // 만약 합친 결과인 (b + a) 가 (a + b) 보다 순서상 크다면 양수 반환
        // (b + a)가 (a + b)와 사전 순서상 동일하다면 0을 반환
        // (b + a)가 (a + b)보다 사전 순서상으로 작다면 음수를 반환
        // [3, 30, 34, 5, 9] 를 9534330 으로 정렬
        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));
        // 정렬 후 만약 배열의 모든 값이 0일경우
        if (arr[0].equals("0")) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            sb.append(s);
        }
        return sb.toString();
    }
}