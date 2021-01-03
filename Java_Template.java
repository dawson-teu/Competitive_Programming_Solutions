import java.util.*;
import java.io.*;

public class Java_Template {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        /*
         For fast input from a text file
         br = new BufferedReader(new FileReader("./src/put_file_here.txt"));
         System.out.println(br.readLine());
         br.close();
         */

         pr.println("Hello, World!");
         long l = readLong();
         int i = readInt();
         double d = readDouble();
         char c = readCharacter();
         String s = readLine();
         System.out.println(l + i + d);
         System.out.println(c + s);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static double readDouble() throws IOException {
        return Double.parseDouble(next());
    }

    static char readCharacter() throws IOException {
        return next().charAt(0);
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
