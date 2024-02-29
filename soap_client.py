from zeep import Client

client = Client("http://localhost:8000/")

result = client.service.SumaDosNumeros(8,5)
print(result)