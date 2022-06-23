import seaborn
import streamlit as st
from matplotlib import pyplot as plt

from matrix import Matrix


def input_validation(func):
    def wrapper(user_input):
        if user_input < 7 or user_input > 1000:
            user_input = 7
        return func(user_input)

    return wrapper


@input_validation
def set_size(user_input):
    return user_input


with st.form("Heart Creation"):
    st.write("Give heart-matrix size")
    matrix_size = set_size(int(st.number_input('Insert a number greater than 7')))

    submitted = st.form_submit_button("Submit")
    if submitted:
        heart = Matrix(matrix_size)
        heart.draw_half_heart()
        heart.make_heart()

        fig, ax = plt.subplots()
        seaborn.heatmap(heart.matrix, ax=ax, vmin=0, vmax=2)
        st.write(fig)
