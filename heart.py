import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import streamlit as st


def mirror(seq):
    output = list(seq[::-1])
    output.extend(seq[1:])
    return output


sns.set_theme()
with st.form("Heart Creation"):
    st.write("Give size")
    size = int(st.number_input('Insert a number greater than 7'))
    if size < 7 or size > 1000:
        size = 7
    submitted = st.form_submit_button("Submit")
    if submitted:
        third = int(size * 0.33)
        matrix = np.zeros((third * 3, size), dtype=int)
        heart_size = size - 1

        for m in matrix:
            stamps = [abs(heart_size - third * 2), heart_size]
            m[stamps[0]] = 1
            m[stamps[1]] = 1

            heart_size -= 1
            if stamps[0] == stamps[1]:
                break

        heart = np.asarray(mirror(matrix)).transpose()
        fig, ax = plt.subplots()
        sns.heatmap(heart, ax=ax, vmin=0, vmax=2)
        st.write(fig)
