import requests

print("Start")

ids = range(1, 1000000)
chunks = [ids[x:x + 100] for x in range(0, len(ids), 100)]

counter = 0

for chunkIds in chunks:
    ids = ",".join([str(id) for id in chunkIds])
    response = requests.get('https://api.vk.com/method/users.get', params={"user_ids": ids, "lang": "en"})
    listSerg = [user for user in response.json()["response"] if user['first_name'] == "Sergey"]
    counter += len(listSerg)
    print('From:{} to {} -  {}'.format(chunkIds[0], chunkIds[len(chunkIds) - 1], len(listSerg)))

print("End ---------")

print(counter)  # 22397
