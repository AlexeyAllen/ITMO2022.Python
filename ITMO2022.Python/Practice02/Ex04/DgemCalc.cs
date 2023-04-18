using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace DgemmCalc
{
    internal class DgemCalc
    {
        public dynamic loadMatrix(string fileName)
        {
            Environment.CurrentDirectory = @"C:\Users\aqml\source\repos\ITMO2022\DgemmCalc\Data\";
            string filePath = Path.Combine(Directory.GetCurrentDirectory(), fileName);

            StreamReader sr = new StreamReader(filePath);

            string[,] data = new string[100, 100];
            string line; string temp;
            string[] mass_t;
            int i = 0, j = 0, m = 0;
            while (!sr.EndOfStream)
            {
                j = 0;
                line = sr.ReadLine();
                mass_t = line.Split(',');
                for (i=m; j < mass_t.Length; j++)
                {
                    temp = mass_t[j];
                    data[i, j] = temp;
                }
                m++;
            }

            int matrixSize = data.GetLength(0);
            double[,] convertedArray = new double[matrixSize, matrixSize];
            Thread.CurrentThread.CurrentCulture = new CultureInfo("en-GB");

            for (int k = 0; k < data.GetLength(0); k++)
            {
                for (int l = 0; l < data.GetLength(1); l++)
                {
                    double number;

                    bool ok = double.TryParse(data[k, l], out number);

                    if (ok)
                    {
                        convertedArray[k, l] = number;
                    }
                    else
                    {
                        convertedArray[k, l] = 0;
                    }
                }
            }

            return convertedArray;
        }


        public dynamic matrices_multiply(double[,] matrix_a, double[,] matrix_b)
        {
            int matrixSize = matrix_a.GetLength(0);
            double[,] multipliedArray = new double[matrixSize, matrixSize];

            for (int row = 0; row < matrixSize; row++)
            {
                for (int col = 0; col < matrixSize; col++)
                {
                    multipliedArray[row, col] = 0;
                    for (int i = 0; i < matrixSize; i++)
                    {
                        multipliedArray[row, col] += matrix_a[row, i] * matrix_b[i, col];
                    }
                }
            }

            return multipliedArray;
        }

        public dynamic multiply_matrix_by_scalar(double[,] matrix_a, double scalar)
        {
            int matrixSize = matrix_a.GetLength(0);
            double[,] multipliedArray = new double[matrixSize, matrixSize];

            for (int row = 0; row < matrixSize; row++)
            {
                for (int col = 0; col < matrixSize; col++)
                {
                    multipliedArray[row, col] = 0;
                    for (int i = 0; i < matrixSize; i++)
                    {
                        multipliedArray[row, col] *= scalar;
                    }
                }
            }

            return matrix_a;
        }

        public dynamic matrices_sum(double[,] matrix_a, double[,] matrix_b)
        {
            int matrixSize = matrix_a.GetLength(0);
            double[,] sumArray = new double[matrixSize, matrixSize];

            int i, j;
            for (i = 0; i < matrixSize; i++)
                for (j = 0; j < matrixSize; j++)
                    sumArray[i, j] = matrix_a[i, j] + matrix_b[i, j];

            return sumArray;
        }

        public dynamic dgemm_calcs(double[,] matrix_a, double[,] matrix_b, double[,] matrix_c, double alpha, double betta)
        {
            double[,] matrix_ab = matrices_multiply(matrix_a, matrix_b);
            double[,] matrix_a_b_alpha = multiply_matrix_by_scalar(matrix_ab, alpha);
            double[,] matrix_c_betta = multiply_matrix_by_scalar(matrix_ab, betta);
            double[,] matrix_a_b_alpha_added_matrix_c_betta = matrices_sum(matrix_a_b_alpha, matrix_c_betta);

            int rowLength = matrix_a_b_alpha_added_matrix_c_betta.GetLength(0);
            int colLength = matrix_a_b_alpha_added_matrix_c_betta.GetLength(1);

            //for (int i = 0; i < rowLength; i++)
            //{
            //    for (int j = 0; j < colLength; j++)
            //    {
            //        Console.Write(string.Format("{0} ", matrix_a_b_alpha_added_matrix_c_betta[i, j]));
            //    }
            //    Console.Write(Environment.NewLine + Environment.NewLine);
            //}
            //Console.ReadLine();

            return matrix_a_b_alpha_added_matrix_c_betta;
        }

        public dynamic dgemm_calcs_multithreading(double[,] matrix_a, double[,] matrix_b, double[,] matrix_c, double alpha, double betta)
        {
            Thread[] ts = new Thread[4];
            double[,] matrix_ab = null;

            for (int i = 0; i < ts.Length; i++)
            {
                ts[i] = new Thread(() => { matrix_ab = matrices_multiply(matrix_a, matrix_b); });
                ts[i].Start();
            }
            for (int i = 0; i < 4; i++)
            {
                ts[i].Join();
            }

            //double[,] matrix_ab = matrices_multiply(matrix_a, matrix_b);
            double[,] matrix_a_b_alpha = multiply_matrix_by_scalar(matrix_ab, alpha);
            double[,] matrix_c_betta = multiply_matrix_by_scalar(matrix_ab, betta);
            double[,] matrix_a_b_alpha_added_matrix_c_betta = matrices_sum(matrix_a_b_alpha, matrix_c_betta);

            int rowLength = matrix_a_b_alpha_added_matrix_c_betta.GetLength(0);
            int colLength = matrix_a_b_alpha_added_matrix_c_betta.GetLength(1);

            //for (int i = 0; i < rowLength; i++)
            //{
            //    for (int j = 0; j < colLength; j++)
            //    {
            //        Console.Write(string.Format("{0} ", matrix_a_b_alpha_added_matrix_c_betta[i, j]));
            //    }
            //    Console.Write(Environment.NewLine + Environment.NewLine);
            //}
            //Console.ReadLine();

            return matrix_a_b_alpha_added_matrix_c_betta;
        }

    }
}
