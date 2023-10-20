import os
from globalVars import bucket, domain, filename, obj_filename

if (os.environ.get('OBJURL') == None):
  print('Please set OBJURL in your environment variables.')
  exit()

k = bucket.new_key(obj_filename)

def sizeof_fmt(num, suff='B'):
  for unit in ['','Ki','Mi','Gi']:
    if abs(num) < 1024.0:
      return f'{num:3.1f}{unit}{suff}'
    num /= 1024.0
  return f'{num:.1f} Yi{suff}'

def progress_cb(transferred, total):
  print(f'{sizeof_fmt(transferred)} of {sizeof_fmt(total)} transferred...')

k.set_contents_from_filename(filename, cb=progress_cb, num_cb=10)
k.set_acl('public-read')

url = k.generate_url(0, query_auth=False, force_http=False)
print(url.replace(os.environ.get('OBJURL'), domain))
