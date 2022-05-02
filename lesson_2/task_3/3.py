import yaml

data_files = {
    'items': ['computer', 'printer', 'gamepad'],
    'quantity': 5,
    'price': {
        'computer': '100₽',
        'printer': '200₽',
        'gamepad': '300₽'
        }
}
with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data_files, f_in, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as f_out:
    data_yaml = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data_files == data_yaml)