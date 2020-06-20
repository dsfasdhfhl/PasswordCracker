import hashlib

p_hash = input("Enter MD5 Hash here --> ")

w_list = input("Enter Password file name here --> ")

password_file = open(w_list, 'r')
fg = 1

for _word in password_file:
	enc_word = _word.encode("utf-8")
	digs = hashlib.md5(enc_word.strip()).hexdigest()

	print(_word)
	print(digs)

	if digs == p_hash:
		print("Password found! :)")
		print("The password is {}".format(_word))
		password_file.close()
		fg=2
		break

if fg == 1:
	print('Password not Found :(')
	quit()