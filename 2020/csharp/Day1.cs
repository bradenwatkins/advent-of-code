using System.Linq;

namespace csharp
{
  public class Day1 : Day
  {

    internal override int? part1(string rawInput)
    {
      var data = rawInput.Split("\n").Select(x => int.Parse(x));
      var entrySet = data.ToHashSet();
      foreach (var x in data)
      {
        if (entrySet.Contains(2020 - x)) return x * (2020 - x);
      }

      return null;
    }

    internal override int? part2(string rawInput)
    {
      var data = rawInput.Split("\n").Select(x => int.Parse(x));
      var entrySet = data.ToHashSet();
      foreach (var (x, i) in data.Select((x, i) => (x, i)))
      {
        foreach (var y in data.Take(i))
        {
          if (entrySet.Contains(2020 - x - y)) return x * y * (2020 - x - y);
        }
      }

      return null;
    }
  }
}