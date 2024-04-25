path = r"C:\Users\mindf\Desktop\Wipro-IIHT\python-work\scripts\project-student\students.csv"

f = open(path)
data = f.readlines()
f.close()

colData = data[0].strip()
cols = colData.split(',')
print(cols)

classDict = {}
for row in data[1:]:
    rowData = row.strip()
    temp = rowData.split(',')
    studDict = dict(zip(cols, temp))
    classDict[studDict['regid']] = studDict

print('-'*100)
print(classDict)

for stud in classDict.keys():
    s = []
    for sub in ['phy', 'chem', 'math', 'bio']:
        temp = classDict[stud][sub]
        s.append(float(temp))
    print(s)
    classDict[stud]['avg'] = sum(s)/ 4


print(classDict)

f = open("results.txt", 'w')

f.write(colData+"\n")

writeData = []
for stud in classDict:
    writeData.append(','.join([str(i) for i in classDict[stud].values()])+"\n")

f.writelines(writeData)

f.close()