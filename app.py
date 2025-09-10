import streamlit as st
import requests
from theme import apply_custom_theme
from utils.helpers import get_educational_resources
from PIL import Image
import os

# Apply custom theme
apply_custom_theme()

# Initialize session state for selected symptoms
if 'selected_symptoms' not in st.session_state:
    st.session_state.selected_symptoms = []

# Styled separator helper
def add_separator():
    st.markdown("<div class='custom-separator'></div>", unsafe_allow_html=True)
    
# Create title container with image
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 class='title'>EndoDx</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #d23669; margin-top: -10px;'>Endometriosis Symptom Assessment</h3>", unsafe_allow_html=True)
    st.markdown("<p>This tool helps assess whether your symptoms might be associated with endometriosis. Select any symptoms you're experiencing below and we'll provide a risk assessment.</p>", unsafe_allow_html=True)

with col2:
    # Add the image next to the title
    try:
        image_path = "assets/united1.jpg"
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=200)
        else:
            st.warning("Image not found at: " + image_path)
    except Exception as e:
        st.warning(f"Could not load image: {str(e)}")

# Add informational section at the top
add_separator()
st.subheader("About Endometriosis")
st.markdown("""
Endometriosis is a condition where tissue similar to the lining of the uterus grows outside the uterus,
causing pain, infertility, and other symptoms. It affects approximately 1 in 10 women during their reproductive years.

**Common symptoms include:**
- Painful periods
- Chronic pelvic pain
- Pain during intercourse
- Pain with bowel movements or urination
- Infertility
- Fatigue

If you're experiencing these symptoms, it's important to consult with a healthcare provider for proper diagnosis and treatment.
""")
add_separator()
# Define the symptoms grouped by severity
symptom_groups = {
    "Common symptoms you may notice but often consider low impact": [
        "Headaches",
        "Nausea",
        "Loss of appetite",
        "Malaise/sickness",
        "Decreased energy/exhaustion",
        "Chronic fatigue"
    ],
    "Noticeable symptoms that are worth paying attention to": [
        "Menstrual pain (Dysmenorrhea)",
        "Painful period cramps",
        "Painful ovulation",
        "Chronic pain",
        "Pelvic (or related) Pains",
        "IBS-like symptoms",
        "Abdominal cramps during intercourse",
        "Cysts (unspecified)",
        "Fever",
        "Bowel pain"
    ],
    "Symptoms that are more serious and shouldn't be ignored": [
        "Painful bowel movements",
        "Infertility",
        "Fertility issues",
        "Severe pain",
        "Ovarian cysts",
        "Painful urination",
        "Bleeding",
        "Abnormal uterine bleeding",
        "Irregular or missed periods"
    ]
}

st.subheader("Select symptoms you're experiencing:")

# Disclaimer
st.markdown("""
<div class="disclaimer-container">
<div class="stMarkdown">
**Disclaimer:** This tool is for informational purposes only and is not a substitute for professional medical advice,
diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any
questions you may have regarding a medical condition.
</div>
</div>
""", unsafe_allow_html=True)

# Display symptoms with clickable buttons
for group_name, symptoms in symptom_groups.items():
    st.markdown(f'<div class="symptom-group"><h3 class="header">{group_name}</h3>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i, symptom in enumerate(symptoms):
        col_idx = i % 2
        with cols[col_idx]:
            checked = symptom in st.session_state.selected_symptoms
            if st.checkbox(symptom, value=checked, key=symptom):
                if not checked:
                    st.session_state.selected_symptoms.append(symptom)
            else:
                if checked:
                    st.session_state.selected_symptoms.remove(symptom)

    st.markdown('</div>', unsafe_allow_html=True)

add_separator()

# The button now just triggers the API call based on the updated session state
if st.button("Assess Endometriosis Risk", type="primary"):
    if not st.session_state.selected_symptoms:
        st.warning("Please select at least one symptom to assess your risk.")
    else:
        with st.spinner("Analyzing your symptoms..."):
            try:
                api_url = "http://localhost:8000/predict"
                payload = {"symptoms": st.session_state.selected_symptoms}
                response = requests.post(api_url, json=payload)

                if response.status_code == 200:
                    result = response.json()
                    st.subheader("Assessment Results")

                    risk_level = result.get("risk_level", "unknown")
                    probability = result.get("probability", 0.0)
                    message = result.get("message", "No message available.")
                    resources = get_educational_resources(probability)

                    if risk_level == "high":
                        st.markdown(f'<div class="prediction-box">🔴 {message}</div>', unsafe_allow_html=True)
                    elif risk_level == "moderate":
                        st.markdown(f'<div class="prediction-box">🟡 {message}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="prediction-box">🟢 {message}</div>', unsafe_allow_html=True)

                    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

                    st.progress(min(max(probability, 0.0), 1.0))
                    st.caption(f"Risk probability: {probability:.1%}")

                    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                    st.subheader("Recommended Next Steps")
                    st.markdown(f"""
                    <div class="recommendation-box">
                        {resources["recommendation"]}
                    </div>
                    """, unsafe_allow_html=True)

                    st.subheader("Educational Resources")
                    for link in resources["links"]:
                        st.markdown(f"- [{link['name']}]({link['url']})")

                else:
                    try:
                        st.error(response.json().get("detail", "An error occurred."))
                    except Exception:
                        st.error(f"An error occurred. Raw response: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the prediction service. Please ensure the API is running.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

# Footer
add_separator()
st.caption("EndoDx - This tool is for educational purposes only and does not provide medical diagnosis.")