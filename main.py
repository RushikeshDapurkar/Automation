import os
from webcraping import File_Updater
import re


File_Updater._find_words('webcraping/files')


# files = os.listdir('webcraping/files')
# to_file = f'webcraping/new'

# print(files)
# for f in files:
# results = File_Updater._removing_duplicates(
#     f'webcraping/files/{f}')
# print(results)
# results = File_Updater._sorting_words_leng(
#     f'webcraping/files/{f}')
# print(results)

# results = File_Updater._updating_words(
#     f'webcraping/present/{f}', 'webcraping/files')
# print(results)
