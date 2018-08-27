import re

sourceFilename = "test_run.txt"
destFilename = "desTestRun.txt"
fhandle = open(sourceFilename, "r")
destFhandle = open(destFilename, "w")

pattern = r'\"text\":(([\"\'])[\w+\W+\s+\S+])'

for objLine in fhandle:
    text=None
    text = re.match(pattern, objLine, re.IGNORECASE)    
    if(text != None):
        destFhandle.write(text.group(0))

fhandle.close()
destFhandle.close()
print("done")
