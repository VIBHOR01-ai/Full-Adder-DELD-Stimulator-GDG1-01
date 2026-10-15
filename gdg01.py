"""
Full Adder Logic Simulator
An interactive CLI tool for digital logic design and binary addition simulation.
"""

import sys
import time

# ==============================================================================
# UI & ANSI STYLING PALETTE
# ==============================================================================
class TerminalTheme:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Status Colors
    PRIMARY_CYAN = "\033[96m"
    ACCENT_MAGENTA = "\033[95m"
    INFO_BLUE = "\033[94m"
    LOGIC_HIGH_GREEN = "\033[92m"
    LOGIC_CARRY_YELLOW = "\033[93m"
    ERROR_RED = "\033[91m"


# ==============================================================================
# CORE DIGITAL LOGIC ENGINE
# ==============================================================================
def compute_full_adder(input_bit_a: int, input_bit_b: int, carry_in_bit: int) -> tuple[int, int]:
    """
    Computes Sum and Carry-out for a standard 1-bit Full Adder circuit.
    
    Equations:
      Sum  = A ⊕ B ⊕ Cin
      Cout = (A · B) + (B · Cin) + (A · Cin)
    """
    sum_bit = input_bit_a ^ input_bit_b ^ carry_in_bit
    carry_out_bit = (input_bit_a & input_bit_b) | (input_bit_b & carry_in_bit) | (input_bit_a & carry_in_bit)
    return sum_bit, carry_out_bit


# ==============================================================================
# UI COMPONENTS & PRESENTATION
# ==============================================================================
def display_header_banner():
    """Renders the main project header banner."""
    print(f"{TerminalTheme.PRIMARY_CYAN}{TerminalTheme.BOLD}")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                ⚡ FULL ADDER LOGIC SIMULATOR ⚡                ║")
    print("║            Digital Electronics & Gate Level Modeling           ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print(f"{TerminalTheme.RESET}")


def display_truth_table():
    """Displays an ASCII-formatted truth table of all 8 possible input states."""
    print(f"\n{TerminalTheme.ACCENT_MAGENTA}{TerminalTheme.BOLD}📊 1-BIT FULL ADDER TRUTH TABLE{TerminalTheme.RESET}")
    print(f"{TerminalTheme.DIM}┌───────┬───────┬───────┬─────────────────┬──────────────────┐{TerminalTheme.RESET}")
    print(f"{TerminalTheme.BOLD}│   A   │   B   │  Cin  │   Sum (S) ⊕     │   Carry (Cout)   │{TerminalTheme.RESET}")
    print(f"{TerminalTheme.DIM}├───────┼───────┼───────┼─────────────────┼──────────────────┤{TerminalTheme.RESET}")

    all_input_combinations = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    ]

    for bit_a, bit_b, bit_cin in all_input_combinations:
        calculated_sum, calculated_carry = compute_full_adder(bit_a, bit_b, bit_cin)

        # Apply terminal highlighting to HIGH (1) logic states
        formatted_sum = (
            f"{TerminalTheme.LOGIC_HIGH_GREEN}1{TerminalTheme.RESET}"
            if calculated_sum
            else f"{TerminalTheme.DIM}0{TerminalTheme.RESET}"
        )
        formatted_carry = (
            f"{TerminalTheme.LOGIC_CARRY_YELLOW}1{TerminalTheme.RESET}"
            if calculated_carry
            else f"{TerminalTheme.DIM}0{TerminalTheme.RESET}"
        )

        print(
            f"│   {bit_a}   │   {bit_b}   │   {bit_cin}   │"
            f"        {formatted_sum}        │"
            f"        {formatted_carry}         │"
        )

    print(f"{TerminalTheme.DIM}└───────┴───────┴───────┴─────────────────┴──────────────────┘{TerminalTheme.RESET}\n")


