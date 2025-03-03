import streamlit as st

# Conversion dictionaries (unchanged)
length_units = {
    'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001,
    'micrometers': 0.000001, 'nanometers': 0.000000001, 'miles': 1609.344,
    'yards': 0.9144, 'feet': 0.3048, 'inches': 0.0254, 'nautical miles': 1852,
    'light-years': 9460730472580800, 'parsecs': 30856775814671900,
    'astronomical units': 149597870700
}

weight_units = {
    'kilograms': 1, 'grams': 0.001, 'milligrams': 0.000001, 'micrograms': 0.000000001,
    'metric tons': 1000, 'pounds': 0.45359237, 'ounces': 0.028349523125,
    'stone': 6.35029318, 'short tons (US)': 907.18474, 'long tons (UK)': 1016.0469088,
    'carats': 0.0002
}

volume_units = {
    'liters': 1, 'milliliters': 0.001, 'cubic meters': 1000, 'cubic centimeters': 0.001,
    'cubic inches': 0.016387064, 'cubic feet': 28.316846592, 'gallons (US)': 3.785411784,
    'gallons (UK)': 4.54609, 'quarts (US)': 0.946352946, 'pints (US)': 0.473176473,
    'fluid ounces (US)': 0.0295735295625, 'barrels (oil)': 158.987294928
}

area_units = {
    'square meters': 1, 'square kilometers': 1000000, 'square centimeters': 0.0001,
    'square millimeters': 0.000001, 'hectares': 10000, 'acres': 4046.8564224,
    'square miles': 2589988.110336, 'square yards': 0.83612736, 'square feet': 0.09290304,
    'square inches': 0.00064516
}

speed_units = {
    'meters/second': 1, 'kilometers/hour': 0.27777777777778, 'miles/hour': 0.44704,
    'feet/second': 0.3048, 'knots': 0.51444444444444, 'mach (at sea level)': 340.2933
}

time_units = {
    'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800,
    'years': 31557600, 'milliseconds': 0.001, 'microseconds': 0.000001,
    'nanoseconds': 0.000000001
}

# Conversion functions (unchanged)
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

# Custom CSS and JS for live background
def add_custom_design():
    st.markdown("""
    <style>
    /* Reset default Streamlit styles */
    .stApp {
        background: none !important;
    }
    
    /* Live animated background */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, #1a1a2e, #0f3460, #16213e);
        animation: gradientBG 15s ease infinite;
        z-index: -1;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main container */
    .main {
        background: rgba(22, 33, 62, 0.8);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        backdrop-filter: blur(5px);
        margin: 2rem auto;
        max-width: 800px;
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background: rgba(15, 52, 96, 0.9);
        border-right: 2px solid #00ffff;
        height: 100vh;
    }
    
    /* Title */
    h1 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #ff00ff;
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Input fields */
    .stNumberInput > div > div > input {
        background: rgba(22, 33, 62, 0.9);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        padding: 0.5rem;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Select boxes */
    .stSelectbox > div > div > div {
        background: rgba(22, 33, 62, 0.9);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Button */
    .stButton > button {
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        color: #1a1a2e;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2.5rem;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #00ffff, 0 0 30px #ff00ff;
    }
    
    /* Success message */
    .stSuccess {
        background: rgba(0, 255, 255, 0.1);
        border: 1px solid #00ffff;
        border-radius: 8px;
        color: #00ffff;
        text-shadow: 0 0 5px #00ffff;
        padding: 1rem;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
    }
    
    /* Columns */
    .stColumn > div {
        padding: 0.5rem;
    }
    
    /* Sidebar header */
    .sidebar h3 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff;
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
def main():
    # Add custom design
    add_custom_design()
    
    # Load futuristic font
    st.markdown('<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)
    
    st.title("Unit Converter 3000")
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Conversion Matrix")
        conversion_type = st.selectbox(
            "Select Conversion Type",
            ["Length", "Weight", "Temperature", "Volume", "Area", "Speed", "Time"],
            help="Choose your dimensional portal"
        )
    
    # Main container
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            value = st.number_input("Input Value", value=0.0, step=0.1, help="Enter your quantum value")
        
        # Unit selection
        if conversion_type == "Length":
            units = list(length_units.keys())
        elif conversion_type == "Weight":
            units = list(weight_units.keys())
        elif conversion_type == "Temperature":
            units = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine']
        elif conversion_type == "Volume":
            units = list(volume_units.keys())
        elif conversion_type == "Area":
            units = list(area_units.keys())
        elif conversion_type == "Speed":
            units = list(speed_units.keys())
        elif conversion_type == "Time":
            units = list(time_units.keys())

        with col2:
            from_unit = st.selectbox("From Unit", units, help="Source dimension")
            to_unit = st.selectbox("To Unit", units, help="Target dimension")
        
        # Convert button outside columns for full width
        if st.button("TRANSFORM"):
            if conversion_type == "Length":
                result = convert_length(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = convert_weight(value, from_unit, to_unit)
            elif conversion_type == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)
            elif conversion_type == "Volume":
                result = convert_volume(value, from_unit, to_unit)
            elif conversion_type == "Area":
                result = convert_area(value, from_unit, to_unit)
            elif conversion_type == "Speed":
                result = convert_speed(value, from_unit, to_unit)
            elif conversion_type == "Time":
                result = convert_time(value, from_unit, to_unit)
            
            st.success(f"{value} {from_unit} → {result:.6f} {to_unit}")

if __name__ == "__main__":
    main()