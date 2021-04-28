import java.util.*;
import java.io.*;

public class C4_P3_Counterattack {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = readInt();
            int b = readInt();
            int w = readInt();
            adjList.get(a - 1).add(new Edge(b, w));
            adjList.get(b - 1).add(new Edge(a, w));
        }

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        int[] dist1 = new int[n];
        int[] dist2 = new int[n];
        Arrays.fill(dist1, (int) 1e9);
        Arrays.fill(dist2, (int) 1e9);
        dist1[0] = 0;
        queue.add(1);
        visited[0] = true;

        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            visited[vertex - 1] = false;

            for (Edge neighbour : adjList.get(vertex - 1)) {
				if(dist1[neighbour.v - 1] > dist1[vertex - 1] + neighbour.w) {
					dist2[neighbour.v - 1] = dist1[neighbour.v - 1];
					dist1[neighbour.v - 1] = dist1[vertex - 1] + neighbour.w;
					if(!visited[neighbour.v - 1]) {
					    visited[neighbour.v - 1] = true;
					    queue.add(neighbour.v);
					}
				} else if(dist1[neighbour.v - 1] != dist1[vertex - 1] + neighbour.w && dist2[neighbour.v - 1] > dist1[vertex - 1] + neighbour.w) {
					dist2[neighbour.v - 1] = dist1[vertex - 1] + neighbour.w;
					if(!visited[neighbour.v - 1]) {
					    visited[neighbour.v - 1] = true;
					    queue.add(neighbour.v);
					}
				}
				if (dist1[neighbour.v - 1] != dist2[vertex - 1] + neighbour.w && dist2[neighbour.v - 1] > dist2[vertex - 1] + neighbour.w) {
					dist2[neighbour.v - 1] = dist2[vertex - 1] + neighbour.w;
					if(!visited[neighbour.v - 1]) {
					    visited[neighbour.v - 1] = true;
					    queue.add(neighbour.v);
					}
				}
            }
        }
        System.out.println(dist2[n - 1]);
    }

    static class Edge {
        final int v;
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
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
