using System;
using System.Collections.Generic;
using System.Linq;

namespace part1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllText("input.txt").Split(
                new[] { System.Environment.NewLine },
                StringSplitOptions.None
            );
            int checkSum = 0;
            foreach(string line in lines){
                List<int> vals = new List<int>();
                string[] string_split = line.Split('\t', StringSplitOptions.None);
                if (line.Length > 2) {
                    foreach(string num in string_split){
                        vals.Add(Int32.Parse(num));
                    }
                    checkSum += vals.Max() - vals.Min();
                }
            }
            Console.Out.WriteLine(checkSum);
        }
    }
}
