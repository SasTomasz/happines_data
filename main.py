import streamlit as st
import plotly.express as px
import pandas as pd


def get_data():
    df = pd.read_csv("./data/happy.csv")
    return df


if __name__ == '__main__':
    st.title("In search for Happiness")

    input_data_label = {"GDP": "gdp", "Generosity": "generosity", "Happiness": "happiness",
                        "Social Support": "social_support", "Life Expectancy": "life_expectancy",
                        "Freedom of choices": "freedom_to_make_life_choices", "Corruption": "corruption"}
    x_axis = st.selectbox("Select the data for the X-axis", input_data_label.keys())
    y_axis = st.selectbox("Select the data for the Y-axis", input_data_label.keys(), index=2)

    st.subheader(f"{x_axis} and {y_axis}")
    data = get_data()

    figure = px.scatter(data, x=input_data_label[x_axis], y=input_data_label[y_axis],
                        labels={input_data_label[x_axis]: x_axis, input_data_label[y_axis]: y_axis})
    st.plotly_chart(figure)

