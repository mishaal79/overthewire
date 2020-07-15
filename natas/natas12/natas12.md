# Password to level13
jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

# Problem

Natas12


Php Website with fileupload.
Source shows that file is uploaded with random name into a directory and extension is harcoded into jpg.
The issue is the jpg hardcode is done on the client side html form input which can be bypassed.
Size of file restrictied but the extension of file is unrestricted due to poor code

# Solution

Upload malicious file and intercept POST request using burpsuite
Rename file from jpg to php and request path file was uploaded too.
Php code is executed therefore we could try to spawn a shell or run shell commands.

We can also run nc on a port and make the server to listen on it and connect to it from target machine

In this case it is better to use a php webshell which can take input through browser an render shell output after execution

webshell.php has the code to spawning a webshell
# Learnings 

Reverse shell binding using netcat
Using metasploit for reversehell and the capability to produce different payloads.
Spawning a webshell

# Mitigation
Restrict file extensions for file upload from server side and not client side.
