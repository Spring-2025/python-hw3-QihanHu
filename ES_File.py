# -*- coding: utf-8 -*-
"""ES_File.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mmaNKF-29j_luWybLq5WBHvnwQJsIE4Y
"""

import numpy as np

def ES(losses, confidence=None, VaR=None):

    if VaR is None:
        if confidence is None:
            raise ValueError("Either confidence or VaR must be provided.")

        VaR = np.percentile(losses, 100 * (1 - confidence))


    es_value = np.mean(losses[losses > VaR])
    return es_value

u = np.random.uniform(0, 100, 100000)



es_confidence = ES(losses=u, confidence=0.8)
print('ES with confidence:', np.round(es_confidence, 0) == 90)

es_var = ES(losses=u, VaR=80)
print('ES with VaR:', np.round(es_var, 0) == 90)