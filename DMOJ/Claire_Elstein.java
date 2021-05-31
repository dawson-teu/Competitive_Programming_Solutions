import java.util.*;
import java.io.*;

public class Claire_Elstein {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), mod = (int) 1e9 + 7;
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        int[] in_degree = new int[n];
        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt();
            adjList.get(a - 1).add(b - 1);
            in_degree[b - 1] += 1;
        }
        long[] count = new long[n], dp = new long[n];
        Queue<Integer> queue = new LinkedList<>();
		for (int i = 0; i < n; i++) {
		    if (in_degree[i] == 0) {
		         queue.add(i);
		         count[i] = 1;
            }
        }
		while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int neighbour: adjList.get(node)) {
                count[neighbour] = (count[node] + count[neighbour]) % mod;
                dp[neighbour] = (dp[neighbour] + dp[node] + count[node]) % mod;
                in_degree[neighbour] -= 1;
                if (in_degree[neighbour] == 0) {
                    queue.add(neighbour);
                }
            }
        }
		long total = 0;
		for (int i = 0; i < n; i++) {
		    if (adjList.get(i).size() == 0) {
		        total = (total + dp[i]) % mod;
            }
        }
        System.out.println(total % mod);
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
