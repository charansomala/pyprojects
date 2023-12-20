#IF condition..

totalmarks = 85
if totalmarks >= 90:
    print("congrats you have secured 'A'grade")
elif totalmarks >=40:
    print("congrats you have cleared exam")
else:
    print("you have cleared the exam")

#Nested if condition..

tmarks=100
if tmarks>=90:
    print("congrats you have cleared exam")
    if tmarks==100:
        print("you got full marks")

##And condition
tmarks=95
attendance=92
if tmarks>=90 and attendance>=90:
    print("you are worst")

fruit ="apple"
if fruit is "mango" or "apple":
    print("i like that fruit")
#For loop
fruits=["orange","kiwi","apple"]
for f in fruits:
    print(f)
#Range
for number in range(1,10):
    print(number)
#break
for number in range(1,20):
    if number==15:
        break









