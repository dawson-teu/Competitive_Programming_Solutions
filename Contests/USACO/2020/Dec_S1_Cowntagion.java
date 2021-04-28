import java.util.*;
import java.io.*;

public class Dec_S1_Cowntagion {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] graph_degree = new int[n];
        for (int i = 0; i < n - 1; i++) {
            int a = readInt(); int b = readInt();
            graph_degree[a - 1] += 1;
            graph_degree[b - 1] += 1;
        }
        graph_degree[0] += 1;
        int total_time = 0;
        for (int i = 0; i < n; i++) {
            if (graph_degree[i] > 1) {
                int num_cows = 1;
                while (num_cows < graph_degree[i]) {
                    num_cows *= 2;
                    total_time += 1;
                }
            }
        }
        total_time += n - 1;
        System.out.println(total_time);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}
