import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("regret_model.pkl")

st.set_page_config(page_title="Decision Regret Checker", layout="centered")

st.title("🤔 Will I Regret This Decision?")
st.caption("Ask Yourself Before You Decide")

st.write("Rate yourself honestly (1 = Low, 5 = High)")

# Personality sliders (with real trait names in brackets)

neuro = st.slider(
    "I get stressed or anxious easily (Neuroticism)",
    1.0, 5.0, 3.0
)

cons = st.slider(
    "I am disciplined and responsible (Conscientiousness)",
    1.0, 5.0, 3.0
)

extra = st.slider(
    "I am outgoing and energetic (Extraversion)",
    1.0, 5.0, 3.0
)

agree = st.slider(
    "I am kind and cooperative (Agreeableness)",
    1.0, 5.0, 3.0
)

open_ = st.slider(
    "I like trying new things (Openness)",
    1.0, 5.0, 3.0
)

# New Feature: Decision Type
decision_type = st.selectbox(
    "What kind of decision are you making?",
    ["Career", "Relationship", "Financial", "Education", "Personal Life"]
)

# Adjust probability slightly based on decision type
decision_weight = {
    "Career": 5,
    "Relationship": 8,
    "Financial": 6,
    "Education": 4,
    "Personal Life": 3
}

if st.button("Check My Regret Risk"):

    input_data = np.array([[neuro, cons, extra, agree, open_]])
    prob = model.predict_proba(input_data)[0][1] * 100

    # Adjusting based on decision type
    prob = prob + decision_weight[decision_type]

    prob = min(prob, 100)

    st.subheader(f"Your Estimated Regret Risk: {round(prob,2)}%")

    # Personalized Advice
    if prob > 75:
        st.error("⚠ High regret tendency detected.")
        st.write("Advice:")
        st.write("- Take more time before deciding.")
        st.write("- Write pros and cons clearly.")
        st.write("- Discuss with someone you trust.")
        st.write("- Avoid emotional decisions.")
        
    elif prob > 45:
        st.warning("⚡ Moderate regret tendency.")
        st.write("Advice:")
        st.write("- Double-check your reasoning.")
        st.write("- Avoid impulsive choices.")
        st.write("- Sleep over the decision if possible.")
        
    else:
        st.success("✅ Low regret tendency.")
        st.write("Advice:")
        st.write("- You generally trust your decisions well.")
        st.write("- Stay confident but still think practically.")
        st.write("- Big decisions still deserve structured thinking.")

    st.markdown("---")
    st.caption("Note: This tool gives an estimated tendency, not a psychological diagnosis.")