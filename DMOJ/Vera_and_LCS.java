import java.io.*;
import java.util.*;

public class Vera_and_LCS {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        String a = readLine();
        int[] letterFreq = new int[26];
        for (int i = 0; i < n; i++) {
            letterFreq[a.charAt(i) - 'a'] += 1;
        }
        char minLetter = ' ';
        int minFreq = (int) 1e9;
        for (int i = 0; i < 26; i++) {
            if (letterFreq[i] < minFreq) {
                minFreq = letterFreq[i];
                minLetter = (char) ('a' + i);
            }
        }
        if (k > n || k < minFreq) {
            System.out.println("WRONGANSWER");
        } else {
            int lettersToCopy = k - minFreq;
            StringBuilder output = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (lettersToCopy > 0 && minLetter != a.charAt(i)) {
                    output.append(a.charAt(i));
                    lettersToCopy -= 1;
                } else {
                    output.append(minLetter);
                }
            }
            System.out.println(output);
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