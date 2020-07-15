Password for level 12

EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

# Problem 
Challenge uses a weak encryption called XOR on the server side to encrypt the cookie.
The code also shows the default plaintext used in the encyrption process.
Set the cookie to a specific which executes code block  value to obtain flag.

**XOR Encryption explained**
In XOR encryption a plaintext and key is XORed to evaluate cipher text.
`A XOR B = C`
Although this is weakned by a known-plaintext style attack.
When the plaintext is XORed with ciphertext the key can be determined

# Solution
Use the default plaintext and cookie set as cipher text to obtain the key.
Run the php code locally with plaintext and cipher text as key to determine key.
Once key is determined replace plaintext with payload text and evaluate the ciphertext

In the browser set the cookie to the ciphertext evaluated to reveal flag

# Learnings
- Running PHP code using local terminal
- XOR encryption weakness

# Mitigations
- Use a different encyrption algorithm for cookie
