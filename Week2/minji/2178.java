import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 2178 {
	
	static int[][] map;
	static int n;
	static int m;
	static boolean[][] visited;
	static int[] dx = { -1, 1, 0, 0 };
    	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for(int i=0; i<n; i++) {
			String s = br.readLine();
			for(int j=0; j<m; j++) {
				map[i][j] = s.charAt(j) - '0';
			}
		}
		
		visited = new boolean[n][m];
		visited[0][0] = true;
		bfs(0, 0);
		System.out.println(map[n-1][m-1]);
	}

	public static void bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {x,y});
		
		while(!q.isEmpty()) {
			int now[] = q.poll();
			int x = now[0];
			int y = now[1];
			
			for(int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
		                if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                		    continue;
        		        if (visited[nx][ny] || map[nx][ny] == 0)
                    		continue;
                    
		                q.add(new int[] {nx, ny});
        		        map[nx][ny] = map[x][y] + 1;
                		visited[nx][ny] = true;
			}
		}
	}
}
