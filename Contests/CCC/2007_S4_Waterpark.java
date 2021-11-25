import java.util.*;
import java.io.*;

public class S4_Waterpark {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int x = readInt(), y = readInt();
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            adjList.add(new ArrayList<>());
        }
        while (x != 0 && y != 0) {
            adjList.get(x).add(y);
            x = readInt();
            y = readInt();
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        while (!queue.isEmpty()) {
            int curPoint = queue.poll();
            for (int neighbour: adjList.get(curPoint)) {
                if (!visited[neighbour]) {
                    visited[neighbour] = true;
                    queue.add(neighbour);
                }
                dp[neighbour] += dp[curPoint];
            }
        }
        System.out.println(dp[n]);
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
