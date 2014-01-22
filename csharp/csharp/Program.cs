using System;
using System.Diagnostics;


namespace euler {
	class Problem114 {

		private long[] cache;

		public static void Main(string[] args) {
			new Problem114().Recursive();
		}

		public void Recursive(int m =50, int n = 3) {
			Stopwatch clock = Stopwatch.StartNew();

			cache = new long[m+1];         
			long solutions = F(m, n);     

			clock.Stop();
			Console.WriteLine("The row can be filled in {0} ways ", solutions);
			Console.WriteLine("Solution took {0} ms", clock.Elapsed.TotalMilliseconds);
		}

		private long F(int m, int n) {
			long solutions = 1;                  // default solution count, 1 value for the 'all black' solution?
			if (n > m) return solutions;         // 'all black' is the only solution, block width is larger than the remaining block space.
			if (cache[m] != 0) return cache[m];  // used a cached result if it's available.


			for (int startpos = 0; startpos <= m-n; startpos++) {
				for (int blocklength = n; blocklength <= m-startpos; blocklength++) {                                        
					solutions += F(m - startpos - blocklength-1, n);
				}
			}
			cache[m] = solutions;
			return solutions;
		}
	}
}