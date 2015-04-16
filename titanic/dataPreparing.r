data<-read.csv(file='train.csv',header=TRUE)
test<-read.csv(file='test.csv',header=TRUE)
#plot(density(data$Age,na.rm=TRUE))
#counts<-table(data$Survived,data$Sex)
#barplot(counts,xlab='gender',ylab='no of people')

data$Sex<-gsub("female",0,data$Sex)
data$Sex<-gsub('male',1,data$Sex)