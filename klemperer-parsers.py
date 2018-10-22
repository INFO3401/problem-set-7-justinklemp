################################################################################
# PART #1
################################################################################

# Steven, Lucas, Marissa, Zach, and Harold helped me
    
def countWordsUnstructured(filename):
    wordcount = {}
    file = open(filename)
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print (wordcount) 
    
################################################################################
# PART 2
################################################################################
    
def generateSimpleCSV(targetfile, wordCounts): 
    with open(targetfile, 'w', newline = '') as csvfile:
		w = csv.writer(csvfile, delimiter = ',')
		w.writerow(['Word', 'Count'])
		for key, value in dict_data.items():
			w.writerow([key, value])
	csvfile.close()
	return csvfile

################################################################################
# PART 3
################################################################################
    
import os
from os import listdir 

def countWordsMany(directory): 
    dirlist = os.listdir(directory)
    wordDict = {}
    for file in dirlist:
        eachWordCount = countWordsUnstructured(files)
        wordDict[files] += eachWordCount
    return wordDict

################################################################################
# PART 4
################################################################################

def generateDirectoryCSV(wordCounts, targetfile):  
    with open (targetfile, 'w') as csv_file:        
        writer = csv.writer(csv_file)        
        writer.writerow(['Filename', 'Word', 'Count'])        
        for key,value in wordCounts.items():
            writer.writerow([key,value])    
    csv_file.close()    
    return csv_file

################################################################################
# PART 5
################################################################################

def generateJSONFile(wordCounts, targetfile):
    JSON_file=open(targetfile, "w")
    JSON_file.write(str(wordCounts).replace("\'", "\""))
    JSON_file.close()
    return JSON_file
generateJSONFile(master_dict, "targetfile3.json")

################################################################################
# PART 6
################################################################################

def searchCSV(csvfile, word): 
    largest_file= ""
    largest_count=0
    with open(csvfile, 'r') as csv_file:
        file_read = csv.reader(csv_file)
        for line in file_read:
            if line[1] == word and int(line[2])>largest_count:
                largest_count= int(line[2])
                largest_file=line[0]
        return largest_file
        csv_file.close()

def searchJSON(JSONfile, word): 
    largest_file= ""
    largest_count=0
    with open(JSONfile, "r") as json_file:
        read_data= json.load(json_file)
        for file in read_data:                
            if word in read_data[file] and read_data[file][word] > largest_count:
                largest_count= read_data[file][word]
                largest_file= file
        return largest_file
        json_file.close()

print(searchCSV("targetfile2.csv", "America"))
print(searchJSON("targetfile3.json", "America"))