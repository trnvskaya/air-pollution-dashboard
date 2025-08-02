import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
data = pd.read_csv('data/data_cleaned.csv')

st.title("Air Pollution Disease Dashboard")
st.markdown("""This interactive dashboard visualizes the burden of disease attributed to **air pollution**, using open data published by the **World Health Organization (WHO)**.

You can explore trends in **Disability-Adjusted Life Years (DALYs)** per 100,000 people by filtering for:
- Country
- Disease type
- Sex
- Year""")

# Sidebar filters
countries = st.multiselect("Select country/countries", options=sorted(data['Location'].unique()), default=["Japan"])
diseases = st.multiselect("Select disease(s)", options=sorted([col for col in data.columns if col not in ['ParentLocation', 'Location', 'Year', 'IsLatestYear', 'Sex']]), default=["Stroke"])

year_min, year_max = st.slider(
    "Select year range",
    min_value=int(data['Year'].min()),
    max_value=int(data['Year'].max()),
    value=(int(data['Year'].min()), int(data['Year'].max())),
    step=1
)
years = list(range(year_min, year_max + 1))
sexes = st.multiselect("Select sex(es)", options=sorted(data['Sex'].unique()), default=["Female"])

# Filter data
filtered = data[
    data['Location'].isin(countries) &
    data['Year'].isin(years) &
    data['Sex'].isin(sexes)
]

if not diseases:
    st.warning("Please select at least one disease.")
else:

    if "Cataracts" in diseases:
        cataracts_null = filtered["Cataracts"].isnull().sum() + (filtered["Cataracts"] == 0).sum()
        if cataracts_null / len(filtered) > 0.5:
            st.warning("Be careful: There are a lot of missing or zero values for Cataracts. The graph may not display true statistics due to lack of data.")
            
    plot_data = filtered.melt(
        id_vars=['Location', 'Year', 'Sex'],
        value_vars=diseases,
        var_name='Disease',
        value_name='DALYs'
    )
    plot_data['Year'] = pd.to_numeric(plot_data['Year'], errors='coerce')
    plot_data = plot_data.sort_values('Year')

    fig = px.line(
        plot_data,
        x="Year",
        y="DALYs",
        color="Disease",
        line_dash="Sex",
        facet_col="Location" if len(countries) > 1 else None,
        markers=True,
        title="DALYs per 100,000 by Disease, Country, Sex, and Year"
    )

st.plotly_chart(fig, use_container_width=True)   