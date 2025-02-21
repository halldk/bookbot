def get_word_count(data:str):
    return len(data.split())

def get_char_stats(data:str):
    stat = {}
    for char in data.lower():
        ent = stat.get(char)
        if ent:
            stat.update({char: ent+1})
        else:
            stat.update({char: 1})
    return stat

def sort_on(dict):
    return list(dict.values())[0]

def generate_report(chars:dict):
    s_list = list()
    for key, value in chars.items():
        s_list.append({key: value})
    s_list.sort(key=sort_on, reverse=True)
    return s_list

