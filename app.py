import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import fastf1
import fastf1.plotting
from fastf1.events import get_event_schedule
import os

# Create cache directory if it doesn't exist
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')

year = 2025 
season = get_event_schedule(year)
race_names = season['EventName'].unique()
df = pd.DataFrame()
# print(all_laps)
for race in race_names[:2]:
    session = fastf1.get_session(2023, race, 'R')
    session.load()
    df = pd.concat([df, session.laps])



df_driver = df['Driver'].unique()

print(df_driver)

