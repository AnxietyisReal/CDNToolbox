from globalVars import bucket, domain

filename = ''
k = bucket.delete_key(filename)
print(f'Deleted {filename} from {domain}')
