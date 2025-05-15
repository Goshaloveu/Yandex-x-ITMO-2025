import re

res = []
method = set()
with open("server.log", "r") as inp:
    p = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] WARNING\tRequest from (?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) \("(?P<method>[A-Z]+) (?P<path>.*)"\) is malicious\b')
    for line in inp.readlines():
        if (p.match(line)):
            x = p.search(line)
            res.append(x)
            method.add(x.group("method"))
            # print(line, x.group("ip"), x.group("method"), x.group("path"), sep="\n", end="\n\n")
        # print(line)


ans = []
s_method = set()
with open("server.log", "r") as inp:
    new_p = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] WARNING\tRequest from (?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) \("(?P<method>[A-Z]+) (?P<path>.*) HTTP/\d\.\d"\) is malicious\b')
    for line in inp.readlines():
        x = new_p.match(line)
        if (x):
            ans.append(x)
            s_method.add(x.group("method"))
            print(line, end="")
            ip = x.group('ip')
            method = x.group('method')
            path = x.group('path')
            print(f"IP:     {ip}")
            print(f"Method: {method}")
            se = "=" * 100
            print(f"Path:   {path}", end=f"\n\n{se}\n\n")

print(len(res), len(ans))
# print(method, s_method)

# s = '[2024-04-13 15:31:17] WARNING\tRequest from 56.185.32.17 ("GET /api/geojson?url=file:///etc/hosts HTTP/1.1") is malicious\n'
# p = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] WARNING\tRequest from (?P<ip>\d{0,3}.\d{0,3}.\d{0,3}.\d{0,3}) \("(?P<method>[A-Z]+) (?P<path>.*) HTTP/1.1"\) is malicious\b')

# if (p.match(s)):
#     x = p.search(s)
#     print(s, x.group("ip"), x.group("method"), x.group("path"), sep="\n", end="\n\n")
# print(s)
