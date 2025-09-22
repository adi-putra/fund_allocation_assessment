# Author: Muhammad Adiputra
# Date: 22/9/2025
# Description: Allocates customer deposits to "High Risk" and "Retirement" portfolios based on one-time and monthly plans, 
# handling happy case, not enough deposits, too much deposits, and empty deposits/zero plans.


def plan_order_alloc(highrisk_required: float, retirement_required: float, deposits: float) -> dict:
    planorder_final_alloc = {"High Risk": 0, "Retirement": 0}
    remaining = deposits

    # fill high risk first
    planorder_final_alloc["High Risk"] = min(highrisk_required, remaining)
    remaining -= planorder_final_alloc["High Risk"]

    # balance fill retirement
    planorder_final_alloc["Retirement"] = min(retirement_required, remaining)

    return planorder_final_alloc

def calc_final_alloc(onetime: dict, monthly: dict, deposits: list) -> dict:

    final_alloc = {
        "High Risk": 0,
        "Retirement": 0
    }

     # Handle empty deposits
    if not deposits or sum(deposits) == 0:
        return final_alloc  # nothing to allocate

    total_deposits = sum(deposits)

    onetime_highrisk = onetime["High Risk"]
    onetime_retirement = onetime["Retirement"]
    monthly_highrisk = monthly["High Risk"]
    monthly_retirement = monthly["Retirement"]

    total_highrisk = onetime_highrisk + monthly_highrisk
    total_retirement = onetime_retirement + monthly_retirement

    total_required = total_highrisk + total_retirement

    # happy case: allocate normally
    if total_deposits == total_required:
        final_alloc["High Risk"] = total_highrisk
        final_alloc["Retirement"] = total_retirement
    # edge case 1: deposit not enough
    elif total_deposits < total_required:
        final_alloc = plan_order_alloc(total_highrisk, total_retirement, total_deposits)

        # Alternative strategy (Proportional Split):
        # highrisk_share = total_highrisk / total_required
        # retirement_share = total_retirement / total_required
        # final_alloc["High Risk"] = total_deposits * highrisk_share
        # final_alloc["Retirement"] = total_deposits * retirement_share

    # edge case 2: deposit too much
    else:
        # strategy: Ignore excess
        final_alloc["High Risk"] = total_highrisk
        final_alloc["Retirement"] = total_retirement
        # optional: uncomment to send excess to Retirement portfolio
        # remaining = total_deposits - total_required
        # final_alloc["Retirement"] = final_alloc["Retirement"] + remaining

    final_alloc["High Risk"] = round(final_alloc["High Risk"], 2)
    final_alloc["Retirement"] = round(final_alloc["Retirement"], 2)
    
    return final_alloc

# demo block: run "python fund_allocation.py"
if __name__ == "__main__":
    # Example deposit plans
    one_time_plan = {"High Risk": 10000, "Retirement": 500}
    monthly_plan = {"High Risk": 0, "Retirement": 100}

    # Different deposit scenarios
    test_deposits = {
        "Happy case": [10500, 100],
        "Not enough deposits": [5000],
        "Partial enough": [10500],
        "Too much deposits": [12000],
        "Empty deposits": [],
        "Zero plans": [0, 0]
    }

    for scenario, deposits in test_deposits.items():
        alloc = calc_final_alloc(one_time_plan, monthly_plan, deposits)
        print(f"{scenario}: deposits={deposits} -> allocation={alloc}")