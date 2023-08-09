import subprocess
import ctypes

def check_execution_policy():
    result = subprocess.run(['powershell', 'Get-ExecutionPolicy'], capture_output=True, text=True)
    execution_policy = result.stdout.strip()
    return execution_policy

def set_execution_policy(policy):
    subprocess.run(['powershell', f'Set-ExecutionPolicy {policy} -Scope Process'])

def analyze_policy():
    print("Analyzing policy and providing insights...")
    result = subprocess.run(['powershell', 'Get-ExecutionPolicy -List'], capture_output=True, text=True)
    policy_info = result.stdout.strip()
    print("Execution Policy Details:\n")
    print(policy_info)
    print("\nInsights:")
    print("- Consider the current policy settings and their impact on security.")
    print("- Be cautious when setting policies to more permissive levels.")
    print("- Regularly review and update policies to align with security requirements.")

def main():
    print("Execution Policy Manager for Windows")
    print("=====================================\n")

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this program as an administrator to modify execution policies.")
        input("Press Enter to exit...")
        return

    while True:
        current_policy = check_execution_policy()

        print("Current Execution Policy:", current_policy)

        print("\nMenu:")
        print("1. Check Execution Policy and Analyze")
        print("2. Set Execution Policy to Unrestricted (Scope Process)")
        print("3. Set Execution Policy to Unrestricted (Force)")
        print("4. Set Execution Policy to Restricted")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyze_policy()
        elif choice == "2":
            set_execution_policy("Unrestricted")
            print("Execution Policy set to Unrestricted (Scope Process)")
        elif choice == "3":
            set_execution_policy("Unrestricted -Force")
            print("Execution Policy set to Unrestricted (Force)")
        elif choice == "4":
            set_execution_policy("Restricted")
            print("Execution Policy set to Restricted")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
