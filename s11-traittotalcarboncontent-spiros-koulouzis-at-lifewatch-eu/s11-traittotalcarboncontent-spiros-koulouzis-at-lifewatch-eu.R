setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_8"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_8 <- gsub('"', '', opt$output_dfmerged_8)



conf_cellcarboncontent = 1
conf_totalcarboncontent = 1
conf_density = 1
conf_output = '/tmp/data/'


conf_cellcarboncontent = 1
conf_totalcarboncontent = 1
conf_density = 1
conf_output = '/tmp/data/'
df.merged=read.csv(output_dfmerged_8,stringsAsFactors=FALSE,sep = ";", dec = ".")

cellcarboncontent = ''
density = ''
TCC_calc = 0.0

if(conf_totalcarboncontent==1){
  if((conf_density==0) & (!'density'%in%names(df.merged))) df.merged$density<-NA
  if((conf_cellcarboncontent==0) & (!'cellcarboncontent'%in%names(df.merged))) df.merged$cellcarboncontent<-NA
  TCC_calc<-round(df.merged$density*df.merged$cellcarboncontent,2)
}

output_dfmerged_9 = paste(conf_output, "dfmerged_8.csv",sep = "")
write.table(df.merged,output_dfmerged_9,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/TCC_calc_', id, '.json'))
writeLines(toJSON(TCC_calc, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_9_', id, '.json'))
writeLines(toJSON(output_dfmerged_9, auto_unbox=TRUE), file)
close(file)
