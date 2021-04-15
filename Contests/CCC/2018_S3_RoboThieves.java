import java.util.*;
import java.io.*;

public class P6_RoboThieves {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        String[][] grid = new String[n][m];
        int startX = -1, startY = -1;
        for (int i = 0; i < n; i++) {
            String line = readLine();
            for (int j = 0; j < m; j++) {
                grid[i][j] = Character.toString(line.charAt(j));
                if (grid[i][j].equals("S")) {
                    startX = j;
                    startY = i;
                }
            }
        }
        boolean[][] camera = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!grid[i][j].equals("C")) {
                    continue;
                }
                for (int x = j + 1; x < m; x++) {
                    if (grid[i][x].equals("W")) {
                        break;
                    }
                    if (grid[i][x].equals(".") || grid[i][x].equals("S")) {
                        camera[i][x] = true;
                    }
                }
                for (int x = j - 1; x >= 0; x--) {
                    if (grid[i][x].equals("W")) {
                        break;
                    }
                    if (grid[i][x].equals(".") || grid[i][x].equals("S")) {
                        camera[i][x] = true;
                    }
                }
                for (int y = i + 1; y < n; y++) {
                    if (grid[y][j].equals("W")) {
                        break;
                    }
                    if (grid[y][j].equals(".") || grid[y][j].equals("S")) {
                        camera[y][j] = true;
                    }
                }
                for (int y = i - 1; y >= 0; y--) {
                    if (grid[y][j].equals("W")) {
                        break;
                    }
                    if (grid[y][j].equals(".") || grid[y][j].equals("S")) {
                        camera[y][j] = true;
                    }
                }
            }
        }
        Map<Integer, int[]> conveyorDest = new HashMap<>();
        boolean[][] convVisited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (conveyorDest.containsKey(i * m + j) || grid[i][j].equals(".") || grid[i][j].equals("W") || grid[i][j].equals("S") || grid[i][j].equals("C")) {
                    continue;
                }
                int[] endPoint = new int[]{j, i};
                boolean exit = false;
                boolean include = true;
                while (!exit) {
                    if (convVisited[endPoint[1]][endPoint[0]]) {
                        include = false;
                        break;
                    }
                    convVisited[endPoint[1]][endPoint[0]] = true;
                    switch (grid[endPoint[1]][endPoint[0]]) {
                        case "U" -> endPoint[1] -= 1;
                        case "D" -> endPoint[1] += 1;
                        case "L" -> endPoint[0] -= 1;
                        case "R" -> endPoint[0] += 1;
                        default -> exit = true;
                    }
                }

                if (include) {
                    int[] curPos = new int[]{j, i};
                    exit = false;
                    while (!exit && !(curPos[0] == endPoint[0] && curPos[1] == endPoint[1])) {
                        conveyorDest.put(curPos[1] * m + curPos[0], endPoint);
                        switch (grid[curPos[1]][curPos[0]]) {
                            case "U" -> curPos[1] -= 1;
                            case "D" -> curPos[1] += 1;
                            case "L" -> curPos[0] -= 1;
                            case "R" -> curPos[0] += 1;
                            default -> exit = true;
                        }
                    }
                } else {
                    camera[i][j] = true;
                }
                convVisited = new boolean[n][m];
            }
        }
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], (int) 1e9);
        }
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        if (!camera[startY][startX]) {
            queue.add(new int[]{startX, startY});
        }
        dist[startY][startX] = 0;
        visited[startY][startX] = true;
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            for (int[] neighbour : neighbours(grid, pos[0], pos[1], m, n, camera)) {
                if (!visited[neighbour[1]][neighbour[0]]) {
                    if (conveyorDest.containsKey(neighbour[1] * m + neighbour[0])) {
                        int[] newPos = conveyorDest.get(neighbour[1] * m + neighbour[0]);
                        if (!grid[newPos[1]][newPos[0]].equals("W") && !camera[newPos[1]][newPos[0]] && !(newPos[0] == pos[0] && newPos[1] == pos[1]) && dist[newPos[1]][newPos[0]] > dist[pos[1]][pos[0]] + 1) {
                            dist[newPos[1]][newPos[0]] = dist[pos[1]][pos[0]] + 1;
                            queue.add(newPos);
                        }
                    } else if (dist[neighbour[1]][neighbour[0]] > dist[pos[1]][pos[0]] + 1){
                        dist[neighbour[1]][neighbour[0]] = dist[pos[1]][pos[0]] + 1;
                        visited[neighbour[1]][neighbour[0]] = true;
                        queue.add(neighbour);
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j].equals(".")) {
                    if (dist[i][j] == (int) 1e9) {
                        System.out.println(-1);
                    } else {
                        System.out.println(dist[i][j]);
                    }
                }
            }
        }
    }

    public static List<int[]> neighbours(String[][] grid, int x, int y, int m, int n, boolean[][] camera) {
        List<int[]> output = new ArrayList<>();
        if (x - 1 >= 0 && !grid[y][x - 1].equals("W") && !camera[y][x - 1]) {
            output.add(new int[]{x - 1, y});
        }
        if (x + 1 < m && !grid[y][x + 1].equals("W") && !camera[y][x + 1]) {
            output.add(new int[]{x + 1, y});
        }
        if (y - 1 >= 0 && !grid[y - 1][x].equals("W") && !camera[y - 1][x]) {
            output.add(new int[]{x, y - 1});
        }
        if (y + 1 < n && !grid[y + 1][x].equals("W") && !camera[y + 1][x]) {
            output.add(new int[]{x, y + 1});
        }
        return output;
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
