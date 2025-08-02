# World Health Organization (WHO) air polution interactive visualization

This project combines data preprocessing, visualization and creation of a web application with interactive graphs.

### **Dataset**
**Air pollution: Burden of disease attributed to air pollution (per 100 000 age-standardized), ambient and household - an open-source real data csv file, published by World Health Organisation (WHO)**

I have decided to use joint dataset due to the next comment:

> *The joint disease burden figures from ambient and household air pollution may not be equal to the sum of their independent impacts since household air pollution is emitted into the ambient environment and therefore contributes to ambient air pollution exposure and related burden of disease, therefore it’s necessary to apply a specific method to minimize the risk of double counting the health impacts.*

As we can see, it would be harder to destinguish 2 categories precisely, as one contributes to another and I have decided that comparison of household and ambient pollution would not be fair due to this factor, thus choosing joint dataset for my project.

### **Technology used**
- EDA in Python (numpy, pandas, plotly)
- Jupyter notebook



### **Project structure**   
```
air-pollution-analysis/
├── app.py
├── data/
│   └── data.csv            # given raw dataset
│   └── cleaned_data.csv    # dataset after preprocessing
├── notebooks/
│   └── data_analysis.ipynb    # notebook for preprocessing
├── requirements.txt
├── Procfile
├── README.md
```
