import pandas as pd
import numpy as np
import scipy.stats as sps

chat_id = 163596104 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pvalue = sps.anderson_ksamp([x, y]).pvalue
    effect = (pvalue < 0.09)
    
    return effect

