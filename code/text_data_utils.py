def generate_data_replace_string():
    '''
    为了将日期字符串 /2/5 转换成 0205这样,
    构建一个map,key为原始字符串,value为目标字符串
    :return:
    date_replace_str_map
    '''
    ori_str_list = []
    new_str_list = []
    for idx in range(1,9):
        str_num = '/'+str(idx);
        new_str_num = '0'+str(idx);
        ori_str_list.append(str_num);
        new_str_list.append(new_str_num);

    ori_str_map = {k:v+1 for v,k in enumerate(ori_str_list)}
    date_replace_str_map= {k:new_str_list[idx] for idx,k in enumerate(ori_str_map.keys())}

    ori_str_list = []
    new_str_list = []
    for idx in range(10,32):
        str_num = '/' + str(idx);
        new_str_num = str(idx)
        ori_str_list.append(str_num)
        new_str_list.append(new_str_num)

    ori_str_map = {k:v+1 for v,k in enumerate(ori_str_list)}
    replace_str_map_part2= {k:new_str_list[idx] for idx,k in enumerate(ori_str_map.keys())}

    for key in replace_str_map_part2.keys():
        date_replace_str_map[key] = replace_str_map_part2.get(key)

    #print(replace_str_map)
    return date_replace_str_map

def generate_time_replace_string():
    '''
    为了将日期字符串 ' 0:05' 转换成 '0005' 这样,
    构建一个map,key为原始字符串,value为目标字符串
    :return:
    time_replace_str_map
    '''
    ori_str_list = []
    new_str_list = []
    for idx in range(9):
        str_num = ' '+str(idx) + ':';
        new_str_num = '0'+str(idx);
        ori_str_list.append(str_num);
        new_str_list.append(new_str_num);

    ori_str_map = {k:v+1 for v,k in enumerate(ori_str_list)}
    time_replace_str_map= {k:new_str_list[idx] for idx,k in enumerate(ori_str_map.keys())}

    ori_str_list = []
    new_str_list = []
    for idx in range(10,24):
        str_num = ' ' + str(idx) + ':';
        new_str_num = str(idx)
        ori_str_list.append(str_num)
        new_str_list.append(new_str_num)

    ori_str_map = {k:v+1 for v,k in enumerate(ori_str_list)}
    replace_str_map_part2= {k:new_str_list[idx] for idx,k in enumerate(ori_str_map.keys())}

    for key in replace_str_map_part2.keys():
        time_replace_str_map[key] = replace_str_map_part2.get(key)

    #print(replace_str_map)
    return time_replace_str_map