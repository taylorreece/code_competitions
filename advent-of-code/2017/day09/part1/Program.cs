using System;
using System.Threading;

namespace part1
{
    class Program
    {
        static int findTotal(string line, int layer){
            int total = layer;
            if (line.Length == 0){
                return 0;
            } else if (line.Length == 2){
                return total;
            } else {
                int bracketLayer = 1;
                int start=1;
                for (int i=2; i < line.Length; i++){
                    if (line[i] == '{'){
                        if (bracketLayer == 0){
                            start = i;
                        }
                        bracketLayer++;
                    } else {
                        bracketLayer--;
                        if (bracketLayer == 0){
                            total += findTotal(line.Substring(start, i-start+1), layer+1);
                        }
                    }
                }
            }
            return total;
        }

        static string removeGarbage(string line){
            string ret_line = "";
            int in_garbage = 0;
            for (int i=0; i < line.Length; i++){
                if (line[i] == '<') {
                    if (in_garbage == 0){
                        in_garbage++;
                    }
                } else if (line[i] == '>') {
                    if (in_garbage == 1) {
                        in_garbage--;
                    }
                } else if (in_garbage == 0) {
                    ret_line += line[i];
                }
            }
            return ret_line;
        }

        static void solve(string line){
            // Remove those cancelation characters
            while(line.IndexOf("!") != -1){
                int idx = line.IndexOf("!");
                line = line.Substring(0, idx) + line.Substring(idx+2, line.Length - 2 - idx);
            }

            // Make up a string without anything but {, }, <, >
            string newLine = "";
            for (int i=0; i < line.Length; i++) {
                if (line[i] == '{' || line[i] == '}' || line[i] == '<' || line[i] == '>') {
                    newLine += line[i];
                }
            }
            newLine = removeGarbage(newLine);
            Console.Out.WriteLine(findTotal(newLine, 1));
            // Console.Out.WriteLine(findTotal(newLine, 1));
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
