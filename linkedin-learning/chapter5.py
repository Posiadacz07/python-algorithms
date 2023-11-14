# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order
for order in test_orders:
    total = 0.0

    for item in order:
        match item:
            case "shirt" | "pants" | "jacket" | "dress" as garment, size, starch, sameday:
                total += 12.95
                if starch:
                    total += 2.00
                if sameday:
                    total += 10.00
            case str() as desc, weight:
                if weight >= 15.0:
                    total += (weight * 4.95) * .9
                else:
                    total += (weight * 4.95)
            case "comforter" | "cover" as blanket, dry_clean, size:
                total += 25.00
            case _:
                print("invalid item format")

    print("Order Total:", total)