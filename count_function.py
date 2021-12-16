import os, time
import pandas as pd
import datetime

file_count = sum(len(files) for _, _, files in os.walk(r'path'))
print(file_count)

c = 0
files_list = ['File Path']
ctime_list = ['Date Created']
mtime_list = ['Date Modified']
selection_to_output_df = pd.DataFrame({})

for root, _, filenames in os.walk(r'path'):
    try:
        for filename in filenames:
            file_path   = root + '/' + filename
            created     = os.path.getctime(file_path)
            modified    = os.path.getmtime(file_path)
            files_list.append(file_path)
            ctime_list.append(datetime.datetime.strptime(time.ctime(created), "%a %b %d %H:%M:%S %Y"))
            mtime_list.append(datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y"))
            c += 1
    except:
        print("fail to find")

files_df = pd.DataFrame({'File Path': files_list[1:]})
selection_to_output_df = pd.concat([selection_to_output_df, files_df], axis=1)
created_df = pd.DataFrame({'Date Created': ctime_list[1:]})
selection_to_output_df = pd.concat([selection_to_output_df, created_df], axis=1)
modified_df = pd.DataFrame({'Date Modified': mtime_list[1:]})
selection_to_output_df = pd.concat([selection_to_output_df, modified_df], axis=1)
all_files_list = []
for sublist in files_list[1:]:
    for item in sublist:
        all_files_list.append(item)

print(selection_to_output_df)

writer2 = pd.ExcelWriter("dataframe2.xlsx", engine='xlsxwriter')
selection_to_output_df.to_excel(writer2, index=False)
writer2.save()
