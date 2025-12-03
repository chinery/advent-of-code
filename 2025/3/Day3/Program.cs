
using System.Numerics;

string filename = "3.txt";
BatteryBankScanner scanner = new(filename);
Console.WriteLine($"{scanner.SumLargestJoltagePart2(12)}");

class BatterySelection
{
    private static readonly int MAX_BATTERY = 9;
    private readonly int[] onBatteries;
    private int LowestBattery { get; set; } = MAX_BATTERY + 1;
    private int LowestIndex { get; set; } = 0;

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
        if (battery < LowestBattery)
        {
            LowestBattery = battery;
            LowestIndex = i;
        }
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
        else if (newBattery >= LowestBattery)
        {
            AddNewBattery(LowestIndex, newBattery);
        }
    }
    private void AddNewBattery(int indexTurnOff, int newBattery)
    {
        // re-init these so they'll be set correctly for new data
        if (indexTurnOff <= RightIsBiggerIndex)
        {
            RightIsBiggerIndex = onBatteries.Length + 1;
        }
        if (indexTurnOff <= LowestIndex)
        {
            // SetBattery will be called for every value for all 
            // indices >= `indexTurnOff` (which will update lowest)

            // we don't need to worry that there's some value to the left of `indexTurnOff`
            // that is lower, because AddNewBattery is only ever called for LowestIndex or
            // RightIsBiggerIndex, and both are the leftmost indicies for their respective
            // conditions 

            // so if RightIsBiggerIndex = 5, then Right Is Lower Or Equal for 0-4 :)
            LowestBattery = MAX_BATTERY + 1;
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
        /*
            if any digit has a value > than it to the right
            turn off the leftmost digit that has something bigger to the right

            else...
            if the new digit is higher or equal lowest, add it to the end, turn off lowest leftmost
        */

        // initialise selection with first 12 digits
        BatterySelection selection = new(batteries[..digits]);

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
