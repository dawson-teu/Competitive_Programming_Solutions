import java.util.*;
import java.io.*;

public class C2_P1_Koala_Konundrum {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        String str = readLine();
        Map<String, Integer> letterCount = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String letter = str.substring(i, i + 1);
            if (letterCount.containsKey(letter)) {
                letterCount.put(letter, letterCount.get(letter) + 1);
            } else {
                letterCount.put(letter, 1);
            }
        }
        int oddLetterCount = 0;
        for (int val: letterCount.values()) {
            if (val % 2 == 1) {
                oddLetterCount += 1;
            }
        }
        System.out.println(Math.max(1, oddLetterCount));
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
