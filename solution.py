import pandas as pd
import numpy as np


chat_id = 163596104 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pval = sps.ks_2samp(x, y, alternative="two-sided").pvalue
    effect = (pval < 0.09)
    
    return effect

