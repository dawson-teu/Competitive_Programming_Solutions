import java.util.*;

public class LivestockLineup {
    static String[] cows;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        String[] a = new String[n];
        String[] b = new String[n];
        for (int i = 0; i < n; i++) {
            String line = input.nextLine();
            a[i] = line.split(" ")[0];
            b[i] = line.split(" ")[5];
        }

        cows = new String[]{"Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"};
        Arrays.sort(cows);
        boolean done;
        do {
            boolean correct = true;
            for (int i = 0; i < n; i++) {
                if (Math.abs(indexOf(cows, a[i]) - indexOf(cows, b[i])) != 1) {
                    correct = false;
                    break;
                }
            }
            if (correct) {
                for (String cow : cows) {
                    System.out.println(cow);
                }
                break;
            }
            done = nextPermutation();
        } while (!done);
    }

    public static int indexOf(String[] arr, String elem) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(elem)) {
                return i;
            }
        }
        return -1;
    }

    public static boolean nextPermutation() {
        if (cows.length < 2) {
            return true;
        }
        int a = cows.length - 2;
        while (a >= 0 && cows[a].compareTo(cows[a + 1]) >= 0) {
            a -= 1;
        }
        if (a < 0) {
            return true;
        }

        int b = cows.length - 1;
        while (cows[b].compareTo(cows[a]) <= 0) {
            b -= 1;
        }

        String t = cows[a];
        cows[a] = cows[b];
        cows[b] = t;
        int l = a + 1;
        int r = cows.length - 1;
        while (l < r) {
            t = cows[l];
            cows[l] = cows[r];
            cows[r] = t;
            l += 1;
            r -= 1;
        }
        return false;
    }
}
