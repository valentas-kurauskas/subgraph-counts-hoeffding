library(data.table)
a<-as.data.table(readRDS("./bics-paper-release/bics-paper-code/data/df_all_waves.rds"))
#https://github.com/dfeehan/bics-paper-release/blob/main/bics-paper-code/code/00-run-all.R
#sums weights, not inverse weights
#this matches the picture in their paper
b=a[, .(n=.N, weight=sum(weight_pooled)), by=.(wave, num_cc)]
dummy<-lapply(0:3, function(x) fwrite(b[wave==x, .(degree=num_cc, freq=n)][order(degree),], paste0("COVID19-Wave",x,".csv"), row.names=FALSE))
dummy<-lapply(0:3, function(x) fwrite(b[wave==x, .(degree=num_cc, freq=weight/sum(weight))][order(degree),], paste0("COVID19-Wave",x,"_adjusted.csv"), row.names=FALSE))

