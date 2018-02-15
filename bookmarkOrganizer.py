def main():
	filename = raw_input("Please enter the bookmark HTML filename: ")
	keyword = raw_input("Enter the website: ")
	list_keyword = []
	#Reads the HTML file and puts all of the data into linesHTML
	with open(filename,"r") as file_read:
		linesHTML = file_read.readlines()

	#Searches through linesHTML to find the website the user entered. If it has found it, then it gets put into 
	#the list_keyword list.
	for i in range(len(linesHTML)):
		if keyword in linesHTML[i].lower():
			list_keyword.append(linesHTML[i])

	#Removes the occurances of the website with linesHTML
	for p in range(len(list_keyword)):
		for z in range(len(linesHTML)):
			if list_keyword[p] in linesHTML[z]:
				linesHTML.remove(linesHTML[z])
				break

	startFolder = "<DL><p> \n <DT><H3> " + keyword + "</H3> \n"
	endFolder = "</DL><p> \n"
	#Inserts the contents of list_keyword back into linesHTML so the folder for the bookmarks can be created.
	list_keyword.insert(0,startFolder)
	list_keyword.insert(len(list_keyword),endFolder)
	linesHTML[9:9] = list_keyword
		
	#Creates a new HTML file that will include the folder of the bookmarks
	newFilename = "new_" +filename
	with open(newFilename,"w") as file_write:
		file_write.writelines(linesHTML)

main()
