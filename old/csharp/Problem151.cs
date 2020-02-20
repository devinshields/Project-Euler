using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEulerCSharp
{
    class Problem151
    {
        public static void Main(string[] args)
        {
            var sw = new Stopwatch();
            sw.Start();

            var res = Enumerable.Range(0, 1000000000).AsParallel().Select(i => (new Envelope()).RunSliceSimulation());
            Console.WriteLine(res.Average());

            sw.Stop();
            Console.WriteLine("Elapsed : {0}", sw.Elapsed);

            



            Console.WriteLine("Hello, Euler 151!");
        }

        class Envelope
        {
            readonly Random _randomIndexGenerator = new Random();
            readonly Dictionary<int, List<int>> _sliceMapper = new Dictionary<int, List<int>>()
            {
                { 1, new List<int>()},
                { 2, new List<int>(new []{1})},
                { 4, new List<int>(new []{2, 1})},
                { 8, new List<int>(new []{4, 2, 1})},
                { 16, new List<int>(new []{8, 4, 2, 1})}
            };
            List<int> _slices = new List<int>() { 16 };

            void UpdateRandomSlice()
            {
                // pick, remove and update the slices list
                var ind = _randomIndexGenerator.Next(_slices.Count);
                var selected = _slices[ind];
                _slices.RemoveAt(ind);
                _slices = _slices.Concat(_sliceMapper[selected]).ToList();
                //Console.WriteLine(this);
            }

            public int RunSliceSimulation()
            {
                var singletonCount = 0;
                while (_slices.Count > 0)
                {
                    UpdateRandomSlice();
                    singletonCount += _slices.Count == 1 ? 1 : 0;
                }
                return singletonCount - 1;
            }

            public override string ToString()
            {
                return String.Join(", ", _slices.Select(i => i.ToString()));
            }
        }
    }
}
