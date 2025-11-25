import requests, json, time
from concurrent.futures import ThreadPoolExecutor



def img_info(img_id):
    url = f"https://jsonplaceholder.typicode.com/photos/{img_id}"
    return requests.get(url).json()

stat_time = time.perf_counter()

with ThreadPoolExecutor(max_workers=50) as executor:
    imgs = [executor.submit(img_info, i) for i in range(1, 5001)]
    img_list = []

    for img in imgs:
        img_list.append(img.result())

    with open("images.json", "w") as f:
        json.dump(img_list, f, indent=4)

end_time = time.perf_counter()

print(end_time - stat_time)