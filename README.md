# EndoDx: Symptom-Based Risk Screening for Endometriosis

**EndoDx** is a web-based prototype developed to demonstrate the practical utility of machine learning in non-invasive, early risk screening for endometriosis using only self-reported symptoms.

---

## Prototype Preview

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/546b3b43-01cd-42d5-a37a-9a4d1604d489" width="450" alt="EndoDx Screenshot 1"/></td>
    <td><img src="https://github.com/user-attachments/assets/d7a72421-5708-4b8f-a9c3-5c8f8e55068c" width="450" alt="EndoDx Screenshot 2"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2243f141-f8cd-4337-84fc-444acca38d98" width="450" alt="EndoDx Screenshot 3"/></td>
    <td><img src="https://github.com/user-attachments/assets/7d00e828-523f-4d49-a4d4-3753cffc26b9" width="450" alt="EndoDx Screenshot 4"/></td>
  </tr>
</table>

---

## Background

Endometriosis is a complex, often misdiagnosed gynecological condition affecting approximately 10% of reproductive-age women. Diagnosis typically involves invasive procedures and lengthy delays due to the variability of symptoms and lack of reliable screening tools. This project investigates how machine learning can support faster, non-invasive risk assessment based on symptom data alone.

---

## Project Goals

- Explore machine learning approaches to classify endometriosis risk.
- Evaluate both traditional and advanced models.
- Integrate the best-performing model into a deployable prototype.
- Provide an accessible tool to demonstrate real-world applicability.

---

## Methodology

The project builds upon the **EndoDetect** dataset, focusing solely on self-reported symptoms. The following models were trained and evaluated:

- **Traditional Models**: Logistic Regression, Decision Tree, Random Forest  
- **Advanced Models**: Support Vector Machine (SVM), XGBoost, Multilayer Perceptron (MLP)

### Feature Selection Strategies

1. **Unified Statistical Baseline** (e.g., chi-square)  
2. **Model-Specific Optimization** (e.g., recursive feature elimination)

### Evaluation Metrics

- F1-score  
- Area Under the ROC Curve (AUC)  
- Specificity  
- Matthews Correlation Coefficient (MCC)  
- Stratified 5-fold cross-validation

---

## Results

The **Support Vector Machine (SVM)** achieved the highest performance among 3 tested Models:

- **F1 Score**: 0.9524  
- **AUC**: 0.9852  

Grouped features reduced performance, emphasizing the importance of detailed, granular symptom input.

---

## Application: EndoDx Prototype

The best-performing model was integrated into a user-facing web application — **EndoDx** — built to showcase the feasibility of real-world deployment. Users input symptoms via a structured form, and the application returns a model-predicted risk score.

---

## Key Contributions

- Demonstrates the effectiveness of machine learning in symptom-only risk screening.  
- Offers a scalable and accessible approach to reduce diagnostic delays.  
- Combines robust modelling techniques with a practical, user-friendly interface.  

---

## Technologies Used

- Python (scikit-learn, XGBoost)  
- Streamlit (for prototype deployment)  
- pandas, NumPy, matplotlib (for data processing and visualization)  

