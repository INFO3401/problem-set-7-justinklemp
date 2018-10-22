#Justin Klemperer
#Work from Friday - problem set 7

#PROBLEM 6

titanic = read.csv(file="titanic.csv",head=TRUE,sep=",")
print(titanic)
summary(titanic)

#PROBLEM 7
names(titanic)
titanic$"PassengerId"
titanic$"Survived"
table(titanic$PassengerId,Survived)

#PROBLEM 8

prop.table(table(titanic_data$Sex, titanic_data$Survived))

prop.table(table(titanic_data$Sex, titanic_data$Survived), 1)

prop.table(table(titanic_data$Sex, titanic_data$Survived), 2)
