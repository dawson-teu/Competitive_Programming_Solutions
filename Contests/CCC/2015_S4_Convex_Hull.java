import java.util.*;

public class ConvexHull {
    static int n, k;
    static List<List<Edge>> adjList;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        k = input.nextInt();
        n = input.nextInt();
        int m = input.nextInt();

        adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = input.nextInt();
            int b = input.nextInt();
            int t = input.nextInt();
            int h = input.nextInt();
            adjList.get(a - 1).add(new Edge(b, t, h));
            adjList.get(b - 1).add(new Edge(a, t, h));
        }
        int a = input.nextInt();
        int b = input.nextInt();
        int[][] result = dij(a);

        int ans = (int) 10e8;
        for (int i = 0; i < k; i++) {
            ans = Math.min(ans, result[b - 1][i]);
        }
        if (ans == (int) 10e8) {
            System.out.println("-1");
        } else {
            System.out.println(ans);
        }
    }

    public static int[][] dij(int start) {
        int[][] dist = new int[n][k];
        boolean[] visited = new boolean[n];
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                dist[i][j] = (int) 10e8;
            }
        }

        dist[start - 1][0] = 0;
        queue.add(new Edge(start, 0, 0));
        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = false;
            for (Edge neighbour : adjList.get(vertex.v - 1)) {
                for (int j = 0; j + neighbour.h < k; j++) {
                    int newDist = dist[vertex.v - 1][j] + neighbour.w;
                    if (newDist < dist[neighbour.v - 1][neighbour.h + j]) {
                        dist[neighbour.v - 1][neighbour.h + j] = newDist;
                        if (!visited[neighbour.v - 1]) {
                            visited[neighbour.v - 1] = true;
                            queue.add(new Edge(neighbour.v, newDist, 0));
                        }
                    }
                }
            }
        }
        return dist;
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;
        final int h;

        Edge(int v, int w, int h) {
            this.v = v;
            this.w = w;
            this.h = h;
        }

        public int compareTo(Edge o) {
            return Integer.compare(this.w, o.w);
        }
    }
}
