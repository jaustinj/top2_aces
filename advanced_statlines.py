import pandas as pd 


PA_lambda = lambda row: row.AB + row.BB + row.HBP + row.SH + row.SF
OBP_lambda = lambda row: (row.H + row.BB + row.HBP) / (row.PA) if row.PA > 0 else 'NaN'
AVG_lambda = lambda row: row.H / row.AB if row.AB > 0 else 'NaN'

stat_functions = [['pa', PA_lambda], ['obp',OBP_lambda], ['avg', AVG_lambda]]
def format_df(df):
    for func in stat_functions:
        df[func[0]] = df.apply(func[1], axis=1)
def order_by(df, sort_column, ascending_val):
    if ascending_val == 'yes':
        ascending_val=True
    else:
        ascending_val=False
    df.sort_values(by=sort_column, inplace=True, ascending=ascending_val)
    df.reset_index(drop=True, inplace=True)