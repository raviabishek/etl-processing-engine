from src.app.job.sales.modules.extract import extract
from src.app.job.sales.modules.transform import transform
from src.app.job.sales.modules.load import load

df = extract()
t_df = transform(df)
load(t_df)