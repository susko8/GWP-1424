import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

log_df = pd.read_csv("statuslog1.csv")

supportProjectIds = log_df['supportprojectstatuslog2supportproject'].unique()

missingLogs = []

for supportProjectId in supportProjectIds:
    projectStatusLogs = log_df.loc[log_df['supportprojectstatuslog2supportproject'] == supportProjectId]
    if 100 not in projectStatusLogs['previousstatus'].tolist():
        if 0 not in projectStatusLogs['previousstatus'].tolist():
            firstRow = projectStatusLogs.iloc[0].copy()
            firstRow['previousstatus'] = 100
            firstRow['currentstatus'] = 1
            missingLogs.append(firstRow)

