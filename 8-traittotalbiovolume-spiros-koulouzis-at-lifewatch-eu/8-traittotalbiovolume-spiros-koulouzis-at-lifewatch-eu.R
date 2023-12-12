setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_5"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_5 <- gsub('"', '', opt$output_dfmerged_5)



conf_density = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_output = '/tmp/data/'
conf_totalbiovolume = 1


conf_density = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_output = '/tmp/data/'
conf_totalbiovolume = 1

biovolume = '' 
density = ''
df.merged=read.csv(output_dfmerged_5,stringsAsFactors=FALSE,sep = ";", dec = ".")

if(conf_totalbiovolume==1){
  if((conf_density==0) & (!'density'%in%names(df.merged))) df.merged$density<-NA
  if((conf_biovolume==0) & (!'biovolume'%in%names(df.merged))) df.merged$biovolume<-NA
  TBV_calc = round(df.merged$density*df.merged$biovolume,2)
}

output_dfmerged_6 = paste(conf_output, "dfmerged_6.csv",sep = "")
write.table(df.merged,output_dfmerged_6,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/TBV_calc_', id, '.json'))
writeLines(toJSON(TBV_calc, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_6_', id, '.json'))
writeLines(toJSON(output_dfmerged_6, auto_unbox=TRUE), file)
close(file)
