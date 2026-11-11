def process_age(age):
    if age is None:
        raise TypeError("Age cannot be None")
    if isinstance(age, bool):
        raise TypeError("Age cannot be a boolean")
    try:
        age_int = int(age)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid age input: {age}")
        
    if not (0 <= age_int <= 120):
        raise ValueError(f"Age must be between 0 and 120, got {age_int}")
    return age_int


def process_fare(fare):
    if fare is None:
        raise TypeError("Fare cannot be None")
    if isinstance(fare, bool):
        raise TypeError("Fare cannot be a boolean")
    try:
        fare_float = float(fare)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid fare input: {fare}")
        
    if fare_float < 0:
        raise ValueError(f"Fare cannot be negative: {fare_float}")
    return round(fare_float, 2)


def process_passenger_name(name):
    if name is None:
        raise TypeError("Name cannot be None")
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
        
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Name cannot be empty or whitespace only")
    return cleaned_name


if __name__ == "__main__":
    print("Testing Processor Functions...")
    test_inputs = [
        ("25", 15.5, "Rahul Sharma"),
        (None, -10, ""),
        ("abc", "free", 123)
    ]
    
    for age, fare, name in test_inputs:
        print(f"\nTesting with inputs: age={age}, fare={fare}, name={name}")
        try:
            print("Age:", process_age(age))
        except Exception as e:
            print("Age Error:", e)
            
        try:
            print("Fare:", process_fare(fare))
        except Exception as e:
            print("Fare Error:", e)
            
        try:
            print("Name:", process_passenger_name(name))
        except Exception as e:
            print("Name Error:", e)