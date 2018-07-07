using System;
using System.Threading;

namespace part1
{
    class Program
    {
        static int countGarbage(string line){
            int ret = 0;
            bool inGarbage = false;
            int start = 0;
            for (int i=0; i < line.Length; i++){
                if (line[i] == '<' && !inGarbage){
                    start = i;
                    inGarbage = true;
                }
                if (line[i] == '>' && inGarbage){
                    ret += i-start-1;
                    inGarbage = false;
                }
            }
            return ret;
        }

        static void solve(string line){
            // Remove those cancelation characters
            while(line.IndexOf("!") != -1){
                int idx = line.IndexOf("!");
                line = line.Substring(0, idx) + line.Substring(idx+2, line.Length - 2 - idx);
            }
            Console.Out.WriteLine(countGarbage(line));
        }

        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllText("input.txt").Split(
                new[] { System.Environment.NewLine },
                StringSplitOptions.None
            );

            foreach (string line in lines){
                solve(line);
            }
        }
    }
}
