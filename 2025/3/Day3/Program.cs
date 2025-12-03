
using System.Numerics;

string filename = "3.txt";
BatteryBankScanner scanner = new(filename);
Console.WriteLine($"{scanner.SumLargestJoltagePart2(12)}");

// var stopwatch = System.Diagnostics.Stopwatch.StartNew();
// for (int i = 1; i < 101; i++)
// {
//     stopwatch.Restart();
//     Console.WriteLine($"{scanner.SumLargestJoltagePart2(i)}");
//     stopwatch.Stop();

//     Console.WriteLine($"{i} execution time: {stopwatch.ElapsedMilliseconds} ms");
// }

class BatterySelection
{
    private static readonly int MAX_BATTERY = 9;
    private readonly int[] onBatteries;

    private int RightIsBiggerIndex { get; set; }
    private bool RightIsBiggerExists { get { return RightIsBiggerIndex <= onBatteries.Length; } }

    public BatterySelection(string batteriesStr)
    {
        int digits = batteriesStr.Length;
        onBatteries = new int[digits];
        RightIsBiggerIndex = digits + 1;

        for (int i = 0; i < digits; i++)
        {
            int battery = batteriesStr[i] - '0';
            SetBattery(i, battery);
        }
    }

    private void SetBattery(int i, int battery)
    {
        onBatteries[i] = battery;
        if (i > 0 && i < RightIsBiggerIndex && onBatteries[i - 1] < onBatteries[i])
        {
            RightIsBiggerIndex = i - 1;
        }
    }

    public void AddNewBattery(int newBattery)
    {
        if (RightIsBiggerExists)
        {
            AddNewBattery(RightIsBiggerIndex, newBattery);
        }
        else if (newBattery > onBatteries[^1])
        {
            SetBattery(onBatteries.Length - 1, newBattery);
        }
    }
    private void AddNewBattery(int indexTurnOff, int newBattery)
    { 
        // re-init so it's set correctly for new data
        if (indexTurnOff <= RightIsBiggerIndex)
        {
            RightIsBiggerIndex = onBatteries.Length + 1;
        }
        for (int i = indexTurnOff; i < onBatteries.Length - 1; i++)
        {
            SetBattery(i, onBatteries[i + 1]);
        }
        SetBattery(onBatteries.Length - 1, newBattery);
    }

    public BigInteger JoltageValue { get { return BigInteger.Parse(string.Join("", onBatteries)); } }
}

class BatteryBank(string batteries)
{
    private readonly string batteries = batteries;

    public int LargestJoltagePart1()
    {
        int largestTensBattery = 0, largestUnitsBattery = 0;
        for (int i = 0; i < batteries.Length; i++)
        {
            int battery = batteries[i] - '0';

            if (battery > largestTensBattery && i < batteries.Length - 1)
            {
                largestTensBattery = battery;
                largestUnitsBattery = batteries[i + 1] - '0';
            }
            else if (battery > largestUnitsBattery)
            {
                largestUnitsBattery = battery;
            }
        }

        return largestTensBattery * 10 + largestUnitsBattery;
    }

    public BigInteger LargestJoltagePart2(int digits)
    {
        // initialise selection with first 12 digits
        BatterySelection selection = new(batteries[..digits]);

        /*
            for each remaining digit

            if any selected digit has a value > than it to the right
            turn off the leftmost digit that has something bigger to the right
            add the new digit to the end

            else...
            if the new digit is higher or equal lowest, add it to the end, turn off lowest leftmost

            and if there's no digit that has something bigger to the right, then the rightmost must be least
        */

        for (int i = digits; i < batteries.Length; i++)
        {
            int battery = batteries[i] - '0';
            selection.AddNewBattery(battery);
        }

        return selection.JoltageValue;
    }
}
class BatteryBankScanner
{
    private readonly List<BatteryBank> batteryBanks;

    public BatteryBankScanner(string filename)
    {
        using StreamReader reader = new(filename);
        string content = reader.ReadToEnd();
        batteryBanks = [.. content.Split('\n').Where(line => line.Length > 0).Select(line => new BatteryBank(line))];
    }

    public int SumLargestJoltagePart1()
    {
        return batteryBanks.Select(bank => bank.LargestJoltagePart1()).Sum();
    }
    public BigInteger SumLargestJoltagePart2(int digits = 12)
    {
        return batteryBanks.Select(bank => bank.LargestJoltagePart2(digits)).Aggregate((acc, x) => acc + x);
    }
}
