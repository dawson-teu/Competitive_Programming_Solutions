import java.util.*;

public class ET_P4_Exam_Delay {
    static List<List<Edge>> adjList;
    static double[] dist;
    static int[] parent;
    static int v;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        v = input.nextInt();
        int e = input.nextInt();

        adjList = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            int m = input.nextInt();
            int n = input.nextInt();
            int d = input.nextInt();
            int s = input.nextInt();
            adjList.get(m - 1).add(new Edge(n, (double) d / s * 60));
            adjList.get(n - 1).add(new Edge(m, (double) d / s * 60));
        }

        dij();
        int index = v - 1;
        int count = 0;
        while (!(parent[index] == -1)) {
            count += 1;
            index = parent[index];
        }
        System.out.println(count);
        System.out.println(Math.round(dist[v - 1] / 3));
    }

    public static void dij() {
        dist = new double[v];
        parent = new int[v];
        boolean[] visited = new boolean[v];
        for (int i = 0; i < v; i++) {
            dist[i] = 1e10;
            parent[i] = 0;
            visited[i] = false;
        }

        PriorityQueue<Edge> queue = new PriorityQueue<>();
        dist[0] = 0;
        visited[0] = true;
        parent[0] = -1;
        queue.add(new Edge(1, 0));
        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = true;
            for (Edge neighbour : adjList.get(vertex.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    double newDist = dist[vertex.v - 1] + neighbour.w;
                    if (newDist < dist[neighbour.v - 1]) {
                        dist[neighbour.v - 1] = newDist;
                        parent[neighbour.v - 1] = vertex.v - 1;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v - 1]));
                    }
                }
            }
        }
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final double w;

        Edge(int v, double w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge o) {
            return Double.compare(this.w, o.w);
        }
    }
}
