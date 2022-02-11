# f1 = open("./output/test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
#
# f2 = open("./output/test.txt", 'r')
# print(f2.read())
# f2.close()


# # Q6
# user_input = input("??? ??? ????? : ")
# f = open('./output/test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

with open('./output/test4.txt', 'w') as f1:
    f1.write("Life is too short \n  You need java")
with open('./output/test4.txt', 'r') as f1:
    body = f1.read()

body = "".replace('java', 'python')

with open('./output/text4.txt', 'w') as f2:
    f2.write(body)