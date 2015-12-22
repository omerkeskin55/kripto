
# -*- coding: utf-8 -*-
import sys

def encrypt(k,plaintext):
	
	cipher = ''
	
	for each in plaintext:
		c = (ord(each)+k) % 126
		
		if c < 32: 
			c+=31
			
		cipher += chr(c)
		
	print ('Your encrypted message is: ' + cipher)

	
def decrypt(k,cipher):
	
	plaintext = ''
	
	for each in cipher:
		p = (ord(each)-k) % 126
	
		if p < 32:
			p+=95
						
		plaintext += chr(p)
		
	print ('Your plain text message is: ' + plaintext)
	
















