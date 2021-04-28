import java.util.*;

public class P4_Herding {
    static int[][] trapPos;
    static String[][] city;
    static int n, m;
    static Map<String, Position> dirToPos;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();
        input.nextLine();
        city = new String[n][m];
        for (int i = 0; i < n; i++) {
            String line = input.nextLine();
            for (int j = 0; j < m; j++) {
                city[i][j] = String.valueOf(line.charAt(j));
            }
        }

        String[] dir = {"N", "E", "S", "W"};
        int[] pos = {0, -1, 1, 0, 0, 1, -1, 0};
        dirToPos = new HashMap<>();
        for (int i = 0; i < dir.length; i++) {
            dirToPos.put(dir[i], new Position(pos[i * 2], pos[i * 2 + 1]));
        }

        int trapCount = 0;
        trapPos = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (trapPos[i][j] == 0) {
                    trapCount += 1;
                    bfs(new Position(j, i), trapCount);
                }
            }
        }
        System.out.println(trapCount);
    }

    public static void bfs(Position start, int trap) {
        Queue<Position> q = new LinkedList<>();
        q.add(start);
        trapPos[start.y][start.x] = trap;
        while (!q.isEmpty()) {
            Position v = q.poll();
            for (Position neighbour : neighbours(v)) {
                trapPos[neighbour.y][neighbour.x] = trap;
                q.add(neighbour);
            }
            Position next = dirToPos.get(city[v.y][v.x]);
            next = new Position(v.x + next.x, v.y + next.y);
            if (trapPos[next.y][next.x] == 0) {
                trapPos[next.y][next.x] = trap;
                q.add(next);
            }
        }
    }

    public static List<Position> neighbours(Position pos) {
        Position[] neighbourCheckPos = {new Position(0, -1), new Position(1, 0), new Position(0, 1), new Position(-1, 0)};
        String[] neighbourDir = {"N", "E", "S", "W"};
        List<Position> neighbourPos = new ArrayList<>();
        for (int i = 0; i < neighbourCheckPos.length; i++) {
            int newX = pos.x - neighbourCheckPos[i].x;
            int newY = pos.y - neighbourCheckPos[i].y;
            String newDir = neighbourDir[i];
            if (newX >= 0 && newX < m && newY >= 0 && newY < n && city[newY][newX].equals(newDir)) {
                if (trapPos[newY][newX] == 0) {
                    neighbourPos.add(new Position(newX, newY));
                }
            }
        }
        return neighbourPos;
    }


    static class Position {
        final int x;
        final int y;

        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
