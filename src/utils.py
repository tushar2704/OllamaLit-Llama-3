##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##OllamaLit [https://github.com/tushar2704/OllamaLit] (https://github.com/tushar2704/OllamaLit)
#######################################################################################################
#Importing dependecies
#######################################################################################################
import os
import sys
import ollama
import streamlit as st
from openai import OpenAI
from logging import getLogger

logger = getLogger(__name__)

#######################################################################################################










def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the models information.

    :param models_info: A dictionary containing the models' information.

    Return:
        A tuple containing the model names.
    """

    return tuple(model["name"] for model in models_info["models"])