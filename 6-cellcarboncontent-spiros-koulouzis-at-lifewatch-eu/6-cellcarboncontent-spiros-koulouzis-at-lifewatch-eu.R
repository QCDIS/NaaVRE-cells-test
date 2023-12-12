setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_3"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_3 <- gsub('"', '', opt$output_dfmerged_3)



conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_cellcarboncontent = 1
conf_output = '/tmp/data/'


conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_cellcarboncontent = 1
conf_output = '/tmp/data/'

df.merged=read.csv(output_dfmerged_3,stringsAsFactors=FALSE,sep = ";", dec = ".")

formulaforweight1 = '' 
formulaforweight2 = '' 
biovolume = ''
cellcarboncontent = ''
df.temp = ''  
cc.form = ''
df.merged.concat = '' 
cc.formulas1 = ''
cc.formulas2 = ''
df.cc = ''
df.cc1 = ''
df.cc2 = ''


if(conf_cellcarboncontent==1){
  df.merged[,'cellcarboncontent'] = rep(NA,length=nrow(df.merged))
  if(conf_biovolume==1){
    df.merged.concat = df.merged[is.na(df.merged[,'biovolume']),]
    df.cc = df.merged[!is.na(df.merged[,'biovolume']),]
    df.cc1 = subset(df.cc,biovolume <= 3000)
    df.cc2 = subset(df.cc,biovolume > 3000)
    cc.formulas1 = unique(df.merged[!is.na(df.merged[,'formulaforweight1']),'formulaforweight1'])
    for(cc.form in cc.formulas1){
      df.temp = subset(df.cc1,formulaforweight1==cc.form)
      df.temp[,'cellcarboncontent'] = round(with(df.temp,eval(parse(text=tolower(cc.form)))),2)
      df.merged.concat = rbind(df.merged.concat,df.temp)
    }
    cc.formulas2 = unique(df.merged[!is.na(df.merged[,'formulaforweight2']),'formulaforweight2'])
    for(cc.form in cc.formulas2){
      df.temp = subset(df.cc2,formulaforweight2==cc.form)
      df.temp$cellcarboncontent = round(with(df.temp,eval(parse(text=tolower(cc.form)))),2)
      df.merged.concat = rbind(df.merged.concat,df.temp)
    }
    df.merged.concat = df.merged.concat[order(df.merged.concat[,'index']),]
    df.merged = df.merged.concat
  }
}

output_dfmerged_4 = paste(conf_output, "dfmerged_4.csv",sep = "")
write.table(df.merged,output_dfmerged_4,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)




# capturing outputs
file <- file(paste0('/tmp/output_dfmerged_4_', id, '.json'))
writeLines(toJSON(output_dfmerged_4, auto_unbox=TRUE), file)
close(file)
