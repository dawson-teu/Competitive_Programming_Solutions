import java.util.*;
import java.io.*;

public class Returning_Home {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), s_len = readInt();
        String[] strings = new String[n];
        for (int i = 0; i < n; i++) {
            strings[i] = readLine();
        }
        int[] palindromesA = new int[m];
        int[] palindromesB = new int[m];
        for (int i = 0; i < m; i++) {
            palindromesA[i] = readInt();
            palindromesB[i] = readInt();
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            boolean[][] is_palindrome = new boolean[s_len + 1][s_len + 1];
            for (int j = s_len; j >= 1; j--) {
                for (int k = j; k <= s_len; k++) {
                    boolean cur_char_equal = strings[i].charAt(j - 1) == strings[i].charAt(k - 1);
                    if (j == k) {
                        is_palindrome[j][k] = true;
                    } else if (j == k - 1 && cur_char_equal) {
                        is_palindrome[j][k] = true;
                    } else if (j < s_len && cur_char_equal && is_palindrome[j + 1][k - 1] || k == 1) {
                        is_palindrome[j][k] = true;
                    }
                }
            }

            boolean satisfies_all = true;
            for (int j = 0; j < m; j++) {
                int a = palindromesA[j], b = palindromesB[j];
                if (!is_palindrome[a][b]) {
                    satisfies_all = false;
                    break;
                }
            }
            if (satisfies_all) {
                count += 1;
            }
        }
        System.out.println(count);
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
