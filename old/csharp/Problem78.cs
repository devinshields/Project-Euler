using System;
using System.Diagnostics;
using System.Collections.Generic;

namespace euler
{
    class Problem78
    {

        //public static void Main(string[] args)
        //{
        //    new Problem78().Generating();
        //}

        public void Generating()
        {
            Stopwatch clock = Stopwatch.StartNew();

            List<int> p = new List<int>();
            p.Add(1);

            int n = 1;
            while (true)
            {
                int i = 0;
                int penta = 1;
                p.Add(0);

                while (penta <= n)
                {
                    int sign = (i % 4 > 1) ? -1 : 1;
                    p[n] += sign * p[n - penta];
                    p[n] %= 1000000;
                    i++;

                    int j = (i % 2 == 0) ? i / 2 + 1 : -(i / 2 + 1);
                    penta = j * (3 * j - 1) / 2;
                }

                if (p[n] == 0) break;
                n++;
            }

            clock.Stop();
            Console.WriteLine("The least value of n for which p(n) is divisible by one million is {0}", n);
            Console.WriteLine("Solution took {0} ms", clock.Elapsed.TotalMilliseconds);
        }
    }
}