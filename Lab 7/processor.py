def parse_transit_corridor(corridor_code):
    if corridor_code is None or not isinstance(corridor_code, str):
        raise TypeError("Corridor code must be a non-empty string")
    
    parts = corridor_code.strip().split('-')
    if len(parts) != 3:
        raise ValueError(f"Invalid format. Expected 'ORIG-DEST-ZONES', got: '{corridor_code}'")
        
    orig, dest, zones_str = parts
    if not orig.strip() or not dest.strip():
        raise ValueError("Origin and destination cannot be empty")
        
    try:
        zones = int(zones_str)
    except (ValueError, TypeError):
        raise ValueError(f"Zones must be a valid integer, got: '{zones_str}'")
        
    if zones < 0:
        raise ValueError(f"Zones cannot be negative, got: {zones}")
        
    base_fare = 2.50 + (zones * 0.75)
    return f"Route {orig.upper()}->{dest.upper()}: {zones} Zones, Fare ${base_fare:.2f}"


def lookup_concession_discount(category_name):
    if category_name is None or not isinstance(category_name, str):
        raise TypeError("Category name must be a non-empty string")
        
    category = category_name.strip().upper()
    discounts = {
        "STANDARD": 1.00,
        "STUDENT": 0.50,
        "SENIOR": 0.35,
        "MILITARY": 0.20,
        "CHILD": 0.00
    }
    
    if category not in discounts:
        raise KeyError(f"Invalid concession category: '{category_name}'")
        
    return discounts[category]


def compute_passenger_density(occupancy_ratio_str):
    if occupancy_ratio_str is None or not isinstance(occupancy_ratio_str, str):
        raise TypeError("Occupancy ratio must be a string formatted as 'passengers/km'")
        
    parts = occupancy_ratio_str.strip().split('/')
    if len(parts) != 2:
        raise ValueError(f"Invalid format. Expected 'passengers/km', got: '{occupancy_ratio_str}'")
        
    passengers_str, km_str = parts
    
    try:
        passengers = float(passengers_str)
        km = float(km_str)
    except (ValueError, TypeError):
        raise ValueError("Passengers and kilometers must be numeric values")
        
    if passengers < 0 or km < 0:
        raise ValueError("Passengers and kilometers cannot be negative")
        
    if km == 0:
        raise ZeroDivisionError("Distance (km) cannot be zero")
        
    density = passengers / km
    return round(density, 2)


def main():
    print("==== Running parse_transit_corridor ====")
    c_input = input("Enter corridor (e.g. DT-UP-3): ")
    try:
        print(parse_transit_corridor(c_input))
    except Exception as e:
        print(f"Error: {e}")

    print("\n==== Running lookup_concession_discount ====")
    cat_input = input("Enter concession category (e.g. STUDENT, SENIOR): ")
    try:
        print("Multiplier:", lookup_concession_discount(cat_input))
    except Exception as e:
        print(f"Error: {e}")

    print("\n==== Running compute_passenger_density ====")
    d_input = input("Enter passengers/km (e.g. 50/10.0): ")
    try:
        print("Density:", compute_passenger_density(d_input))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()