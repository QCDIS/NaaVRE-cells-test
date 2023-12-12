setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_7"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_7 <- gsub('"', '', opt$output_dfmerged_7)



conf_surfacearea = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_surfacevolumeratio = 0
conf_output = '/tmp/data/'


conf_surfacearea = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_surfacevolumeratio = 0
conf_output = '/tmp/data/'

biovolume = ''
surfacearea = ''

df.merged=read.csv(output_dfmerged_7,stringsAsFactors=FALSE,sep = ";", dec = ".")

if(conf_surfacevolumeratio==1){
  if((conf_surfacearea==0) & (!'surfacearea'%in%names(df.merged))) df.merged$surfacearea<-NA
  if((conf_biovolume==0) & (!'biovolume'%in%names(df.merged))) df.merged$biovolume<-NA
  SVR_calc<-round(df.merged$surfacearea/df.merged$biovolume,2)
}


output_dfmerged_8 = paste(conf_output, "dfmerged_8.csv",sep = "")
write.table(df.merged,output_dfmerged_8,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/SVR_calc_', id, '.json'))
writeLines(toJSON(SVR_calc, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_8_', id, '.json'))
writeLines(toJSON(output_dfmerged_8, auto_unbox=TRUE), file)
close(file)
