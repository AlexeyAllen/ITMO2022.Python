package DgemmCalc;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DgemmCalc {
    public double[][] loadMatrix(String fileName) {

        String pathName = "C:\\Users\\aqml\\IdeaProjects\\DgemCalc\\Data\\";
        List<String[]> rowList = new ArrayList<String[]>();
        try (BufferedReader br = new BufferedReader(new FileReader(pathName + fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] lineItems = line.split(",");
                rowList.add(lineItems);
            }
        } catch (Exception e) {
            System.out.println("some exception");
        }
        String[][] matrix = new String[rowList.size()][];
        for (int i = 0; i < rowList.size(); i++) {
            String[] row = rowList.get(i);
            matrix[i] = row;
        }

        int tableStringLength = matrix.length;
        double[][] matrixDouble = new double[tableStringLength][tableStringLength];
        for (int i = 0; i < tableStringLength; i++) {
            for (int j = 0; j < tableStringLength; j++) {
                matrixDouble[i][j] = Double.parseDouble(matrix[i][j]);
            }
        }
        return matrixDouble;
    }

    public double[][] matrices_multiply(double[][] matrix_a, double[][] matrix_b) {
        int matrixSize = matrix_a.length;
        double[][] multipliedArray = new double[matrixSize][matrixSize];

        for (int row = 0; row < matrixSize; row++) {
            for (int col = 0; col < matrixSize; col++) {
                multipliedArray[row][col] = 0;
                for (int i = 0; i < matrixSize; i++) {
                    multipliedArray[row][col] += matrix_a[row][i] * matrix_b[i][col];
                }
            }
        }
        return multipliedArray;
    }

    public double[][] multiply_matrix_by_scalar(double[][] matrix_a, double scalar) {
        int matrixSize = matrix_a.length;
        double[][] multipliedArray = new double[matrixSize][matrixSize];

        for (int row = 0; row < matrixSize; row++) {
            for (int col = 0; col < matrixSize; col++) {
                multipliedArray[row][col] = 0;
                for (int i = 0; i < matrixSize; i++) {
                    multipliedArray[row][col] *= scalar;
                }
            }
        }
        return matrix_a;
    }

    public double[][] matrices_sum(double[][] matrix_a, double[][] matrix_b) {
        int matrixSize = matrix_a.length;
        double[][] sumArray = new double[matrixSize][matrixSize];

        int i, j;
        for (i = 0; i < matrixSize; i++)
            for (j = 0; j < matrixSize; j++)
                sumArray[i][j] = matrix_a[i][j] + matrix_b[i][j];

        return sumArray;
    }

    public double[][] dgemm_calcs(double[][] matrix_a, double[][] matrix_b, double[][] matrix_c, double alpha, double betta) {
        double[][] matrix_ab = matrices_multiply(matrix_a, matrix_b);
        double[][] matrix_a_b_alpha = multiply_matrix_by_scalar(matrix_ab, alpha);
        double[][] matrix_c_betta = multiply_matrix_by_scalar(matrix_ab, betta);
        double[][] matrix_a_b_alpha_added_matrix_c_betta = matrices_sum(matrix_a_b_alpha, matrix_c_betta);

//        int rowLength = matrix_a_b_alpha_added_matrix_c_betta.length;
//        int colLength = matrix_a_b_alpha_added_matrix_c_betta.length;
//
//        for (int i = 0; i < rowLength; i++) {
//            for (int j = 0; j < colLength; j++) {
//                System.out.println(matrix_a_b_alpha_added_matrix_c_betta[i][j]);
//            }
//            System.out.println();
//        }
        return matrix_a_b_alpha_added_matrix_c_betta;
    }

    public double[][] dgemm_calcs_multithreading(double[][] matrix_a, double[][] matrix_b, double[][] matrix_c,
                                                 double alpha, double betta) throws InterruptedException {

        Thread[] ts = new Thread[4];
        double[][] matrix_ab = null;

        for (int i = 0; i < ts.length; i++) {
            ts[i] = new Thread();
            matrix_ab = matrices_multiply(matrix_a, matrix_b);
            ts[i].start();
        }
        for (int i = 0; i < ts.length; i++) {
            ts[i].join();
        }


        //double[,] matrix_ab = matrices_multiply(matrix_a, matrix_b);
        double[][] matrix_a_b_alpha = multiply_matrix_by_scalar(matrix_ab, alpha);
        double[][] matrix_c_betta = multiply_matrix_by_scalar(matrix_ab, betta);
        double[][] matrix_a_b_alpha_added_matrix_c_betta = matrices_sum(matrix_a_b_alpha, matrix_c_betta);

//        int rowLength = matrix_a_b_alpha_added_matrix_c_betta.length;
//        int colLength = matrix_a_b_alpha_added_matrix_c_betta.length;
//
//        for (int i = 0; i < rowLength; i++) {
//            for (int j = 0; j < colLength; j++) {
//                System.out.println(matrix_a_b_alpha_added_matrix_c_betta[i][j]);
//            }
//            System.out.println();
//        }

        return matrix_a_b_alpha_added_matrix_c_betta;
    }
}

