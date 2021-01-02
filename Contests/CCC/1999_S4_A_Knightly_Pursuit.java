import java.util.*;

public class AKnightlyPursuit {
    static int[][] board;
    static int r, c, pr, pc, kr, kc;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        for (int l = 0; l < n; l++) {
            r = input.nextInt();
            c = input.nextInt();
            pr = input.nextInt();
            pc = input.nextInt();
            kr = input.nextInt();
            kc = input.nextInt();
            board = new int[r][c];
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    board[i][j] = -1;
                }
            }

            bfs();
            String outcome = "l";
            int moves = 0;
            for (int i = pr - 1; i < r - 1; i++) {
                int time = i - pr + 1;
                if (board[i][pc - 1] >= 0 && board[i][pc - 1] <= time && (time - board[i][pc - 1]) % 2 == 0) {
                    outcome = "w";
                    moves = time;
                    break;
                }
                if (board[i + 1][pc - 1] >= 0 && board[i + 1][pc - 1] <= time + 1
                        && (time - board[i + 1][pc - 1]) % 2 == 0) {
                    outcome = "s";
                    moves = time;
                    break;
                }
            }

            if (outcome.equals("w")) {
                System.out.println("Win in " + moves + " knight move(s).");
            } else if (outcome.equals("s")) {
                System.out.println("Stalemate in " + moves + " knight move(s).");
            } else {
                System.out.println("Loss in " + (r - pr - 1) + " knight move(s).");
            }
        }
        input.close();
    }

    public static void bfs() {
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(kc, kr));
        board[kr - 1][kc - 1] = 0;
        while (!q.isEmpty()) {
            Position pos = q.poll();
            for (Position neighbour : neighbours(pos)) {
                board[neighbour.y - 1][neighbour.x - 1] = board[pos.y - 1][pos.x - 1] + 1;
                q.add(neighbour);
            }
        }
    }

    public static List<Position> neighbours(Position pos) {
        int[] neighbourCheckPos = { 1, 2, 2, 1, 2, -1, 1, -2, -1, -2, -2, -1, -2, 1, -1, 2 };
        List<Position> neighbourPos = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            int newX = pos.x + neighbourCheckPos[i * 2] - 1;
            int newY = pos.y + neighbourCheckPos[i * 2 + 1] - 1;
            if (newX >= 0 && newX < c && newY >= 0 && newY < r && board[newY][newX] == -1) {
                neighbourPos.add(new Position(newX + 1, newY + 1));
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
