# Sites Monitoring Utility

Thank you for using my script for checking sites health. 

## Quick start

Donwload script and go to terminal:
<pre>
$ pip install -r requirements.txt
$ python3 check_sites_health.py [__path_to_file_with_urls__]
</pre>

## Script info

Script checks if site responds with 200 HTTP-code, then gets domain expiry date and checks
if it is a month or more since today.  
On launch you can pass file directly in terminal, if not scrpit asks you for it.

## Typical output

<pre>
http://www.google.ru
Server responds with 200 code: True
Server expires over month: True
--------
http://www.vk.com
Server responds with 200 code: False
Server expires over month: True
--------
</pre>
