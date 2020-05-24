using System;
using System.Diagnostics;
using System.Threading;

namespace LAB5
{
    class Program
    {
        static void Main(string[] args)
        {
            unOptimized();
        }

        static void unOptimized()
        {
            long start = Stopwatch.GetTimestamp();
            int[,] ad = new int[2,2];
            int res = 0;

            for (int j = 500000000; j > 0; j--)
            {
                ad[0,0]++;
                ad[0,0]++;
            }

            ad[1,1] = ad[0,0];

            long exTime = Stopwatch.GetTimestamp() - start;

            Console.WriteLine(ad[0,0]);
            Console.WriteLine("Time of execution: " + exTime + " ns");
        }

    }
}

