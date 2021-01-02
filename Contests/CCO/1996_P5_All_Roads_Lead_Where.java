import java.util.*;

public class AllRoadsLeadWhere {
    static Map<String, List<String>> adjList;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int m = input.nextInt(), n = input.nextInt();
        input.nextLine();
        adjList = new HashMap<>();
        for (int i = 0; i < m; i++) {
            String road = input.nextLine();
            String a = road.split(" ")[0], b = road.split(" ")[1];
            if (adjList.containsKey(a)) {
                adjList.get(a).add(b);
            } else {
                List<String> l = new ArrayList<>();
                l.add(b);
                adjList.put(a, l);
            }
            if (adjList.containsKey(b)) {
                adjList.get(b).add(a);
            } else {
                List<String> l = new ArrayList<>();
                l.add(a);
                adjList.put(b, l);
            }
        }
        for (int i = 0; i < n; i++) {
            String query = input.nextLine();
            String a = query.split(" ")[0], b = query.split(" ")[1];
            List<String> result = bfs(a, b);
            StringBuilder answer = new StringBuilder();
            for (int j = result.size() - 1; j >= 0; j--) {
                answer.append(result.get(j).charAt(0));
            }
            System.out.println(answer);
        }
    }

    public static List<String> bfs(String start, String target) {
        Queue<String> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        Map<String, String> parent = new HashMap<>();
        q.add(start);
        visited.add(start);
        while (!q.isEmpty()) {
            String v = q.poll();
            if (v.equals(target)) {
                List<String> path = new ArrayList<>();
                path.add(target);
                while (!path.get(path.size() - 1).equals(start)) {
                    path.add(parent.get(path.get(path.size() - 1)));
                }
                return path;
            }
            for (String neighbour : adjList.get(v)) {
                if (!visited.contains(neighbour)) {
                    visited.add(neighbour);
                    parent.put(neighbour, v);
                    q.add(neighbour);
                }
            }
        }
        return new ArrayList<>();
    }
}
