import java.util.Scanner;

public class Array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        System.out.println("Digite 10 números inteiros:");

        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        System.out.println("\nNúmeros digitados:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Número " + (i + 1) + ": " + numeros[i]);
        }

        System.out.print("Qual número deseja encontrar? ");
        int numeroProcurado = scanner.nextInt();

        boolean encontrado = false;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == numeroProcurado) {
                System.out.println("Número " + numeroProcurado + " encontrado na posição: " + (i + 1));
                encontrado = true;
                break;
            }
        }
        if (!encontrado) {
            System.out.println("Número " + numeroProcurado + " não encontrado.");
        }

        scanner.close();
    }
}
