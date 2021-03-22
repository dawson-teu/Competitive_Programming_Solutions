import java.util.*;
import java.io.*;

public class Adams_Party {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), k = readInt();
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt();
            adjList.get(a - 1).add(b);
            adjList.get(b - 1).add(a);
        }
        int[] forward_dist = new int[n];
        Arrays.fill(forward_dist, m);
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        forward_dist[0] = 0;
        visited[0] = true;
        queue.add(1);
        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            for (int neighbour: adjList.get(vertex - 1)) {
                if (!visited[neighbour - 1]) {
                    visited[neighbour - 1] = true;
                    forward_dist[neighbour - 1] = forward_dist[vertex - 1] + 1;
                    queue.add(neighbour);
                }
            }
        }

        int[] backwards_dist = new int[n];
        Arrays.fill(backwards_dist, m);
        queue = new LinkedList<>();
        visited = new boolean[n];
        backwards_dist[n - 1] = 0;
        visited[n - 1] = true;
        queue.add(n);
        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            for (int neighbour: adjList.get(vertex - 1)) {
                if (!visited[neighbour - 1]) {
                    visited[neighbour - 1] = true;
                    backwards_dist[neighbour - 1] = backwards_dist[vertex - 1] + 1;
                    queue.add(neighbour);
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (forward_dist[i] <= k && backwards_dist[i] <= k) {
                count += 1;
            }
        }
        int ans = 1;
        int exp = 0;
        while (exp < count - 2) {
            ans *= 2;
            ans %= (1e9 + 7);
            exp += 1;
        }
        System.out.println(ans);
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
