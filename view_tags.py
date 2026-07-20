import json
with open('img_tags.json', 'r') as f:
    data = json.load(f)
for d in data:
    if 'index Adu_files' in d['src']:
        hash_id = d['src'].split('/')[-1][:8]
        print(f"{d['file']} : {hash_id} : Context: {d['context'][:100]}")
