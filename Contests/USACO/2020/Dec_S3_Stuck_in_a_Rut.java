import java.util.*;
import java.io.*;

public class Dec_S3_Stuck_in_a_Rut {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        List<Point> eastCows = new ArrayList<>();
        List<Point> northCows = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char dir = readCharacter();
            int x = readInt(), y = readInt();
            if (dir == 'E') {
                eastCows.add(new Point(x, y, i));
            } else {
                northCows.add(new Point(x, y, i));
            }
        }
        eastCows.sort(Comparator.comparingInt(p -> p.y));
        northCows.sort(Comparator.comparingInt(p -> p.x));
        boolean[] stoppedCows = new boolean[n];
        int[] numStoppedCows = new int[n];
        for (Point eCow: eastCows) {
            for (Point nCow: northCows) {
                if (!stoppedCows[eCow.n] && !stoppedCows[nCow.n]) {
                    if (eCow.x < nCow.x && nCow.y < eCow.y) {
                        if (nCow.x - eCow.x < eCow.y - nCow.y) {
                            stoppedCows[nCow.n] = true;
                            numStoppedCows[eCow.n] += numStoppedCows[nCow.n] + 1;
                        } else if (nCow.x - eCow.x > eCow.y - nCow.y) {
                            stoppedCows[eCow.n] = true;
                            numStoppedCows[nCow.n] += numStoppedCows[eCow.n] + 1;
                        }
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(numStoppedCows[i]);
        }
    }

    static class Point {
        final int x;
        final int y;
        final int n;
        public Point(int x, int y, int n) {
            this.x = x;
            this.y = y;
            this.n = n;
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

    static char readCharacter() throws IOException {
        return next().charAt(0);
    }
}
