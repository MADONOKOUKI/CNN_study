from decode_img_url import save_picture

orion = open('onion.txt','r')
string = orion.readline()
cnt = 0
# print(string[1])
while string:
    save_picture(string.split(',')[1],cnt,"onion")
    string = orion.readline()
    cnt+=1

orion = open('carot.txt','r')
string = orion.readline()
cnt = 0
# print(string[1])
while string:
    save_picture(string.split(',')[1],cnt,"carot")
    string = orion.readline()
    cnt+=1

