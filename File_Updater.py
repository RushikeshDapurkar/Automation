import keyboard
import time
import requests
import re
from bs4 import BeautifulSoup
import html5lib
from pynput.mouse import Controller, Button
mouse = Controller()


def _reading_file(_file):
    try:
        read_file = open(f'{_file}', 'r')
        read_from = ''.join(read_file)
        files_words_list = read_from.split()
        read_file.close()
    except Exception as e:
        files_words_list = [f'Error  =>  {e}']
    return files_words_list


def _emptying_file(_file_path):
    fw = open(f'{_file_path}', 'w')
    fw.write('')
    fw.close()
    return f'Done Emptying File For Saving Whatever You Like.'


def _create_new(_from_file, _to_path):
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        print(from_words[0])
        exit()

    for word in from_words:
        _to_file = f"{_to_path}/{word[0]}.txt"

        file1 = open(_to_file, "a")  # append mode
        file1.write(word+' ')
        file1.close()
    return f'Done Adding'


def _updating_words(_from_file, _to_path):
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        print(from_words[0])
        exit()

    for word in from_words:
        if len(word) > 7:
            _to_file = f"{_to_path}/{word[0]}.txt"
            # to_words = _reading_file(f'files/{word[0]}.txt')
            to_words = _reading_file(_to_file)
            if len(to_words) > 1:
                pass
            else:
                print(to_words[0])
                exit()
            if word not in to_words:
                fw = open(_to_file, 'a')
                fw.write(' '+word+' ')
                fw.close()
        else:
            break
    return f'Done Updating Words, File Added to given location. ==> {_to_path}'


def _removing_duplicates(_from_file, _to_path=None):
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        print(from_words[0])
        exit()
    from_words = set(from_words)
    from_words = list(from_words)

    if _to_path == None:
        _emptying_file(_from_file)
    for word in from_words:
        if len(word) > 7:
            word = word.lower()
            if _to_path != None:
                fw = open(f'{_to_path}/{word[0]}.txt', 'a')
                fw.write(word+' ')
                fw.close()
            else:
                fw = open(f'{_from_file}', 'a')
                fw.write(word+' ')
                fw.close()
        else:
            break
    return f'Done Removing Duplicates, File Added to given location.==> {_from_file}'


def _filtering_words(_from_file, _to_path=None):
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        print(from_words[0])
        exit()
    if _to_path == None:
        _emptying_file(_from_file)
    for word in from_words:
        if len(word) > 7:
            if _to_path != None:
                try:
                    length = len(word)
                    int(word[length-2:])
                    word = word[:length-2]
                except Exception:
                    word = word
                fw = open(f'{_to_path}/{word[0]}.txt', 'a')
                fw.write(word+' ')
                fw.close()
            else:
                fw = open(f'{_from_file}', 'a')
                fw.write(word+' ')
                fw.close()
        else:
            break
    return f'Done Filtering, File Added to given location.'


def _sorting_words_leng(_from_file, _to_path=None):
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        print(from_words[0])
        exit()
    from_words.sort(key=len, reverse=True)

    if _to_path == None:
        fw = open(f'{_from_file}', 'w')
        fw.write('')
        fw.close()
    for word in from_words:
        if len(word) > 7:
            if _to_path != None:
                fw = open(f'{_to_path}/{word[0]}.txt', 'a')
                fw.write(word+' ')
                fw.close()
            else:
                fw = open(f'{_from_file}', 'a')
                fw.write(word+' ')
                fw.close()
        else:
            break
    return f'Done Sortering, File Added to given location. ==> {_from_file}'


def _get_words_list(_from_path, _words_list, _used_list=None, _delete_list=None):
    _from_file = f'{_from_path}/{_words_list[0]}.txt'
    from_words = _reading_file(_from_file)
    if len(from_words) > 1:
        pass
    else:
        exit()

    if (_used_list == None) and (_delete_list == None):
        words = [i for i in from_words
                 if (_words_list[1] not in i) and (_words_list[2] not in i)]
    else:
        words = [i for i in from_words
                 if (_words_list[1] not in i) and (_words_list[2] not in i) and (i not in _used_list) and (i not in _delete_list)]
    return words


def _validate_command(_cmd, _optn_list, _used_list, _delete_list):
    try:
        _cmd[0] = int(_cmd[0])
        return ['repeat']
    except Exception:
        _cmd[0] = _cmd[0]
    if (len(_cmd) == 3) and (len(_cmd[0]) == 1) and (len(_cmd[1]) == 1) and (len(_cmd[2]) == 1):
        return 'Go'

    elif 'res' in _cmd:
        _used_list.clear()
        print('Game Restarted ==>')
        return ['restart_game']

    elif 'exit' in _cmd:
        print('Used =', _used_list)
        print('Delete =', _delete_list)
        exit()

    elif ('da' in _cmd):
        try:
            pos = int(_cmd[1])-1
            _delete_list.add(_optn_list[pos])
            return ['deleted', _delete_list]
        except Exception:
            return ['repeat']

    elif ('ad' in _cmd):
        try:
            pos = int(_cmd[1])-1
            _used_list.add(_optn_list[pos])
            return ['used', _used_list]
        except Exception:
            return ['repeat']
    else:
        return ['repeat']


def _find_words(_from_path):
    used = set()
    delete = set()
    option = []
    path = _from_path
    while True:
        print()
        _cmd = input().split()
        print('''<-------->
    ''')
        _action = _validate_command(_cmd, option, used, delete)
        if _action == 'Go':
            pass
        else:
            continue
        words = _get_words_list(
            _from_path=path,  _words_list=_cmd, _used_list=used, _delete_list=delete)

        words.sort(key=len, reverse=True)
        counter = 0
        try:
            lenn = len(words[0])
        except Exception:
            continue
        len_store = []
        option = []
        for word in words:
            if counter == 12:
                break
            if len(word) < lenn:
                lenn = len(word)
            if len(word) >= 10:
                if (len(word) == lenn):
                    option.append(word)
                    print(' '*25,
                          f"{counter+1}. {word} ({len(word)}) ")
                    print(end=' '*40)

                    len_store.append(len(word))
                    counter += 1

                    lenth_of_legth_store = len(len_store)-1
                    length = len_store[lenth_of_legth_store]
                    coun = len_store.count(length)

                    if coun > 1:
                        lenn -= 1
                    if counter % 2 == 0:
                        print()
            else:
                break
        print()
        print('-'*130)


def _get_position():
    key_dict = {}
    while True:
        if keyboard.is_pressed('escape'):
            print(f'Exit')
            break
        else:
            key_dict[keyboard.read_key()] = mouse.position
            time.sleep(0.5)
    return key_dict


def __mouse_clicker(_list_pos, _sleep_for=None):
    if (_sleep_for != None) and (_sleep_for is int):
        time.sleep(_sleep_for)
    for pos in _list_pos:
        mouse.position = pos
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
    return f'Done Clicking'


def _add_data_from_web(_url, _find):
    page = requests.get(_url).text
    soup = BeautifulSoup(page, 'html.parser')

    # Method For Find Data Use Class or Id for Better Results
    # find_tag = soup.findAll(_find, _class='')
    find_tag = soup.find(_find)

    return find_tag
