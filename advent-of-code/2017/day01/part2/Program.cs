using System;

namespace day01
{
    class Program
    {
        static int computeTotal(string text) {
            int total = 0;
            for(int i = 0; i < text.Length/2; i++){
                if (text[i] == text[i + text.Length/2]) {
                  total += (int)Char.GetNumericValue(text[i]);
                }
            }
            return total*2;
        }

        static void Main(string[] args)
        {
            string text = System.IO.File.ReadAllText("input.txt");
            // Console.Out.WriteLine(computeTotal("1212"));
            // Console.Out.WriteLine(computeTotal("1221"));
            // Console.Out.WriteLine(computeTotal("123425"));
            // Console.Out.WriteLine(computeTotal("123123"));
            // Console.Out.WriteLine(computeTotal("12131415"));
            Console.Out.WriteLine(computeTotal(text.Replace(System.Environment.NewLine, "")));
        }
    }
}
