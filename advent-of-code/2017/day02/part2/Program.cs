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
                string[] string_split = line.Split(new[] {'\t', ' '}, StringSplitOptions.None);
                if (line.Length > 2) {
                    foreach(string num in string_split){
                        vals.Add(Int32.Parse(num));
                    }
                    for (int i = 0; i < vals.Count; i++){
                        for (int j = 0; j < vals.Count; j++){
                            if (i != j) {
                                float division = (float)vals[i] / (float)vals[j];
                                if (division == (int)division){
                                    checkSum += (int)division;
                                }
                            }
                        }
                    }
                }
            }
            Console.Out.WriteLine(checkSum);
        }
    }
}
