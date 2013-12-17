import re

def readFile(fileName):
	f = open(fileName, 'r')
	return f

def parseFile(parseMe):
	fileStr = parseMe.read()
	urls = re.findall('<a href="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', fileStr)
	return urls

def main():
	webPage = readFile("sample_page.html")
	result = parseFile(webPage)
	print result

if __name__ == '__main__':
	main()