import java.util.*;

class sort01 {
    public int[] solution(int[] array, int[][] command) {
        int[] answer = new int[command.length];
        int arr[];
        for (int i = 0; i < command.length; i++) {
            for (int j = 0; j < 3; j++) {
                arr = new int[command[i][1] - command[i][0] + 1];
                for (int k = 0; k < arr.length; k++) {
                    arr[k] = array[command[i][0] - 1 + k];
                }
                Arrays.sort(arr);
                answer[i] = arr[command[i][2] - 1];
            }
        }
        return answer;
    }
}