import java.util.*;
import java.io.*;

public class C1_P3_Hitchhiking_Fun {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = readInt(), b = readInt(), t = readInt();
            adjList.get(a - 1).add(new Edge(b, 0, t));
            adjList.get(b - 1).add(new Edge(a, 0, t));
        }

        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        Edge[] dist = new Edge[n];
        for (int i = 0; i < n; i++) {
            dist[i] = new Edge(0, (int) 1e9, (int) 1e9);
        }
        queue.add(new Edge(1, 0, 0));
        dist[0] = new Edge(0, 0, 0);

        while (!queue.isEmpty()) {
            Edge node = queue.poll();
            visited[node.vertex - 1] = true;
            for (Edge neighbour : adjList.get(node.vertex - 1)) {
                if (!visited[neighbour.vertex - 1]) {
                    Edge newDist = new Edge(0, node.distance + 1, node.safety + neighbour.safety);
                    if (newDist.compareTo(dist[neighbour.vertex - 1]) < 0) {
                        dist[neighbour.vertex - 1] = newDist;
                        queue.add(new Edge(neighbour.vertex, node.distance + 1, node.safety + neighbour.safety));
                    }
                }
            }
        }
        if (dist[n - 1].distance == (int) 1e9) {
            System.out.println(-1);
        } else {
            System.out.println(dist[n - 1].safety + " " + dist[n - 1].distance);
        }
    }

    static class Edge implements Comparable<Edge> {
        final int vertex;
        final int distance;
        final int safety;

        Edge(int v, int d, int s) {
            vertex = v;
            distance = d;
            safety = s;
        }

        public int compareTo(Edge o) {
            if (o.safety == this.safety) {
                return Integer.compare(this.distance, o.distance);
            } else {
                return Integer.compare(this.safety, o.safety);
            }
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
