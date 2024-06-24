def ask_question(question):
    answer = input(f"{question} (yes/no): ").lower()
    return answer == "yes"

def diagnose_issue():
    potential_issues = []

    # Question 1
    if ask_question("Is your computer turning on?"):
        # Sub-questions for Question 1
        if ask_question("Is the screen displaying anything?"):
            if ask_question("Is the screen flickering?"):
                potential_issues.append("Display or graphics card issue.")
        if ask_question("Are there any unusual sounds coming from the computer?"):
            if ask_question("Is the computer heating?"):
                potential_issues.append("Hard drive or fan malfunction.")
    else:
        potential_issues.append("Power supply or motherboard failure.")

    # Question 2
    if not ask_question("Are peripherals (keyboard, mouse) working properly?"):
        if not ask_question("Is the keyboard functioning correctly?"):
            if not ask_question("Are you able to type into the screen?"):
                potential_issues.append("Keyboard driver or connection issue.")
        if not ask_question("Is the mouse working as expected?"):
            if not ask_question("Is the cursor moving on the screen?"):
                potential_issues.append("Mouse driver or connection issue.")

    # Question 3
    if ask_question("Have you recently installed new software or hardware?"):
        if ask_question("Is the new software causing any problems?"):
            if ask_question("Is the new software causing your computer to lag?"):
                potential_issues.append("Software compatibility issue.")
        if not ask_question("Is the new hardware properly installed?"):
            if ask_question("Did the new hardware delete any existing data?"):
                potential_issues.append("Hardware configuration issue.")

    # Question 4
    if ask_question("Is there a problem with internet connectivity?"):
        if ask_question("Is the connection wired?"):
            if ask_question("Is wire connected properly to the ports?"):
                potential_issues.append("Network adapter or cable issue.")
        if not ask_question("Can other devices connect to the internet?"):
            if ask_question("Is the router/modem connected to a power supply?"):
                potential_issues.append("Router or modem problem.")

    # Question 5
    if ask_question("Has there been a recent power outage or surge?"):
        if ask_question("Are other electronics affected by the power issue?"):
            if ask_question("Did your computer start having problems only after the power issue?"):
                potential_issues.append("Power supply or surge protector failure.")
        if ask_question("Did the computer shut down unexpectedly during the event?"):
            if not ask_question("Were you able to restart the computer?"):
                potential_issues.append("Power supply or motherboard issue.")

    # Question 6
    if ask_question("Is the computer running slowly or freezing frequently?"):
        if ask_question("Have you performed disk cleanup and defragmentation?"):
            if not ask_question("Has your computer been exposed to liquid?"):
                potential_issues.append("Disk fragmentation or storage issue.")
        if not ask_question("Is the antivirus software up to date?"):
            if ask_question("Has your computer suffered any data loss/data corruption?"):
                potential_issues.append("Malware or virus infection.")

    # Question 7
    if ask_question("Are there any error messages or pop-ups on the screen?"):
        if ask_question("Do the errors occur during specific tasks or programs?"):
            if ask_question("Do the errors messages stop normal functioning of your programs?"):
                potential_issues.append("Software compatibility or corruption issue.")
        if ask_question("Have you recently updated the operating system?"):
            if ask_question("Is your computer facing any lagging issue?"):
                potential_issues.append("Operating system update or configuration issue.")
    
    # Question 8
    if ask_question("Is the computer making a loud noise during operation?"):
        if ask_question("Does the noise occur when performing specific tasks?"):
            if ask_question("Do the noise occur even when computer is in sleep mode?"):
                potential_issues.append("Fan or cooling system malfunction.")
        if not ask_question("Have you checked for dust buildup inside the computer?"):
            if ask_question("Is the computer overheating as soon as it is switched on?"):
                potential_issues.append("Dust accumulation or hardware overheating.")
            
    # Final potential issues
    if potential_issues:
        print()
        print()
        print("Potential issues detected:")
        for issue in potential_issues:
            print(f"- {issue}")
    else:
        print("No issues detected.")

# Usage
diagnose_issue()
