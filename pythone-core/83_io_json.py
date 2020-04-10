"""
существует всего один модуль json для работы с данным форматом файлов
https://python-scripts.com/json

Тестирование JSON: http://echo.jsontest.com/insert-key-here/insert-value-here/key/value
https://jsonplaceholder.typicode.com/

"""
import json
import requests

json_obj = \
{
	"breakfast": {
		"hours": "7-11",
		"items": {
			"breakfast burritos": "$6.00",
			"pancakes": "$4.00"
		}
	},
	"lunch": {
		"hours": "11-3",
		"items": {
			"hamburger": "$5.00"
		}
	},
	"dinner": {
		"hours": "3-10",
		"items": {
			"spaghetti": "$8.00"
		}
	}
}

# сериализация
with open("test_data_file.json", "wt") as write_file:
    json.dump(json_obj, write_file)  # запишем json в файл

json_string = json.dumps(json_obj, indent=4, separators=(', ', ': '))  # c json можно работать как со строкой. indent - это форматирование - определяет размер отступа
                                                                       # separators - это кортеж используемых разделителей
print('Сериализованный JSON: ', json_string)

# Десериализация JSON - превращает исходные данные в объект Python
with open("test_data_file.json", "r") as read_file:
    data = json.load(read_file)

print('Десериализованный JSON: ', data)

#
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)  # получаем список словарей
print(todos == response.json())  # True
print(type(todos))  # <class 'list'>

print('QQQ: ', todos[:2])  # распечатать первые два элемента списка