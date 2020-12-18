using System;
using System.Diagnostics;
using System.IO;

namespace csharp
{
  public abstract class Day
  {
    internal virtual int? part1(string rawInput) => null;

    internal virtual int? part2(string rawInput) => null;

    public void run(int day)
    {
      Console.WriteLine($"AOC 2020 Day {day:00}");
      var filename = $"../input/{day:00}.txt";
      var rawInput = File.ReadAllText(filename);
      Console.WriteLine($"Loaded puzzle input from {filename}");

      Console.WriteLine("Running Part 1");
      var sw = Stopwatch.StartNew();
      Console.WriteLine($"Output: {part1(rawInput)}");
      sw.Stop();
      Console.WriteLine($"Took: {formatRuntime(sw.ElapsedMilliseconds)}\n");

      Console.WriteLine("Running Part 2");
      sw = Stopwatch.StartNew();
      Console.WriteLine($"Output: {part2(rawInput)}");
      sw.Stop();
      Console.WriteLine($"Took: {formatRuntime(sw.ElapsedMilliseconds)}\n");
    }

    private static string formatRuntime(long ms)
    {
      if (ms < 1000)
      {
        return $"{ms} ms";
      }

      var sec = ms / 1000;
      if (sec < 60)
      {
        return $"{sec:.00} sec";
      }

      var min = sec / 60;
      return $"{min:.00} min";
    }
  }
}