
using System.Numerics;

string filename = "3.txt";

// post-submission update:
//   decided I didn't like all the array shuffling, wanted to try a LinkedList implementation
//   of the BatterySelection class
//
//   seems the performance slightly worse for digits = 12 (pointer juggling I guess)
//   but if you set digits = 45, then it's about half the time

bool useLinkedList = true;
int digits = 12;

// useLinkedList = true, digits = 12, 100 loops = 239.3272 ms
// useLinkedList = false, digits = 12, 100 loops = 155.1784 ms

// useLinkedList = true, digits = 45, 100 loops = 182.3002 ms
// useLinkedList = false, digits = 45, 100 loops = 358.6222 ms

BatteryBankScanner scanner = new(filename, useLinkedList);

var stopwatch = System.Diagnostics.Stopwatch.StartNew();
stopwatch.Restart();
for (int i = 0; i < 100; i++)
{
    Console.WriteLine($"{scanner.SumLargestJoltagePart2(digits)}");
}
stopwatch.Stop();
Console.WriteLine($"execution time: {stopwatch.Elapsed.TotalMilliseconds} ms");

abstract class BatterySelection {
    public abstract void AddNewBattery(int newBattery);
    public abstract BigInteger JoltageValue {get;}
}

class LinkedListBatterySelection: BatterySelection
{
    private readonly LinkedList<int> onBatteries = new();
    private readonly LinkedList<LinkedListNode<int>> rightIsBiggerNodes = new();

    public LinkedListBatterySelection(string batteriesStr)
    {
        int digits = batteriesStr.Length;

        for (int i = 0; i < digits; i++)
        {
            int battery = batteriesStr[i] - '0';
            var node = onBatteries.AddLast(battery);

            if (i < digits - 1 && batteriesStr[i] < batteriesStr[i + 1])
            {
                rightIsBiggerNodes.AddLast(node);
            }
        }
    }

    public override void AddNewBattery(int newBattery)
    {
        var rightIsBiggerNode = rightIsBiggerNodes.First?.Value;
        if (rightIsBiggerNode is not null)
        {
            rightIsBiggerNodes.RemoveFirst();

            if (rightIsBiggerNode.Previous is not null && rightIsBiggerNode.Previous.Value < rightIsBiggerNode.Next!.Value)
            {
                rightIsBiggerNodes.AddFirst(rightIsBiggerNode.Previous);
            }
            onBatteries.Remove(rightIsBiggerNode);

            var last = onBatteries.Last!;
            if (last.Value < newBattery)
            {
                rightIsBiggerNodes.AddLast(last);
            }

            onBatteries.AddLast(newBattery);
        }
        else if (newBattery > onBatteries.Last!.Value)
        {
            onBatteries.Last!.Value = newBattery;

            if (onBatteries.Last!.Previous!.Value < newBattery)
            {
                rightIsBiggerNodes.AddLast(onBatteries.Last!.Previous!);
            }
        }

    }

    public override BigInteger JoltageValue { get { return BigInteger.Parse(string.Join("", onBatteries)); } }
}

class ArrayBatterySelection: BatterySelection
{
    private readonly int[] onBatteries;

    private int RightIsBiggerIndex { get; set; }
    private bool RightIsBiggerExists { get { return RightIsBiggerIndex <= onBatteries.Length; } }

    public ArrayBatterySelection(string batteriesStr)
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

    public override void AddNewBattery(int newBattery)
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

    public override BigInteger JoltageValue { get { return BigInteger.Parse(string.Join("", onBatteries)); } }
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

    public BigInteger LargestJoltagePart2(int digits, bool useLinkedList)
    {
        // initialise selection with first 12 digits
        BatterySelection selection;
        if (useLinkedList) {
            selection = new LinkedListBatterySelection(batteries[..digits]);
        } else {
            selection = new ArrayBatterySelection(batteries[..digits]);
        }

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
    private bool useLinkedList = false;

    public BatteryBankScanner(string filename, bool useLinkedList = false)
    {
        using StreamReader reader = new(filename);
        string content = reader.ReadToEnd();
        batteryBanks = [.. content.Split('\n').Where(line => line.Length > 0).Select(line => new BatteryBank(line))];

        this.useLinkedList = useLinkedList;
    }

    public int SumLargestJoltagePart1()
    {
        return batteryBanks.Select(bank => bank.LargestJoltagePart1()).Sum();
    }
    public BigInteger SumLargestJoltagePart2(int digits = 12)
    {
        return batteryBanks.Select(bank => bank.LargestJoltagePart2(digits, useLinkedList)).Aggregate((acc, x) => acc + x);
    }
}
