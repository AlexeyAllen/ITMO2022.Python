using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace DgemmCalc
{
    internal class Program
    {
        static void Main(string[] args)
        {
            DgemCalc calc = new DgemCalc();
            var matrix_a_double = calc.loadMatrix("matrix_a_float.csv");
            var matrix_b_double = calc.loadMatrix("matrix_b_float.csv");
            var matrix_c_double = calc.loadMatrix("matrix_c_float.csv");


            Console.WriteLine("Введите значение alpha");
            double alpha = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Введите значение betta");
            double betta = Convert.ToDouble(Console.ReadLine());


            var watch = System.Diagnostics.Stopwatch.StartNew();
            var resultedMatrix = calc.dgemm_calcs(matrix_a_double, matrix_b_double, matrix_c_double, alpha, betta);
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine(elapsedMs);

            var watch2 = System.Diagnostics.Stopwatch.StartNew();
            var resultedMatrix2 = calc.dgemm_calcs_multithreading(matrix_a_double, matrix_b_double, matrix_c_double, alpha, betta);
            watch.Stop();
            var elapsedMs2 = watch.ElapsedMilliseconds;
            Console.WriteLine(elapsedMs2);
        }
    }
}
