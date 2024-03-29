setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_1"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_CalcType"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_1 <- gsub('"', '', opt$output_dfmerged_1)

param_CalcType = opt$param_CalcType


conf_output = '/tmp/data/'


conf_output = '/tmp/data/'

df.merged = read.csv(output_dfmerged_1,stringsAsFactors=FALSE,sep = ";", dec = ".")

formulaformissingdimension = '' 
formulaformissingdimensionsimplified = ''
df.temp = ''  
md.form = ''
df.temp2 = ''
index = ''
md = ''
df.merged.concat = '' 
md.formulas = ''

if(param_CalcType=='advanced'){
  df.merged.concat = df.merged[is.na(df.merged[,'formulaformissingdimension']),]
  md.formulas = unique(df.merged[!is.na(df.merged[,'formulaformissingdimension']),'formulaformissingdimension'])
  for(md.form in md.formulas){
    df.temp = subset(df.merged,formulaformissingdimension==md.form)
    for(md in unique(df.temp[,'missingdimension'])){
      df.temp2 = df.temp[df.temp[,'missingdimension']==md,]
      df.temp2[[md]] = round(with(df.temp2,eval(parse(text=md.form))),2)
      df.merged.concat = rbind(df.merged.concat,df.temp2)
    }
  }
  df.merged.concat = df.merged.concat[order(df.merged.concat[,'index']),]
  df.merged = df.merged.concat
} else if(param_CalcType=='simplified'){
  df.merged.concat = df.merged[is.na(df.merged[,'formulaformissingdimensionsimplified']),]
  md.formulas = unique(df.merged[!is.na(df.merged[,'formulaformissingdimensionsimplified']),'formulaformissingdimensionsimplified'])
  for(md.form in md.formulas){
    df.temp = subset(df.merged,formulaformissingdimensionsimplified==md.form)
    for(md in unique(df.temp[,'missingdimensionsimplified'])){
      df.temp2 = df.temp[df.temp[,'missingdimensionsimplified']==md,]
      df.temp2[[md]] = round(with(df.temp2,eval(parse(text=md.form))),2)
      df.merged.concat = rbind(df.merged.concat,df.temp2)
    }
  }
  df.merged.concat = df.merged.concat[order(df.merged.concat[,'index']),]
  df.merged = df.merged.concat
}

output_dfmerged_2 = paste(conf_output, "dfmerged_2.csv",sep = "")
write.table(df.merged,output_dfmerged_2,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/output_dfmerged_2_', id, '.json'))
writeLines(toJSON(output_dfmerged_2, auto_unbox=TRUE), file)
close(file)
