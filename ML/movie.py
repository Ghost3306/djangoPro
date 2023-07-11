import http.client

conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "54c5622d9bmshf5826e42ab8884dp146e96jsna06521484ec1",
    'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
}

conn.request("GET", "/titles?genre=superhero", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))