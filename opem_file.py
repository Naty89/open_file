open_file("file_to_save.txt", "r+")
open_file.write("hello world")
if "e" in open_file.read():
	open_file.write(' I was right!")
else:
	open_file.write(" I was wrong")

