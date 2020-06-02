## import modules here 
import pandas as pd
import numpy as np
import helper
################### Question 1 ###################
 
def buc_rec_optimized(df):  # do not change the heading of the function
    df2 = pd.DataFrame(columns=df.columns)
    buc(df, [], df2)
    return df2
 
def buc(df, pre, df2):
    if df.shape[0] == 1:
        binLst = [bin(i)[3:] for i in range(2**df.shape[1],2**(df.shape[1]+1),2)]
        for s in binLst:
            tmpLst = ['ALL' if s[i]=='1' else list(df.iloc[0])[i] for i in range(len(s))]
            tmpLst = pre + tmpLst
            df2.loc[len(df2)] = tmpLst
 
    elif df.shape[1] == 1:
        _pre = pre.copy()
        _pre.append(sum(helper.project_data(df, 0)))
        df2.loc[len(df2)] = _pre
 
    else:
        valLst = sorted(list(set(helper.project_data(df, 0).values)))
        _pre = pre.copy()
        for val in valLst:
            subdf = helper.slice_data_dim0(df, val)
            pre_ = _pre.copy()
            pre_.append(val)
            buc(subdf, pre_, df2)
        subdf = helper.remove_first_dim(df)
        pre_ = _pre.copy()
        pre_.append('ALL')

        buc(subdf, pre_, df2)
