import java.util.*;

public class ChooseYourOwnPath {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        List<List<Integer>> adjList = init(n);
        for (int i = 0; i < n; i++) {
            int m = input.nextInt();
            if (adjList.get(i).size() == 0) {
                adjList.set(i, new ArrayList<>());
            }
            for (int j = 0; j < m; j++) {
                adjList.get(i).add(input.nextInt());
            }
        }
        input.close();

        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        List<Integer> paths = new ArrayList<>();
        q.add(1);
        visited[0] = true;
        dist[0] = 1;
        while (!q.isEmpty()) {
            int v = q.poll();
            if (adjList.get(v - 1).size() == 0) {
                paths.add(dist[v - 1]);
            }
            for (int w : adjList.get(v - 1)) {
                if (!visited[w - 1]) {
                    visited[w - 1] = true;
                    dist[w - 1] = dist[v - 1] + 1;
                    q.add(w);
                }
            }
        }

        boolean all_visited = true;
        for (boolean b : visited) {
            if (!b) {
                all_visited = false;
                break;
            }
        }
        if (all_visited) {
            System.out.println("Y");
        } else {
            System.out.println("N");
        }

        int min = 10001;
        for (int path : paths) {
            if (path < min) {
                min = path;
            }
        }
        System.out.println(min);
    }

    public static List<List<Integer>> init(int n) {
        List<List<Integer>> l = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            l.add(new ArrayList<>());
        }
        return l;
    }
}
