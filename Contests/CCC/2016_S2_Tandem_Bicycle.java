import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class S2_Tandem_Bicycle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int type = input.nextInt();
        int n = input.nextInt();
        List<Integer> dmoj = new ArrayList<>();
        List<Integer> peg = new ArrayList<>();
        input.nextLine();
        String[] dmojString = input.nextLine().split(" ");
        String[] pegString = input.nextLine().split(" ");
        for (String elem : dmojString) {
            dmoj.add(Integer.parseInt(elem));
        }
        for (String elem : pegString) {
            peg.add(Integer.parseInt(elem));
        }
        input.close();

        int total = 0;
        if (type == 1) {
            for (int i = 0; i < n; i++) {
                int maxDmojElem = Collections.max(dmoj);
                int maxPegElem = Collections.max(peg);
                total += Math.max(maxDmojElem, maxPegElem);
                dmoj.remove((Integer) maxDmojElem);
                peg.remove((Integer) maxPegElem);
            }
        } else if (type == 2) {
            for (int i = 0; i < n; i++) {
                int maxDmojElem = Collections.max(dmoj);
                int minPegElem = Collections.min(peg);
                total += Math.max(maxDmojElem, minPegElem);
                dmoj.remove((Integer) maxDmojElem);
                peg.remove((Integer) minPegElem);
            }
        }
        System.out.println(total);
    }
}
