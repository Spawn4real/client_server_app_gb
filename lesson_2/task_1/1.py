import csv
import re
import chardet
task_files = ('info_1.txt', 'info_2.txt', 'info_3.txt')


def get_data(files):

    os_prod_list = []
    os_code_list = []
    os_name_list = []
    os_type_list = []
    main_data = []

    for i in files:
        with open(i, 'rb') as my_files:
            b_data = my_files.read()
            result = chardet.detect(b_data)
            data = b_data.decode(result['encoding'])

        os_prod_re = re.compile(r'Изготовитель системы: \s*\S*')
        os_prod_list.append(os_prod_re.findall(data)[0].split()[2])

        os_name_re = re.compile(r'Windows: \s\S*')
        os_name_list.append(os_name_re.findall(data)[0])

        os_type_re = re.compile(r'Тип системы: \s*\S*')
        os_type_list.append(os_type_re.findall(data)[0].split()[2])

        os_code_re = re.compile(r'Код продукта: \s*\S*')
        os_code_list.append(os_code_re.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Windows', 'Тип системы', 'Код продукта']
    main_data.append(headers)
    data_for_rows = (os_prod_list, os_name_list, os_type_list, os_code_list)
    main_data.append(data_for_rows)

    for idx in range(len(data_for_rows[0])):
        line = [row[idx] for row in data_for_rows]
        main_data.append(line)
    return main_data


def write_to_csv(out_file):
    main_data = get_data(task_files)
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report.csv')
