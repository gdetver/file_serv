Примеры запросов для использования API


POST запрос для отправки файла на сервер

curl --request POST \
  --url http://localhost:8080/upload \
  --header 'Postman-Token: f0ea3ffe-0ff3-4e21-8a9c-1887feb38a8f' \
  --header 'cache-control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form '=./bday-179.gif'
  
GET запрос для получения файла

curl --request GET \
  --url 'http://localhost:8080/download?filename_hash=-1150851688997711064' \
  --header 'Postman-Token: 354be5a7-8382-454f-9ad8-4fcb1892ff81' \
  --header 'cache-control: no-cache'
  
DELETE запрос для удаления

curl --request DELETE \
  --url 'http://localhost:8080/delete?filename_hash=-1697883135038405100' \
  --header 'Postman-Token: 3410ac13-b811-47ea-80e6-c0901f293669' \
  --header 'cache-control: no-cache'
