import java.util.*;
import java.io.*;

public class P2_Conditional_Contracts {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        Map<Integer, Integer> widthNum = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int width = readInt();
            if (widthNum.containsKey(width)) {
                widthNum.put(width, widthNum.get(width) + 1);
            } else {
                widthNum.put(width, 1);
            }
        }
        List<Integer> numActors = new ArrayList<>(widthNum.values());
        Collections.sort(numActors);
        if (numActors.size() == 1) {
            System.out.println(numActors.get(0));
        } else {
            int output = numActors.get(numActors.size() - 1) + numActors.get(numActors.size() - 2);
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
}
