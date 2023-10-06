import streamlit as st
import math
import scipy.stats
from scipy.stats import norm
from utils import add_copyright

utils.add_copyright()
# Function to calculate sample size
def calculate_sample_size(alpha, power, effect_size, allocation_ratio=1):
    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)
    
    numerator = (z_alpha + z_beta)**2 * (1 + 1/allocation_ratio)
    denominator = effect_size**2
    
    sample_size_group_1 = math.ceil(numerator / denominator)
    sample_size_group_2 = math.ceil(sample_size_group_1 / allocation_ratio)
    
    return sample_size_group_1, sample_size_group_2

# Streamlit app layout and logic
st.title("Clinical Trial Sample Size Calculator")

# Sidebar for future menu options
#st.sidebar.markdown('<a href="https://www.linkedin.com/in/jivishov/" target="_blank">© Emil Jivishov</a>', unsafe_allow_html=True)
#st.sidebar.title("Menu")
# st.sidebar.text("Future options will go here.")

# Main content
st.header("Sample Size Calculation")

# User input
alpha = st.number_input("Significance Level (Alpha, 0-1)", min_value=0.01, max_value=0.99, value=0.05)
power = st.number_input("Power (1 - Beta, 0-1)", min_value=0.50, max_value=0.99, value=0.80)
effect_size = st.number_input("Effect Size (Cohen's d)", min_value=0.01, max_value=10.0, value=0.5)
allocation_ratio = st.number_input("Allocation Ratio (Group 1 / Group 2)", min_value=0.1, max_value=10.0, value=1.0)

# Calculate and display sample size
if st.button("Calculate Sample Size"):
    n1, n2 = calculate_sample_size(alpha, power, effect_size, allocation_ratio)
    st.write(f"Required sample size for Group 1: **{n1}**")
    st.write(f"Required sample size for Group 2: **{n2}**")
