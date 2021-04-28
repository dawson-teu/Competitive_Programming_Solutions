import java.util.*;
import java.io.*;

public class Longest_Path {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int[] dp;
    static boolean[] visited;
    static List<List<Integer>> adjList;
    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();

        dp = new int[n];
        visited = new boolean[n];

        adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int x = readInt(), y = readInt();
            adjList.get(x - 1).add(y);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i + 1);
            }
        }

        int maxLength = -1;
        for (int i = 0; i < n; i++) {
            maxLength = Math.max(maxLength, dp[i]);
        }
        System.out.println(maxLength);
    }

    static void dfs(int vertex) {
        visited[vertex - 1] = true;
        for (int neighbour: adjList.get(vertex - 1)) {
            if (!visited[neighbour - 1]) {
                dfs(neighbour);
            }
            dp[vertex - 1] = Math.max(dp[vertex - 1], dp[neighbour - 1] + 1);
        }
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
