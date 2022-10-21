<h1>Простой калькулятор на FastApi</h1>

<h2>API:</h2>

Вычислить значение выражения:

GET

```sh
/eval?phrase=1-1
```
Ответ:
```sh
1-1 = 0
```

POST

```sh
/eval
```
Тело запроса:
```sh
{"phrase":"1+1"}
```
Ответ:
```sh
{"result":"1-1 = 0"}
```
<h2>Установка:</h2>


```sh
pip install requerments.txt
```


<h2>Запуск:</h2>


```sh
uvicorn main:app --reload
```



