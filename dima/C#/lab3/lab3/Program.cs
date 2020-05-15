using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Diagnostics;

namespace lab3
{

    internal class Program
    {
        static double sum = 0d;
        
        static void LeftTriangle(object n)
        {
            var left = 0;
            var right = 2.5;
            var nums = (int)n;
            double h = (right - left) / nums;
            sum = 0d;
            for (var i = 0; i <= nums - 1; i++)
            {
                var x = left + i * h;
                sum += f4(x);
            }

            sum = h * sum;
        }
        
        static double f1(double x)
        {
            return Math.Sin(x) * Math.Cos(x * x);
        }

        static double f2(double x)
        {
            return Math.Log(x) * 10 * Math.Cos(x);
        }

        static double f3(double x)
        {
            return Math.Pow(x, x) - 10 * Math.Sin( 5 * x);
        }
        
        static double f4(double x)
        {
            return -1 * x * x  + 5;
        }

        static void Threads(int numThreads)
        {
            ThreadPool.SetMaxThreads(numThreads, 0);
            for (int i = 0; i < numThreads; i++)
            {
                ThreadPool.QueueUserWorkItem(LeftTriangle, 1000);
            }
            Thread.Sleep(300);
            Console.WriteLine(sum);
        }
        
        static void Main(string[] args)
        {
            Threads(Environment.ProcessorCount);
        }
    }
}