import java.util.*;

public class Dec_B2_Where_Am_I {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        String road = input.nextLine();

        Set<String> uniqueSeq = new HashSet<>();
        for (int i = 1; i < n + 1; i++) {
            uniqueSeq.clear();
            boolean unique = true;
            for (int j = 0; j < n - i + 1; j++) {
                String roadSeq = road.substring(j, j + i);
                if (uniqueSeq.contains(roadSeq)) {
                    unique = false;
                    break;
                } else {
                    uniqueSeq.add(roadSeq);
                }
            }
            if (unique) {
                System.out.println(i);
                break;
            }
        }
    }
}
