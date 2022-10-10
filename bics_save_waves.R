library(data.table)
a<-as.data.table(readRDS("./bics-paper-release/bics-paper-code/data/df_all_waves.rds"))
#https://github.com/dfeehan/bics-paper-release/blob/main/bics-paper-code/code/00-run-all.R
#sums weights, not inverse weights
#this matches the picture in their paper
b=a[, .(n=.N, weight=sum(weight_pooled)), by=.(wave, num_cc)]
dummy<-lapply(0:3, function(x) fwrite(b[wave==x, .(degree=num_cc, freq=n)][order(degree),], paste0("COVID19-Wave",x,".csv"), row.names=FALSE))
dummy<-lapply(0:3, function(x) fwrite(b[wave==x, .(degree=num_cc, freq=weight/sum(weight))][order(degree),], paste0("COVID19-Wave",x,"_adjusted.csv"), row.names=FALSE))

fwrite(b[wave %in% 1:3, .(freq=sum(n)), by=.(degree=num_cc)], "COVID19-Waves1,2,3combined.csv",row.names=FALSE)
b[, `:=`(nweight=weight/sum(weight), num_cc_wave=sum(num_cc)), by=.(wave)]
fwrite(b[wave %in% 1:3, .(freq=sum(nweight*num_cc_wave)/sum(num_cc_wave)), by=.(degree=num_cc)][order(degree)], "COVID19-Waves1,2,3combined_adjusted.csv",row.names=FALSE)

