import java.util.*;
import java.io.*;

public class P6_Keep_on_Truckin {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        List<Integer> motels = new ArrayList<>();
        int[] startingMotels = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000};
        for (int motel: startingMotels) {
            motels.add(motel);
        }

        int a = readInt(), b = readInt(), n = readInt();
        for (int i = 0; i < n; i++) {
            motels.add(readInt());
        }
        Collections.sort(motels);

        long[] numPaths = new long[motels.size()];
        numPaths[0] = 1;
        for (int i = 0; i < numPaths.length; i++) {
            for (int j = 0; j < i; j++) {
                int distance = motels.get(i) - motels.get(j);
                if (a <= distance && distance <= b) {
                    numPaths[i] += numPaths[j];
                }
            }
        }
        System.out.println(numPaths[numPaths.length - 1]);
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
