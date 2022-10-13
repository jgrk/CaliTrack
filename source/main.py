from email import header
import pandas as Pd

file_dir="/Users/erikduvander/Documents/Projects/Python/CaliTrack/source/nutrients.csv"

p=Pd.read_csv(file_dir)

print(p.loc[p["Food"]=="milk"])

