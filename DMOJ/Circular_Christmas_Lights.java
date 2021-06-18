import java.util.*;
import java.io.*;

public class Circular_Christmas_Lights {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] lights = new int[n];
        for (int i = 0; i < n; i++) {
            lights[i] = readInt();
        }
        int power_2 = 1;
        while (m > 0) {
            int[] new_lights = new int[n];
            if (m % 2 == 1) {
                for (int i = 0; i < n; i++) {
                    new_lights[i] = lights[i] ^ lights[(i + power_2) % n];
                }
                lights = new_lights;
            }
            m /= 2;
            power_2 *= 2;
        }
        for (int i = 0; i < n; i++) {
            System.out.println(lights[i]);
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
}
