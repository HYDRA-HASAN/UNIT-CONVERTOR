import streamlit as st

# Conversion dictionaries and functions
length_units = {
    'meters': 1,
    'kilometers': 1000,
    'centimeters': 0.01,
    'millimeters': 0.001,
    'micrometers': 0.000001,
    'nanometers': 0.000000001,
    'miles': 1609.344,
    'yards': 0.9144,
    'feet': 0.3048,
    'inches': 0.0254,
    'nautical miles': 1852,
    'light-years': 9460730472580800,
    'parsecs': 30856775814671900,
    'astronomical units': 149597870700
}

weight_units = {
    'kilograms': 1,
    'grams': 0.001,
    'milligrams': 0.000001,
    'micrograms': 0.000000001,
    'metric tons': 1000,
    'pounds': 0.45359237,
    'ounces': 0.028349523125,
    'stone': 6.35029318,
    'short tons (US)': 907.18474,
    'long tons (UK)': 1016.0469088,
    'carats': 0.0002
}

volume_units = {
    'liters': 1,
    'milliliters': 0.001,
    'cubic meters': 1000,
    'cubic centimeters': 0.001,
    'cubic inches': 0.016387064,
    'cubic feet': 28.316846592,
    'gallons (US)': 3.785411784,
    'gallons (UK)': 4.54609,
    'quarts (US)': 0.946352946,
    'pints (US)': 0.473176473,
    'fluid ounces (US)': 0.0295735295625,
    'barrels (oil)': 158.987294928
}

area_units = {
    'square meters': 1,
    'square kilometers': 1000000,
    'square centimeters': 0.0001,
    'square millimeters': 0.000001,
    'hectares': 10000,
    'acres': 4046.8564224,
    'square miles': 2589988.110336,
    'square yards': 0.83612736,
    'square feet': 0.09290304,
    'square inches': 0.00064516
}

speed_units = {
    'meters/second': 1,
    'kilometers/hour': 0.27777777777778,
    'miles/hour': 0.44704,
    'feet/second': 0.3048,
    'knots': 0.51444444444444,
    'mach (at sea level)': 340.2933
}

time_units = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800,
    'years': 31557600,  # Based on Julian year (365.25 days)
    'milliseconds': 0.001,
    'microseconds': 0.000001,
    'nanoseconds': 0.000000001
}

def convert_length(value, from_unit, to_unit):
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    value_in_kg = value * weight_units[from_unit]
    return value_in_kg / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        temp = value
    elif from_unit == 'Fahrenheit':
        temp = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        temp = value - 273.15
    elif from_unit == 'Rankine':
        temp = (value - 491.67) * 5/9
    
    if to_unit == 'Celsius':
        return temp
    elif to_unit == 'Fahrenheit':
        return (temp * 9/5) + 32
    elif to_unit == 'Kelvin':
        return temp + 273.15
    elif to_unit == 'Rankine':
        return (temp + 273.15) * 9/5

def convert_volume(value, from_unit, to_unit):
    value_in_liters = value * volume_units[from_unit]
    return value_in_liters / volume_units[to_unit]

def convert_area(value, from_unit, to_unit):
    value_in_sq_meters = value * area_units[from_unit]
    return value_in_sq_meters / area_units[to_unit]

def convert_speed(value, from_unit, to_unit):
    value_in_mps = value * speed_units[from_unit]
    return value_in_mps / speed_units[to_unit]

def convert_time(value, from_unit, to_unit):
    value_in_seconds = value * time_units[from_unit]
    return value_in_seconds / time_units[to_unit]

# Streamlit app
def main():
    st.title("Comprehensive Unit Converter")
    
    # Sidebar for conversion type selection
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature", "Volume", "Area", "Speed", "Time"]
    )
    
    # Input value
    value = st.number_input("Enter value to convert", value=0.0, step=0.1)
    
    # Unit selection and conversion
    if conversion_type == "Length":
        from_unit = st.selectbox("From unit", list(length_units.keys()))
        to_unit = st.selectbox("To unit", list(length_units.keys()))
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Weight":
        from_unit = st.selectbox("From unit", list(weight_units.keys()))
        to_unit = st.selectbox("To unit", list(weight_units.keys()))
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Temperature":
        temp_units = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine']
        from_unit = st.selectbox("From unit", temp_units)
        to_unit = st.selectbox("To unit", temp_units)
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Volume":
        from_unit = st.selectbox("From unit", list(volume_units.keys()))
        to_unit = st.selectbox("To unit", list(volume_units.keys()))
        if st.button("Convert"):
            result = convert_volume(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Area":
        from_unit = st.selectbox("From unit", list(area_units.keys()))
        to_unit = st.selectbox("To unit", list(area_units.keys()))
        if st.button("Convert"):
            result = convert_area(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Speed":
        from_unit = st.selectbox("From unit", list(speed_units.keys()))
        to_unit = st.selectbox("To unit", list(speed_units.keys()))
        if st.button("Convert"):
            result = convert_speed(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
            
    elif conversion_type == "Time":
        from_unit = st.selectbox("From unit", list(time_units.keys()))
        to_unit = st.selectbox("To unit", list(time_units.keys()))
        if st.button("Convert"):
            result = convert_time(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

if __name__ == "__main__":
    main()