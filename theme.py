import streamlit as st

# Custom theme for Streamlit app with salmon pink colors
def apply_custom_theme():
    st.markdown("""
    <style>
    /* Target the main app container */
    .stApp {
        background: linear-gradient(145deg, #ffdee9 30%, #ffb6c1 90%), 
                    url("https://www.transparenttextures.com/patterns/flowers.png");
        background-blend-mode: hard-light;
        background-size: auto;
    }
    
        
    /* Expand the main content area */
    .main .block-container {
        padding: 2rem 5rem;
        width: 1200px;
    }
    
    /* Style headers for better visibility */
    h1, h2, h3, h4, h5, h6 {
        color: #d23669 !important;
    }

    .subtitle {
        color: #d23669 !important;
        font-size: 1.2rem !important;
        margin-top: -5px;
        font-weight: 600;
    }
    
    /* Only style the main CTA buttons, not symptoms */
    .stButton>button[kind="primary"] {
        background-color: #ff6b6b !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 14px 32px !important;
        font-weight: bold !important;
        border: 2px solid #d23669 !important;  /* add border */
        box-shadow: 0 6px 14px rgba(210, 54, 105, 0.35) !important; /* subtle glow */
        margin-top: 30px !important; /* spacing from symptoms */
    }
    
    /* Center the main CTA button */
    div.stButton > button[kind="primary"] {
        display: block !important;
        margin-left: auto !important;
        margin-right: auto !important;
        max-width: 300px !important;   /* keep it compact */
        width: 100% !important;        /* still responsive on mobile */
    }

    
    /* Symptom buttons - single style for all groups */
    button.symptom-btn {
        background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%) !important;
        color: #000000 !important;
        border-radius: 25px !important;
        padding: 12px 20px 12px 45px !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        border: none !important;
        width: 100% !important;
        margin: 5px 0 !important;
        position: relative !important;
        text-align: left !important;
        transition: all 0.3s ease !important;
    }
    
    button.symptom-btn:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
        background: linear-gradient(135deg, #e8e8e8 0%, #d8d8d8 100%) !important;
    }
    
    button.symptom-btn.selected {
        background: linear-gradient(135deg, #a8e6cf 0%, #88d3ba 100%) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2) !important;
    }
    
    button.symptom-btn.selected::before {
        content: "✓" !important;
        position: absolute !important;
        left: 20px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        font-weight: bold !important;
        font-size: 16px !important;
        color: #1a3c2b !important;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #fff5f5 0%, #ffecec 100%);
        border-radius: 15px;
        padding: 35px 25px;  /* Increased vertical padding */
        margin: 40px 0;       /* More vertical space around the box */
        border-left: 6px solid #ff6b6b;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        font-size: 1.1rem;
        font-weight: 500;
        line-height: 1.7;
        color: #660000;
    }

    
    .resource-box {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe6ee 100%);
        border-radius: 15px;
        padding: 18px;
        margin: 15px 0;
        border-left: 5px solid #ff85a2;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    .title {
        color: #d23669;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .symptom-group {
        background: linear-gradient(180deg, #ffdfdf 70%, #ffc9c9 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .header {
        color: #9A3141 !important;
        font-weight: 800 !important;
        font-size: 1.3rem !important;  
        margin-bottom: 15px;
    }
    
    /* Remove background from disclaimer and make text black */
    .disclaimer-container {
        background: transparent !important;
        color: #000000 !important;
        border: 1px solid #ff6b6b;
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
    }
    
    .disclaimer-container .stMarkdown {
        color: #000000 !important;
    }
    
    /* Make sure text is visible on the gradient background */
    .stMarkdown, .stText {
        color: #333333;
    }
    
    /* Custom styling for subheaders - make them black */
    .stSubheader {
        color: #000000 !important;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Title container with image */
    .title-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 2rem;
    }
    
    .title-text {
        flex: 1;
    }
    
    .title-image {
        margin-left: 2rem;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem 2rem;
        }
        
        .title-container {
            flex-direction: column;
        }
        
        .title-image {
            margin-left: 0;
            margin-top: 1rem;
        }
    }

    .recommendation-box {
        background: #ffecec;
        color: #222222 !important;
        font-size: 1rem;
        font-weight: 500;
        border-left: 5px solid #d23669;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }

    /* Checkbox as button (symptom) with hover lift and glow */
    div.stCheckbox > label {
        width: 100% !important;
        background: linear-gradient(135deg, #c97ba0 40%, #e6789b 60%);
        color: #000000 !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    /* Hover effect with lift and glow */
    div.stCheckbox > label:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(255, 105, 105, 0.5) !important;
        background: linear-gradient(135deg, #e6789b 40%, #c97ba0 60%) !important; /* subtle gradient shift on hover */
    }
    
    /* Checked state keeps the selection color but also lifts */
    div.stCheckbox input:checked + span {
        font-weight: 600 !important;
        color: #1a3c2b !important;
    }
    
    div.stCheckbox input:checked + span::before {
        content: "✓ " !important;
        font-weight: bold !important;
    }


    /* Custom thin separator */
    .custom-separator {
        border-top: 2px solid #d23669;
        margin: 30px 0;
        opacity: 0.4;
    }

    .results-container {
        background: #fff7f7;
        padding: 30px;
        margin: 50px 0;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(255, 105, 105, 0.15);
    }


    </style>
    """, unsafe_allow_html=True)