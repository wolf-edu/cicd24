"""
    Easy Azure Streamlit Demo
    Author: Wolf Paulus (wolf@paulus.com)
"""
from random import randint
import streamlit as st
from log import logger


def ui(items: [int]) -> None:

    st.title("Streamlit Demo v1.0.")
    st.subheader(".. on Azure")
    st.line_chart(items)


if __name__ == "__main__":
    data = [randint(0, 10) for _ in range(25)]
    logger.info(f"Created a list with {len(data)} items.")
    ui(data)
