
RECIEPIENT = '[Recipient Name]'
WEDDINGDATE = '[Wedding Date]'
WEDDINGTIME='[Wedding Time]'
VENUE='[Wedding Venue Address]'


with open('./Input/Recepients.txt','r') as rec:
    lists = rec.readlines()
    print(lists)

with open ('./Input/Mail_template.txt','r') as file:
        readTemplate = file.read()
        
#        print(lists[i])
for item in lists:
    stripped_name = item.strip()
    outFileName = "./out/"+stripped_name+".txt"    
    with open(f"./out/Invite_{stripped_name}.txt","w") as outFile:
        tempFile = readTemplate.replace(RECIEPIENT,stripped_name)
        tempFile = tempFile.replace(WEDDINGDATE,"11/11/2011")
        tempFile = tempFile.replace(WEDDINGTIME,"08:08")
        tempFile = tempFile.replace(VENUE,"The Taj Banquate")
        outFile.write(tempFile)
    

        