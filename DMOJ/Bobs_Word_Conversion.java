import java.io.*;

public class Bobs_Word_Conversion {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String a = readLine();
        String b = readLine();
        if (a.equals(b)) {
            System.out.println("Yes");
        } else if (a.length() - 1 != b.length()) {
            System.out.println("No");
        } else {
            int a_index = 0;
            int b_index = 0;
            boolean isPossible = true;
            while (b_index < b.length()) {
                if (a.charAt(a_index) != b.charAt(b_index)) {
                    if (a_index == b_index) {
                        a_index += 1;
                    } else {
                        isPossible = false;
                        break;
                    }
                } else {
                    a_index += 1;
                    b_index += 1;
                }
            }
            if (isPossible) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
