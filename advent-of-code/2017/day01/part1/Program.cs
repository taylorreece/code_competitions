using System;

namespace day01
{
    class Program
    {
        static int computeTotal(string text) {
            text = text + text[0]; // Account for line-wrap
            int total = 0;
            for(int i = 0; i < text.Length-1; i++){
                if (text[i] == text[i+1]) {
                  total += (int)Char.GetNumericValue(text[i]);
                }
            }
            return total;
        }

        static void Main(string[] args)
        {
            string text = System.IO.File.ReadAllText("input.txt");
            Console.Out.WriteLine(computeTotal(text.Replace(System.Environment.NewLine, "")));
        }
    }
}
