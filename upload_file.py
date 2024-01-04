import os
import time
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

start_time = time.time()

def progress_cb(transferred, total):
  os.system('cls' if os.name == 'nt' else 'clear')
  time_elapsed = time.time() - start_time
  transfer_speed = transferred / time_elapsed if time_elapsed else 0
  time_remaining = (total - transferred) / transfer_speed if transfer_speed else None
  progress = f'{sizeof_fmt(transferred)}/{sizeof_fmt(total)} transferred...'
  elapsed = f'Time elapsed: {time_elapsed:.2f} seconds'
  if time_remaining is not None:
    remaining = f'Estimated time remaining: {time_remaining:.2f} seconds'
  else:
    remaining = 'Estimated time remaining: nil'
  print(f'{progress}\n{elapsed}\n{remaining}', end='', flush=True)

k.set_contents_from_filename(filename, cb=progress_cb, num_cb=10)
k.set_acl('public-read')

url = k.generate_url(0, query_auth=False, force_http=False)
print(f'\n{url.replace(os.environ.get("OBJURL"), domain)}')
