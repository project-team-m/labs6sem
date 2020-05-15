using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Diagnostics;

namespace lab4
{
    class Program
    {
        static bool is_Simple(int digit)
        {
            for (int i = 2; i < digit; i++)
            {
                if (digit % i == 0)
                {
                    return false;
                }
            }

            return true;
        }
        
        static int[] comb_gen(int digit)
        {
            int[] mass = new int[digit.ToString().Length];
            mass[0] = digit;
            for (int i = 1; i < digit.ToString().Length; i++)
            {
                if (mass[i - 1] > 10)
                {
                    if (mass[i - 1].ToString()[1] != '0')
                    {
                        mass[i] = Convert.ToInt32(mass[i - 1].ToString().Remove(0, 1) + 
                                                  mass[i - 1].ToString().Remove(1));
                    }
                }
            }
            return mass;
        }

        static bool all_simple(int digit)
        {
            foreach (var i in comb_gen(digit))
            {
                if (!is_Simple(i))
                {
                    return false;
                }
            }

            return true;
        }

        static void quest_without_paral(int border)
        {
            List<int> digits = new List<int>();
            var timer = Stopwatch.StartNew();
            for (int i = 2; i <= border; i++)
            {
                if (all_simple(i))
                {
                    digits.Add(i);
                }
            }
            timer.Stop();
            Console.WriteLine("Ended for " + timer.ElapsedMilliseconds);
            Console.WriteLine();
        }
        
        static void quest(int border)
        {
            List<int> digits = new List<int>();
            var timer = Stopwatch.StartNew();
            Parallel.For(2, border + 1,
                new ParallelOptions { MaxDegreeOfParallelism = 8 },
                (i) =>
            {
                if (all_simple(i))
                {
                    digits.Add(i);
                }
            });
            timer.Stop();
            Console.WriteLine("Ended for " + timer.ElapsedMilliseconds);
            
            Console.Write("Sequence: ");
            foreach (var i in digits)
            {
                Console.Write(i + " ");
            }
        }
        
        static void Main(string[] args)
        {
            var border = 50000;
            quest_without_paral(border);
            quest(border);
 
        }
    }
}