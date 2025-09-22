Sure! Here’s a **professional README** for your project. You can create a `README.md` file in the same folder as `fund_allocation.py` and `test.py`:

````markdown
# Fund Allocation Assessment

**Author:** Muhammad Adiputra  
**Date:** 22/9/2025  

---

## Overview
This project implements a Python module to **allocate customer deposits** to two portfolios: `"High Risk"` and `"Retirement"` based on **one-time** and **monthly deposit plans**.  

The allocation logic handles:
- **Happy case**: deposits exactly match the required amounts  
- **Not enough deposits**: allocates using **Plan Order** (High Risk first)  
- **Too much deposits**: caps allocation at required amounts  
- **Empty deposits / zero plans**: returns zero allocation  
- **Optional proportional split** (commented for future use)  

---

## Files
- `fund_allocation.py` : Main module containing the allocation functions and a demo block.  
- `test.py` : Unit tests covering all major scenarios including edge cases.  

---

## Usage

### Running the Demo
You can run the main script to see example allocations for different deposit scenarios:

```bash
python fund_allocation.py
````

Example output:

```
Happy case: deposits=[10500, 100] -> allocation={'High Risk': 10000, 'Retirement': 600}
Not enough deposits: deposits=[5000] -> allocation={'High Risk': 5000, 'Retirement': 0}
Partial enough: deposits=[10500] -> allocation={'High Risk': 10000, 'Retirement': 500}
Too much deposits: deposits=[12000] -> allocation={'High Risk': 10000, 'Retirement': 600}
Empty deposits: deposits=[] -> allocation={'High Risk': 0, 'Retirement': 0}
Zero plans: deposits=[0, 0] -> allocation={'High Risk': 0, 'Retirement': 0}
```

### Running Unit Tests

To run the unit tests and verify the correctness of the allocation logic:

```bash
python test.py
```

All tests should pass if the module works correctly.

---

## Functions

### `calc_final_alloc(onetime: dict, monthly: dict, deposits: list) -> dict`

Calculates the final allocation of deposits across `"High Risk"` and `"Retirement"` portfolios.

**Parameters:**

* `onetime` : dict with required one-time deposits for each portfolio
* `monthly` : dict with required monthly deposits for each portfolio
* `deposits` : list of deposit amounts from the customer

**Returns:**
A dictionary with the allocated amounts:

```python
{"High Risk": <amount>, "Retirement": <amount>}
```

---

### `plan_order_alloc(highrisk_required: float, retirement_required: float, deposits: float) -> dict`

Helper function that allocates deposits **High Risk first, then Retirement**.

---

## Notes

* Type hints are used for clarity.
* The module rounds allocation amounts to 2 decimal places.
* Proportional split logic is included as comments for future enhancement.
