import pandas as pd
import json

line = "I3FA31ASSYL"
df = pd.read_excel("D:/Program Files (x86)/web/211.xls", engine="xlrd")
line_fail_detail = (
    df.loc[df["TEST_LINE"] == line]
    .groupby(["MODEL_NAME", "ERROR_DESC"])["TEST_LINE"]
    .count()
    .sort_values(ascending=False)
).reset_index().to_dict(orient="records")
# 遍历时直接把元组解包成两个变量
print(line_fail_detail)

