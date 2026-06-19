#!/usr/bin/env python3
"""
Freelance Rate Calculator — Figure out your hourly rate.
Usage: python freelance_rate_calc.py --salary 100000 --hours 40 --weeks 48
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate your freelance hourly rate")
    parser.add_argument("--salary", type=float, help="Desired annual salary")
    parser.add_argument("--hours", type=float, default=40, help="Hours per week")
    parser.add_argument("--weeks", type=float, default=48, help="Weeks worked per year")
    parser.add_argument("--expenses", type=float, default=0, help="Annual business expenses")
    args = parser.parse_args()
    
    if not args.salary:
        # Interactive mode
        args.salary = float(input("Desired annual salary ($): "))
        args.expenses = float(input("Annual business expenses ($): ") or "0")
    
    total_needed = args.salary + args.expenses
    total_hours = args.hours * args.weeks
    rate = total_needed / total_hours
    
    print(f"\n📊 Freelance Rate Calculator")
    print(f"{'='*40}")
    print(f"Desired salary:    ${args.salary:,.2f}")
    print(f"Business expenses: ${args.expenses:,.2f}")
    print(f"Total needed:      ${total_needed:,.2f}")
    print(f"Hours/year:        {total_hours:.0f}")
    print(f"{'='*40}")
    print(f"👉 Your rate:      ${rate:.2f}/hour")
    print(f"                   ${rate*8:.2f}/day (8hr)")
    print(f"                   ${rate*160:.2f}/month (160hr)")
    
    # Common benchmarks
    print(f"\n📈 Benchmarks:")
    print(f"  $30/hr = ${30*total_hours:,.0f}/year")
    print(f"  $50/hr = ${50*total_hours:,.0f}/year")
    print(f"  $75/hr = ${75*total_hours:,.0f}/year")
    print(f"  $100/hr = ${100*total_hours:,.0f}/year")

if __name__ == "__main__":
    main()
