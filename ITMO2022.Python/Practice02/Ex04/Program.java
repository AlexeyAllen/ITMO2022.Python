package DgemmCalc;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) throws InterruptedException {
        DgemmCalc calc = new DgemmCalc();
        double[][] matrix_a_double = calc.loadMatrix("matrix_a_float.csv");
        double[][] matrix_b_double = calc.loadMatrix("matrix_b_float.csv");
        var matrix_c_double = calc.loadMatrix("matrix_c_float.csv");

        calc.matrices_multiply(matrix_a_double, matrix_b_double);

        Scanner sc= new Scanner(System.in);
        System.out.println("Введите значение alpha");
        double alpha = Double.parseDouble(sc.nextLine());
        System.out.println("Введите значение betta");
        double betta = Double.parseDouble(sc.nextLine());


        long startTime = System.currentTimeMillis();
        var resultedMatrix = calc.dgemm_calcs(matrix_a_double, matrix_b_double, matrix_c_double, alpha, betta);
        long endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime);

        startTime = System.currentTimeMillis();
        var resultedMatrix2 = calc.dgemm_calcs_multithreading(matrix_a_double, matrix_b_double, matrix_c_double, alpha, betta);
        endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime);

    }
}