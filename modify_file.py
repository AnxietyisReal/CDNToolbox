from globalVars import bucket, domain

filename = ''
k = bucket.get_key(filename)
if k is not None:
  k.set_canned_acl('public-read')
  print(f'Set {filename} to public-read on {domain}')
