# Password to level
Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

# Problem
It is similiar to NATAS level 12.
File upload vulnerability.
In this challenge the server is validating the type of file by using a whitelist mechanism.
It only allows files which makes the exif_imagetype() function true.
This list of imagetypes are in the php reference https://www.php.net/manual/en/function.exif-imagetype.php.
The exif_imagetype() function only reads the first bytes of an image file and checks its signature.

# Solution
It is pretty evident that the fact the only first bytes of an image is used for signature check should be exploited.
How can this be done ?
Use exiftool to write php code into comment or other attribute section of an image file.

Writing phpcode using exif is rather cumbersome and the filesize of the jpeg should be less than 1000 bytes.

The file header for gif format is rather easy to write into a php exploit file.

`GIF89a;` is the file header for gif files and as the server function accepts gif file.
Insert the file header to top of webshell.php and we have an exploit.

Repeat the same steps for NATAS12 to obtain flag

# Learnings 

Image file header manipulation
- use hex editor to edit file headers
- insert php/shellcode to image metadata attributes using exiftool


# Mitigation
Strictly do a file extension check from server side to save file as jpg and not php.
The reason the code gets exectued is becuase it is stored as php on the server filesystem.
