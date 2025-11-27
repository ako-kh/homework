from concurrent.futures import ThreadPoolExecutor
from socket import gethostbyname
import csv, requests, time

domains = []

with open("domains.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        domains.append(row[1])

results_list = []
main_time = time.perf_counter()

def request_f(domain, timeout):
    try:
        request_start = time.perf_counter()
        requests.get("https://" + domain, timeout=timeout)
        response_t = (time.perf_counter() - request_start)
        ip = gethostbyname(domain)
    except:
        response_t = "N/A"
        ip = "N/A"

    return {
            "domain": domain,
            "response_time": response_t,
            "ip_address": ip
        }

with ThreadPoolExecutor(max_workers=100) as executor:
    for dom in domains:
        results_list.append(executor.submit(request_f, dom, 5))

with open("results.csv", "w") as f:
    headers = ["domain", "response_time", "ip_address"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for result in results_list:
        writer.writerow(result.result())

print(time.perf_counter() - main_time)




