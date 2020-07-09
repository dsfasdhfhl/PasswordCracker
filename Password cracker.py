import hashlib

print("\033[1;36;40m\033\n")
print("""{}
    
    ██╗  ██╗ ██████╗ ██╗██████╗                                                    
    ██║  ██║██╔════╝███║██╔══██╗                                                   
    ███████║██║     ╚██║██║  ██║                                                
    ╚════██║██║      ██║██║  ██║                                                   
         ██║╚██████╗ ██║██████╔╝                                                   
         ╚═╝ ╚═════╝ ╚═╝╚═════╝                                                    
                                                                                   
            ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     
            ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    
            ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    
            ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    
            ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     
                                                                                   
                         ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗    
                        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗   
                        ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝   
                        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   
                        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║   
                         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
{}\n\tWelcome To 4C1D's Password Cracker (The Hashes WON'T Show)\n\tSubscribe To Linux Hacker On YT, And Follow linux_hacker_4c1d On IG\n{}""".format("="*100,"="*100,"="*100))

print("\033[1;37;40m\n")

p_hash = input("Enter MD5 Hash Here --> ")

w_list = input("Enter Wordlist Here --> ")

print("\033[1;34;40m\n")
print("Please Wait The Password Is Being Cracked This Might Take A Bit...")                
print("So While You Wait Dance With The Robots └[∵┌]└[ ∵ ]┘[┐∵]┘")




password_file = open(w_list, 'r')
fg = 1
for _word in password_file:
	enc_word = _word.encode("utf-8")
	digs = hashlib.md5(enc_word.strip()).hexdigest()




	if digs == p_hash:
		print("\033[1;32;40m\n")
		print("==================================")
		print("Password Found! ٩(^ᴗ^)۶")
		print("The Password Is {}".format(_word))
		print("Closing Program... Bye (•◡•) /")
		print("==================================")		
		print("Come Back Soon (•◡•) /")
		print("==================================")
		password_file.close()
		fg=2
		break
if fg == 1:
	print("\033[1;31;40m\n")
	print("==================================")	
	print("Password Not Found (︶︹︺)")
	print("Closing Program... Bye (•◡•) /")
	print("==================================")	
	print("Come Back Soon (•◡•) /")
	print("==================================")	

	quit()