def prompt_binary_bit(signal_label: str) -> int:
    """Prompts the user for a single binary bit (0 or 1) with loop validation."""
    while True:
        raw_user_input = input(f"{TerminalTheme.BOLD}👉 Enter {signal_label} [0 or 1]: {TerminalTheme.RESET}").strip()
        if raw_user_input in ("0", "1"):
            return int(raw_user_input)
        print(f"{TerminalTheme.ERROR_RED}✖ Error: Input must be a valid binary digit (0 or 1).{TerminalTheme.RESET}")


def run_interactive_simulation():
    """Handles the custom interactive input phase and visual output rendering."""
    print(f"\n{TerminalTheme.INFO_BLUE}{TerminalTheme.BOLD}🎛️  SIGNAL INPUT CONFIGURATION{TerminalTheme.RESET}")
    print(f"{TerminalTheme.DIM}────────────────────────────────────────────{TerminalTheme.RESET}")
    
    input_signal_a = prompt_binary_bit("Input Pin A ")
    input_signal_b = prompt_binary_bit("Input Pin B ")
    carry_input_cin = prompt_binary_bit("Carry In Pin")

    print(f"\n{TerminalTheme.PRIMARY_CYAN}⚙️  Simulating propagation delay...{TerminalTheme.RESET}")
    time.sleep(0.25)

    # Calculate Logic
    result_sum, result_carry_out = compute_full_adder(input_signal_a, input_signal_b, carry_input_cin)

    # Visual State Badges
    sum_badge = (
        f"{TerminalTheme.LOGIC_HIGH_GREEN}[ HIGH (1) ]{TerminalTheme.RESET}"
        if result_sum
        else f"{TerminalTheme.DIM}[ LOW (0)  ]{TerminalTheme.RESET}"
    )
    carry_badge = (
        f"{TerminalTheme.LOGIC_CARRY_YELLOW}[ HIGH (1) ]{TerminalTheme.RESET}"
        if result_carry_out
        else f"{TerminalTheme.DIM}[ LOW (0)  ]{TerminalTheme.RESET}"
    )

    # Render Results Card
    print(f"\n{TerminalTheme.LOGIC_HIGH_GREEN}{TerminalTheme.BOLD}✨ SIMULATION RESULTS{TerminalTheme.RESET}")
    print(f"{TerminalTheme.DIM}┌────────────────────────────────────────────┐{TerminalTheme.RESET}")
    print(f"│  A: {input_signal_a}    │  B: {input_signal_b}    │  Cin: {carry_input_cin}              │")
    print(f"{TerminalTheme.DIM}├────────────────────────────────────────────┤{TerminalTheme.RESET}")
    print(f"│  Sum Output               : {result_sum} {sum_badge} │")
    print(f"│  Carry Output             : {result_carry_out} {carry_badge} │")
    print(f"{TerminalTheme.DIM}└────────────────────────────────────────────┘{TerminalTheme.RESET}\n")


# ==============================================================================
# MAIN APPLICATION CONTROLLER
# ==============================================================================
def main():
    display_header_banner()

    while True:
        print(f"{TerminalTheme.BOLD}MAIN MENU:{TerminalTheme.RESET}")
        print(f"  {TerminalTheme.PRIMARY_CYAN}[1]{TerminalTheme.RESET} View Full Adder Truth Table 📋")
        print(f"  {TerminalTheme.PRIMARY_CYAN}[2]{TerminalTheme.RESET} Simulate Custom Logic Inputs 🧪")
        print(f"  {TerminalTheme.PRIMARY_CYAN}[3]{TerminalTheme.RESET} Exit Simulator 🚪")

        menu_choice = input(f"\n{TerminalTheme.BOLD}Select an option (1-3): {TerminalTheme.RESET}").strip()

        if menu_choice == "1":
            display_truth_table()
        elif menu_choice == "2":
            run_interactive_simulation()
        elif menu_choice == "3":
            print(f"\n{TerminalTheme.LOGIC_CARRY_YELLOW}👋 Simulator terminated successfully. Happy coding!{TerminalTheme.RESET}\n")
            sys.exit(0)
        else:
            print(f"{TerminalTheme.ERROR_RED}✖ Invalid selection. Please enter 1, 2, or 3.{TerminalTheme.RESET}\n")


if __name__ == "__main__":
    main()