import os
import File_Updater
import re

files = os.listdir('files')
# to_file = f'new'

# print(files)

'''Finding Words From A Particular Folder As per Name Of The File----'''

# File_Updater._find_words('files')

'''Removing Dupicates, Sorting, Updating New Words From 
 Multiple Files Present In Particular Folder-------------------------'''

for f in files:
    results = File_Updater._removing_duplicates(
        f'files/{f}')
    print(results)
#     results = File_Updater._sorting_words_leng(
#         f'files/{f}')
#     print(results)
#     results = File_Updater._updating_words(
#         f'present/{f}', 'files')
#     print(results)

'''Updating Words From Single File-----------------------------------'''

# results = File_Updater._updating_words(
#     f'present/{f}', 'files')
# print(results)


'''Checking New words in file-----------------------------------------'''

# for f in files:
#     url = f'https://www.dictionary.com/browse'
#     tag = 'h1'
#     from_file = 'files/' + f
#     to_path = 'backup'
#     results = File_Updater._checking_words(from_file, url, tag)
#     present, not_present = results[0], results[1]
#     File_Updater._save_checked_words(to_path, present, not_present)
