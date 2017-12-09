import os
import time

t0= time.clock()
scoreList = []
scoreString = ''
rootDir = '.'
missing = 0
count = 1
for dirName, subdirList, fileList in os.walk(rootDir):
    subDir = os.path.join(rootDir, dirName)
    for fname in fileList:
        if fname=='grade.txt':
            print('grade file #' + str(count) + ' found')
            count+=1
            log = open(os.path.join(subDir, fname), 'r')
            words = log.read()
            log.close()
            words = words.split()
            #find score:
            scoreList.append([float(words[-1][:-4]), dirName[3:]])

scoreList = sorted(scoreList)
print('grades sorted')

#find mean
total = 0
for value in scoreList:
    total+=value[0]
mean = total/len(scoreList)
        
for value in scoreList:
    scoreString += str(value)+'\n'
analysis = 'Submissions: '+str(len(scoreList))+'\n'
analysis += 'Lowest:'+ str(scoreList[0])+'.......'+ 'Highest:'+ str(scoreList[-1])+'\n'
analysis += 'Median:'+str(scoreList[len(scoreList)//2])+'.......'+'Average:'+str(mean)

f = open('data.txt','w')
print('text file created')
f.write('Data Analysis'+'\n\n\n')
f.write('Sorted: \n\n' + scoreString + '\n')
f.write(' CS111 PS9 Stats: \n' + analysis)

t= time.clock() - t0

f.write('\nTask completed in '+str(t)+' seconds')
f.close()
print('text file completed and closed')
