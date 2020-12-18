using System;
using System.Collections.Generic;

namespace csharp
{
  class Program
  {

    private static Dictionary<int, Day> days = new Dictionary<int, Day>
      {
        {1, new Day1()}
      };

    static void Main(string[] args)
    {
      int day = -1;
      if (args.Length == 0)
      {
        day = DateTime.Today.Subtract(new DateTime(2020, 12, 1)).Days + 1;
      }
      else if (!int.TryParse(args[0], out day))
      {
        Console.WriteLine($"Could not parse day {args[1]}");
        return;
      }

      if (!days.ContainsKey(day))
      {
        Console.WriteLine($"Day {day} is not yet configured to run");
        return;
      }

      days[day].run(day);
    }
  }
}
