setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_6"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_CalcType"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_6 <- gsub('"', '', opt$output_dfmerged_6)

param_CalcType = opt$param_CalcType


conf_output = '/tmp/data/'
conf_surfacearea = 1


conf_output = '/tmp/data/'
conf_surfacearea = 1

index = 0

df.merged=read.csv(output_dfmerged_6,stringsAsFactors=FALSE,sep = ";", dec = ".")
surfacearea = ''
formulaforsurfacesimplified = '' 
formulaforsurface = ''

CalcType=param_CalcType

if(conf_surfacearea==1){
  if(CalcType=='advanced'){
    df.merged$surfacearea <- rep(NA,length=nrow(df.merged))
    df.merged.concat <- df.merged[is.na(df.merged$formulaforsurface),]
    sa.formulas <- unique(df.merged[!is.na(df.merged$formulaforsurface),]$formulaforsurface)
    for(sa.form in sa.formulas){
      df.temp <- subset(df.merged,formulaforsurface==sa.form)
      df.temp$surfacearea <- round(with(df.temp,eval(parse(text=sa.form))),2)
      df.merged.concat <- rbind(df.merged.concat,df.temp)
    }
    df.merged.concat <- df.merged.concat[order(df.merged.concat$index),]
    df.merged <- df.merged.concat
    SA_calc <- df.merged$surfacearea
  }
  else if(CalcType=='simplified'){
    df.merged$surfacearea <- rep(NA,length=nrow(df.merged))
    df.merged.concat <- df.merged[is.na(df.merged$formulaforsurfacesimplified),]
    sa.formulas <- unique(df.merged[!is.na(df.merged$formulaforsurfacesimplified),]$formulaforsurfacesimplified)
    for(sa.form in sa.formulas){
      df.temp <- subset(df.merged,formulaforsurfacesimplified==sa.form)
      df.temp$surfacearea <- round(with(df.temp,eval(parse(text=sa.form))),2)
      df.merged.concat <- rbind(df.merged.concat,df.temp)
    }
    df.merged.concat <- df.merged.concat[order(df.merged.concat$index),]
    df.merged <- df.merged.concat
    SA_calc <- df.merged$surfacearea
  }
}

output_dfmerged_7 = paste(conf_output, "dfmerged_7.csv",sep = "")
write.table(df.merged,output_dfmerged_7,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/SA_calc_', id, '.json'))
writeLines(toJSON(SA_calc, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_7_', id, '.json'))
writeLines(toJSON(output_dfmerged_7, auto_unbox=TRUE), file)
close(file)
