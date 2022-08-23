using System;

namespace NISM {
    public class mf {
        public static List<List<int>> createNodeArray(int l) {
            List<int> tempArr = new List<int>();
            List<List<int>> coordArr = new List<List<int>>();
            for (int i = 0; i < l*l; i++) {
                if (i % l == 0) {
                    coordArr.Add(tempArr);
                    tempArr.Clear();
                }
                else {
                    tempArr.Add(i);
                }
            }
            return coordArr;
        }

        public static void Main() {
            Console.WriteLine("> Enter the length of the coordinate plane.");
            Console.Write("> Length :: ");
            string lS = Console.ReadLine();
            int l = Int32.Parse(lS);
            List<List<int>> coordPlane = createNodeArray(l);
            for (int i = 0; i < l; i++) {
                foreach (var node in coordPlane[i]) {
                    Console.Write(" [ {0} ] ", node);
                }
                Console.Write("\n");
            }
        }
    }
}