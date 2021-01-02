import java.util.Scanner;

class Question1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int j = input.nextInt();
        int a = input.nextInt();

        input.nextLine();
        String[] jerseys = new String[j];
        for (int i = 0; i < j; i++) {
            jerseys[i] = input.nextLine();
        }

        String[][] athleteReq = new String[a][2];
        for (int i = 0; i < a; i++) {
            athleteReq[i] = input.nextLine().split(" ");
        }
        input.close();

        int fulfilledReq = 0;
        for (String[] req : athleteReq) {
            int index = Integer.parseInt(req[1]) - 1;
            if (sizeToInt(req[0]) <= sizeToInt(jerseys[index]) && !jerseys[index].equals("X")) {
                fulfilledReq += 1;
                jerseys[index] = "X";
            }
        }
        System.out.println(fulfilledReq);
    }

    private static int sizeToInt(String size) {
        switch (size) {
            case "S":
                return 0;
            case "M":
                return 1;
            case "L":
                return 2;
            default:
                return -1;
        }
    }
}
