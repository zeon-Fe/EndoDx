import joblib
import numpy as np
from typing import List, Dict

# Symptom mapping (user-facing → internal feature names)
symptom_mapping = {
    "Menstrual pain (Dysmenorrhea)": "menstrual_pain_dysmenorrhea",
    "Pelvic (or related) Pains": "pelvic_pain",
    "Irregular or missed periods": "irregular_missed_periods",
    "Painful bowel movements": "painful_bowel_movements",
    "Nausea": "nausea",
    "Infertility": "infertility",
    "Painful period cramps": "painful_period_cramps",
    "Chronic pain": "chronic_pain",
    "Chronic fatigue": "chronic_fatigue",
    "Painful ovulation": "painful_ovulation",
    "Severe pain": "severe_pain",
    "Bleeding": "bleeding",
    "Fertility issues": "fertility_issues",
    "Ovarian cysts": "ovarian_cysts",
    "Painful urination": "painful_urination",
    "Headaches": "headaches",
    "IBS-like symptoms": "ibslike_symptoms",
    "Bowel pain": "bowel_pain",
    "Cysts (unspecified)": "cysts_unspecified",
    "Malaise/sickness": "malaise_sickness",
    "Abnormal uterine bleeding": "abnormal_uterine_bleeding",
    "Fever": "fever",
    "Decreased energy/exhaustion": "decreased_energy_exhaustion",
    "Abdominal cramps during intercourse": "abdominal_cramps_during_intercourse",
    "Loss of appetite": "loss_of_appetite"
}

def load_model_artifacts():
    model = joblib.load("models/svm_model.pkl")          
    scaler = joblib.load("models/svm_scaler.pkl")       
    features = joblib.load("models/svm_features.pkl")
    return model, scaler, features


def map_symptoms_to_vector(user_symptoms: List[str], features: List[str]) -> np.ndarray:
    """Convert user symptoms into a feature vector (1 x N) in correct order"""
    selected = {symptom_mapping[s] for s in user_symptoms if s in symptom_mapping}
    return np.array([[1 if f in selected else 0 for f in features]], dtype=float)


def get_educational_resources(probability: float) -> Dict[str, List[str]]:
    """Return appropriate educational resources based on prediction probability"""
    resources = {
        "high_risk": {
            "title": "Based on your symptoms, you may be at higher risk for endometriosis",
            "links": [
                {"name": "Endometriosis Association", "url": "https://www.endometriosisassn.org/"},
                {"name": "EndoFound - Endometriosis Foundation of America", "url": "https://www.endofound.org/"},
                {"name": "ACOG - Endometriosis Information", "url": "https://www.acog.org/womens-health/faqs/endometriosis"},
                {"name": "FPA Sri Lanka - End Silence Endometriosis", "url": "https://www.fpasrilanka.org/en/content/end-silence-endometriosis"},
                {"name": "ACE 2025 - Asian Congress on Endometriosis", "url": "https://ace2025colombo.lk/"}
            ],
            "recommendation": "We recommend consulting with a healthcare provider who specializes in endometriosis for a comprehensive evaluation."
        },
        "moderate_risk": {
            "title": "Some of your symptoms may be associated with endometriosis",
            "links": [
                {"name": "Endometriosis UK", "url": "https://www.endometriosis-uk.org/"},
                {"name": "Mayo Clinic - Endometriosis Overview", "url": "https://www.mayoclinic.org/diseases-conditions/endometriosis/symptoms-causes/syc-20354656"},
                {"name": "FPA Sri Lanka - End Silence Endometriosis", "url": "https://www.fpasrilanka.org/en/content/end-silence-endometriosis"},
                {"name": "ACE 2025 - Asian Congress on Endometriosis", "url": "https://ace2025colombo.lk/"}
            ],
            "recommendation": "Consider discussing these symptoms with your healthcare provider to determine if further evaluation is needed."
        },
        "low_risk": {
            "title": "Your symptoms show minimal association with endometriosis",
            "links": [
                {"name": "Women's Health.gov - Endometriosis", "url": "https://www.womenshealth.gov/a-z-topics/endometriosis"},
                {"name": "General Women's Health Resources", "url": "https://www.healthywomen.org/"},
                {"name": "FPA Sri Lanka - End Silence Endometriosis", "url": "https://www.fpasrilanka.org/en/content/end-silence-endometriosis"},
                {"name": "ACE 2025 - Asian Congress on Endometriosis", "url": "https://ace2025colombo.lk/"}
            ],
            "recommendation": "If you're experiencing persistent symptoms, it's always a good idea to consult with a healthcare provider."
        }
    }
    
    if probability >= 0.7:
        return resources["high_risk"]
    elif probability >= 0.4:
        return resources["moderate_risk"]
    else:
        return resources["low_risk"]
