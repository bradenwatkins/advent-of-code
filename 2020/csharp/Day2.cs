using System.Linq;

namespace csharp
{
  public class Day2 : Day
  {

    internal override int? part1(string rawInput)
    {
      return rawInput.Split("\n")
                     .Select(x => x.Split(" "))
                     .Aggregate(0, (total, line) =>
                     {
                       var counts = line[0].Split("-").Select(x => int.Parse(x)).ToList();
                       var letter = line[1][0];
                       var password = line[2];
                       var actual = password.Count(x => x == letter);
                       if (counts[0] <= actual && actual <= counts[1])
                         total++;
                       return total;
                     });
    }

    internal override int? part2(string rawInput)
    {
      return rawInput.Split("\n")
                     .Select(x => x.Split(" "))
                     .Aggregate(0, (total, line) =>
                      {
                        var indices = line[0].Split("-").Select(x => int.Parse(x) - 1).ToList();
                        var i = indices[0];
                        var j = indices[1];
                        var letter = line[1][0];
                        var password = line[2];
                        var actual = password.Count(x => x == letter);
                        if ((password[i] == letter && password[j] != letter) 
                          ||(password[i] != letter && password[j] == letter))
                          total++;
                        return total;
                      });
    }
  }
}