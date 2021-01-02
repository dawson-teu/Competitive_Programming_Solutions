import java.util.*;
import java.io.*;

public class InterNAV {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int m, n;
    static String[][] grid;
    static Position start;

    public static void main(String[] args) throws IOException {
        m = readInt();
        n = readInt();
        grid = new String[n][m];

        for (int i = 0; i < n; i++) {
            String line = readLine();
            for (int j = 0; j < m; j++) {
                if (String.valueOf(line.charAt(j)).equals("1")) {
                    start = new Position(j, i);
                }
                grid[i][j] = String.valueOf(line.charAt(j));
            }
        }

        List<Integer> result = bfs();
        Collections.sort(result);

        List<String> new_result = new ArrayList<>();
        for (Integer integer : result) {
            new_result.add(String.valueOf(integer));
        }

        System.out.println(String.join(" ", new_result));
    }

    public static List<Integer> bfs() {
        Queue<Position> q = new LinkedList<>();
        boolean[] visited = new boolean[m * n];
        List<Integer> roomsVisited = new ArrayList<>();
        q.add(start);
        visited[start.index1d()] = true;
        roomsVisited.add(1);
        while (!q.isEmpty()) {
            Position pos = q.poll();
            for (Position neighbour : neighbours(pos)) {
                if (!visited[neighbour.index1d()]) {
                    visited[neighbour.index1d()] = true;
                    if (is_digit(grid[neighbour.y][neighbour.x])) {
                        roomsVisited.add(Integer.parseInt(grid[neighbour.y][neighbour.x]));
                    }
                    q.add(neighbour);
                }
            }
        }
        return roomsVisited;
    }

    public static List<Position> neighbours(Position pos) {
        List<Position> neighbours = new ArrayList<>();
        for (int[] offset : new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}) {
            int newX = pos.x + offset[0];
            int newY = pos.y + offset[1];
            if (newX < m && newX >= 0 && newY < n && newY >= 0 && !grid[newY][newX].equals("#")) {
                neighbours.add(new Position(newX, newY));
            }
        }
        return neighbours;
    }

    public static boolean is_digit(String str) {
        return str.equals("1") || str.equals("2") || str.equals("3") || str.equals("4")
                || str.equals("5") || str.equals("6") || str.equals("7") || str.equals("8")
                || str.equals("9");
    }

    static class Position {
        final int x;
        final int y;

        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int index1d() {
            return y * m + x;
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

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
