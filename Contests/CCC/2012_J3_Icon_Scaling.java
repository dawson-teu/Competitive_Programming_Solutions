import java.util.Scanner;

class Question1 {
    public static void main(String[] args) {
        String[][] icon = {{"*", "x", "*"}, {" ", "x", "x"}, {"*", " ", "*"}};

        Scanner input = new Scanner(System.in);
        int k = input.nextInt();
        input.close();

        for (int i = 0; i < k * 3; i++) {
            for (int j = 0; j < k * 3; j++) {
                System.out.print(icon[i / k][j / k]);
            }
            System.out.println();
        }
    }
}
