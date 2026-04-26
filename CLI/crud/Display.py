"""
display.py
==========
Sirf print karna — koi DB code nahi.
MySQL ya SQLite dono ke saath kaam karta hai.
"""


def print_table(rows):
    """Rows ko table format mein print karo."""
    if not rows:
        print("\n  ⚠️  Koi record nahi mila.\n")
        return
    print()
    print(f"  {'ID':<5} {'Name':<20} {'Age':<5} {'Course':<22} {'Marks'}")
    print("  " + "─" * 60)
    for r in rows:
        print(f"  {r[0]:<5} {r[1]:<20} {r[2]:<5} {r[3]:<22} {r[4]}")
    print(f"\n  Total: {len(rows)} record(s)\n")


def print_student(row):
    """Single student card dikhao."""
    if not row:
        print("\n  ❌ Student nahi mila.\n")
        return
    print()
    print("  ┌─────────────────────────────┐")
    print(f"  │  ID     : {row[0]}")
    print(f"  │  Name   : {row[1]}")
    print(f"  │  Age    : {row[2]}")
    print(f"  │  Course : {row[3]}")
    print(f"  │  Marks  : {row[4]}")
    print("  └─────────────────────────────┘\n")


def print_stats(stats: dict):
    """Statistics sundar format mein."""
    print()
    print("  📊 STATISTICS")
    print("  " + "─" * 35)
    print(f"  Total Students  : {stats['total']}")
    if stats['total'] and stats['total'] > 0:
        print(f"  Average Marks   : {stats['average']}")
        print(f"  Highest Marks   : {stats['highest']}")
        print(f"  Lowest Marks    : {stats['lowest']}")
        if stats['topper']:
            print(f"  Topper          : {stats['topper']['name']} "
                  f"({stats['topper']['marks']} marks) 🏆")
    print()


def confirm(prompt: str) -> bool:
    """User se yes/no pucho."""
    ans = input(f"  {prompt} (yes/no): ").strip().lower()
    return ans == "yes"