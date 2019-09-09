data = []
with open('reading.txt','r') as f:
	for li in f:
		data.append(li.strip())
print(len(data))
print(data)

sum_len = 0
for zifu in data:
	sum_len += len(zifu)
print('the average is ',sum_len/len(data))