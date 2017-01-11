import wolframalpha

app_id = 'HQWY5J-34GREV68GE'

client = wolframalpha.Client(app_id)

res = client.query('tides seattle, Washington')

print res
for pod in res.pods:
    do_something_with(pod)

for pod in res.pods:
    for sub in pod.subpods:
    	print(sub)
    	print('\n')
    print('####\n\n')

print(next(res.results).text)

