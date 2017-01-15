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
http://afisha.ru: Responds with code 200: Yes | Domain is paid for over a month: Yes
http://devman.org: Responds with code 200: Yes | Domain is paid for over a month: Yes
http://github.com: Responds with code 200: Yes | Domain is paid for over a month: Yes
</pre>
