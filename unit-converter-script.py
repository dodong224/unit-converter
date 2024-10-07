def unit_converter():
    # Dictionary to store conversion factors
    conversion_factors = {
        'length': {
            'm_to_ft': 3.28084,
            'ft_to_m': 0.3048,
            'km_to_mi': 0.621371,
            'mi_to_km': 1.60934
        },
        'weight': {
            'kg_to_lb': 2.20462,
            'lb_to_kg': 0.453592
        },
        'temperature': {
            'c_to_f': lambda c: (c * 9/5) + 32,
            'f_to_c': lambda f: (f - 32) * 5/9
        }
    }

    # Input value
    value = float(input("Enter the value to convert: "))

    # Select unit type
    print("\nSelect unit type:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    unit_type = input("Enter your choice (1/2/3): ")

    # Select specific conversion
    if unit_type == '1':
        print("\nSelect conversion:")
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        conversion = input("Enter your choice (1/2/3/4): ")
        
        if conversion == '1':
            result = value * conversion_factors['length']['m_to_ft']
            print(f"{value} meters is equal to {result:.2f} feet")
        elif conversion == '2':
            result = value * conversion_factors['length']['ft_to_m']
            print(f"{value} feet is equal to {result:.2f} meters")
        elif conversion == '3':
            result = value * conversion_factors['length']['km_to_mi']
            print(f"{value} kilometers is equal to {result:.2f} miles")
        elif conversion == '4':
            result = value * conversion_factors['length']['mi_to_km']
            print(f"{value} miles is equal to {result:.2f} kilometers")
        else:
            print("Invalid choice")

    elif unit_type == '2':
        print("\nSelect conversion:")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        conversion = input("Enter your choice (1/2): ")
        
        if conversion == '1':
            result = value * conversion_factors['weight']['kg_to_lb']
            print(f"{value} kilograms is equal to {result:.2f} pounds")
        elif conversion == '2':
            result = value * conversion_factors['weight']['lb_to_kg']
            print(f"{value} pounds is equal to {result:.2f} kilograms")
        else:
            print("Invalid choice")

    elif unit_type == '3':
        print("\nSelect conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        conversion = input("Enter your choice (1/2): ")
        
        if conversion == '1':
            result = conversion_factors['temperature']['c_to_f'](value)
            print(f"{value}°C is equal to {result:.2f}°F")
        elif conversion == '2':
            result = conversion_factors['temperature']['f_to_c'](value)
            print(f"{value}°F is equal to {result:.2f}°C")
        else:
            print("Invalid choice")

    else:
        print("Invalid unit type choice")

# Run the unit converter
unit_converter()
