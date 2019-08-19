import pandas as pd


#my import
import text_data_utils as tdu

warning_df = pd.read_csv('./train_warning_utf8.csv', header=0 ,sep=',',index_col=None ) #用0行作为标题
warning_df.rename(columns = {'告警开始时间':'time',
                            '告警标题':'warning',
                             '基站eNBID或小区ECGI':'cell_id'
                            },inplace=True)
#print(warning_df.head(3))

#reshape the time format
date_replace_map = tdu.generate_data_replace_string();
date_replace_keys = date_replace_map.keys()
date_replace_values = []
for the_key in date_replace_keys:
    date_replace_values.append(date_replace_map.get(the_key))

time_replace_map = tdu.generate_time_replace_string();
time_replace_keys = time_replace_map.keys()
time_replace_value = []
for the_key in time_replace_keys:
    time_replace_value.append(time_replace_map.get(the_key))
warning_df['time'].replace(date_replace_keys,date_replace_values, regex=True, inplace=True)
warning_df['time'].replace(time_replace_keys,time_replace_value, regex=True, inplace=True)

print(warning_df.head(3))