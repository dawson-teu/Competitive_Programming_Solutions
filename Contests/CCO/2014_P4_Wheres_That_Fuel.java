import java.util.*;
import java.io.*;

public class P4_Wheres_That_Fuel {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), p = readInt();
        List<Pair> planets = new ArrayList<>();
        Pair startingPlanet = new Pair(0, 0);
        for (int i = 0; i < n; i++) {
            int a = readInt();
            int b = readInt();
            if (i == p - 1) {
                startingPlanet = new Pair(a, b);
                continue;
            }
            if (a >= b) {
                planets.add(new Pair(a, b));
            }
        }

        planets.sort(Comparator.comparingInt(k -> k.num2));
        int totalFuel = startingPlanet.num1;
        int totalPlanets = 1;
        for (Pair planet: planets) {
            totalFuel -= planet.num2;
            if (totalFuel < 0) {
                totalFuel += planet.num2;
                break;
            }
            totalFuel += planet.num1;
            totalPlanets += 1;
        }
        System.out.println(totalFuel);
        System.out.println(totalPlanets);
    }

    static class Pair {
        public final int num1;
        public final int num2;

        public Pair(int num1, int num2) {
            this.num1 = num1;
            this.num2 = num2;
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
