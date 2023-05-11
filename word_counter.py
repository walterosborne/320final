import json

with open('Final.ipynb', encoding='utf-8') as json_file:
    data = json.load(json_file)

wordCount = 0
lineCount = 0
for each in data['cells']:
    cellType = each['cell_type']
    if cellType == "code":
        content = each['source']
        for line in content:
            if not line.lstrip().startswith('#'):
                lineCount += 1
    if cellType == "markdown":
        content = each['source']
        for line in content:
            temp = [word for word in line.split() if "#" not in word] # we might need to filter for more markdown keywords here
            wordCount = wordCount + len(temp)
            
print("Word count " + str(wordCount))
print("Line count " + str(lineCount))
