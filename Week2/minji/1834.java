import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long sum = 0;
        long num = 0;
        
        for(long i=0; i<n; i++)
        {
            num = i*n+i;
            sum+=num;
        }

        bw.write(String.valueOf(sum));
        bw.flush();

	}
}
