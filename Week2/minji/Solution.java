class Solution {
    public int solution(int n, int[][] computers) {
        int count = 0;
        boolean[] flag = new boolean[n];
        
        for(int i=0; i<n; i++) {
            if(!flag[i]) {
                dfs(computers, i, flag);
                count++;
            }
        }
        
        return count;
    }
    
    void dfs(int[][] computers, int i, boolean[] flag) {
        flag[i] = true;
        
        for(int j=0; j<computers.length; j++) {
            if(i != j && computers[i][j] == 1 && flag[j] == false) {
                flag[j] = true;
                dfs(computers, j, flag);
            }
        } 
    }
}
