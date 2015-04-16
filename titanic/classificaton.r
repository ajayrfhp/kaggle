data<-read.csv(file='train.csv',header=TRUE)
test<-read.csv(file='test.csv',header=TRUE)
#data<-subset(data,select=-c(Name,PassengerId,SibSp))
#test<-subset(test,select=-c(Name,PassengerId,SibSp))

id <- which(!(test$Name %in% levels(data$Name)))
test$Name[id]<-NA







id <- which(!(test$Ticket %in% levels(data$Ticket)))
test$Ticket[id]<-NA




data<-na.omit(data)
test<-na.omit(test)

model<-glm(Survived~.,data=data)
answer<-predict(model,test)