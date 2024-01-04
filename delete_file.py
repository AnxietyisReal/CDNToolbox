from globalVars import bucket, domain

all_keys = bucket.get_all_keys()
for key in all_keys:
  if key.name.startswith(''):
    bucket.delete_key(key.name)
    print(f'Deleted {key.name} from {domain}')

""" filename = ''
k = bucket.delete_key(filename)
print(f'Deleted {filename} from {domain}') """
