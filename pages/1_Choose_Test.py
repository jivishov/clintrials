import streamlit as st

# Streamlit layout and logic
st.title("Statistical Test Decision Helper")

# # Sidebar for future menu options
# st.sidebar.title("Menu")
# st.sidebar.text("Future options will go here.")

# Main content
st.header("Select Your Criteria")

# User input
data_type = st.selectbox("What type of data do you have?", ["Continuous", "Categorical"])
num_groups = st.selectbox("How many groups are you comparing?", ["Two", "More than two"])
paired = st.selectbox("Are the data paired?", ["Yes", "No"])
normal_dist = st.selectbox("Is the data normally distributed?", ["Yes", "No", "Don't know"])

# Decision logic
if st.button("Find Suitable Test"):
    if data_type == "Continuous":
        if num_groups == "Two":
            if paired == "Yes":
                if normal_dist == "Yes":
                    st.write("You should use a **Paired t-test**.")
                else:
                    st.write("You should use a **Wilcoxon Signed-Rank Test**.")
            else:
                if normal_dist == "Yes":
                    st.write("You should use an **Independent t-test**.")
                else:
                    st.write("You should use a **Mann-Whitney U Test**.")
        else:
            if normal_dist == "Yes":
                st.write("You should use **One-way ANOVA**.")
            else:
                st.write("You should use **Kruskal-Wallis H Test**.")
    else:
        if num_groups == "Two":
            st.write("You should use a **Chi-Square Test for Independence**.")
        else:
            st.write("You should use a **Chi-Square Test for Goodness of Fit**.")

# Additional suggestion
st.write("Note: For diagnostic or prognostic tests, consider **Sensitivity, Specificity, PPV, and NPV calculations**.")
