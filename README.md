# World Health Organization (WHO) air polution interactive visualization
This project provides an interactive web application to visualize the burden of disease attributable to air pollution globally, using open data from the World Health Organization (WHO).

---

## **Dataset**
**Air pollution: Burden of disease attributed to air pollution (per 100 000 age-standardized), ambient and household - an open-source real data csv file, published by World Health Organisation (WHO)**

I have decided to use joint dataset due to the next comment:

> *The joint disease burden figures from ambient and household air pollution may not be equal to the sum of their independent impacts since household air pollution is emitted into the ambient environment and therefore contributes to ambient air pollution exposure and related burden of disease, therefore it’s necessary to apply a specific method to minimize the risk of double counting the health impacts.*

As we can see, it would be harder to destinguish 2 categories precisely, as one contributes to another and I have decided that comparison of household and ambient pollution would not be fair due to this factor, thus choosing joint dataset for my project.

---

## Technologies Used

* Data processing and exploratory data analysis: Python (NumPy, Pandas, Plotly)
* Interactive visualization web app: Streamlit
* Jupyter Notebook for data cleaning and analysis
* Deployment: Streamlit Community Cloud

---

## Project Structure

```
air-pollution-analysis/
├── app.py                  # Streamlit web app source code
├── data/
│   ├── data.csv            # Raw WHO air pollution dataset
│   └── data_cleaned.csv    # Preprocessed and cleaned data
├── notebooks/
│   └── data_analysis.ipynb # Data preprocessing and EDA notebook
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## How to Use

### Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/air-pollution-analysis.git
   cd air-pollution-analysis
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and visit `http://localhost:8501` to interact with the dashboard.

---

### Access Online

The app is deployed on Streamlit Community Cloud and can be accessed here:

[https://air-polution-interactive-visualization.streamlit.app/](https://air-polution-interactive-visualization.streamlit.app/)

---

## Features

* Select one or multiple countries to compare
* Choose specific diseases attributable to air pollution
* Filter by year and sex
* Interactive line charts showing Disability-Adjusted Life Years (DALYs) per 100,000 population over time
* Faceted visualization for multiple countries

## License

This project is open-source and available under the MIT License.
