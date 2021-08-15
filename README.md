# python_requests_firebase
Biblioteca requests para realizar solicitudes HTTP y consumir API Firebase

## Docker image
docker build -t python_firebase:v1 .

## Container
docker run -it -v /workspace/python_requests_firebase/webapp:/webapp -p 8080 --name webpy -h webpy python_firebase:v1