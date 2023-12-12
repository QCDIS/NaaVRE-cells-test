setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--output_dfmerged_4"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
output_dfmerged_4 <- gsub('"', '', opt$output_dfmerged_4)



conf_surfacearea = 1
conf_cellcarboncontent = 1
conf_totalcarboncontent = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_density = 1
conf_totalbiovolume = 1
conf_surfacevolumeratio = 0
conf_output = '/tmp/data/'


conf_surfacearea = 1
conf_cellcarboncontent = 1
conf_totalcarboncontent = 1
conf_biovolume = 1 # if 1 it is calculated, if 0 it is not calculated
conf_density = 1
conf_totalbiovolume = 1
conf_surfacevolumeratio = 0
conf_output = '/tmp/data/'

df.merged=read.csv(output_dfmerged_4,stringsAsFactors=FALSE,sep = ";", dec = ".")

if (conf_density==1) {countingStrategy <- 'density0'}

volumeofsedimentationchamber = '' 
df.temp = ''
df.temp1 = ''
df.temp2 = ''  
df.temp3 = ''  
df.temp4 = ''  
df.temp5 = ''  
df.merged.concat = '' 
pi = 3.14159



if(conf_density==1){
  df.merged[,'density'] = rep(NA,length=nrow(df.merged))
  # default method to calculate the density
  if(countingStrategy=='density0'){  
    df.merged.concat = df.merged[(is.na(df.merged[,'volumeofsedimentationchamber'])) & (is.na(df.merged[,'transectcounting'])),]
    df.temp = df.merged[!is.na(df.merged[,'volumeofsedimentationchamber']) & !is.na(df.merged[,'transectcounting']),]
    df.temp1 = subset(df.temp,volumeofsedimentationchamber <= 5)
    df.temp1[,'density'] = df.temp1[,'organismquantity']/df.temp1[,'transectcounting']*1000/0.001979
    df.merged.concat = rbind(df.merged.concat,df.temp1)
    df.temp2 = subset(df.temp,(volumeofsedimentationchamber > 5) & (volumeofsedimentationchamber <= 10))
    df.temp2[,'density'] = df.temp2[,'organismquantity']/df.temp2[,'transectcounting']*1000/0.00365
    df.merged.concat = rbind(df.merged.concat,df.temp2)
    df.temp3 = subset(df.temp,(volumeofsedimentationchamber > 10) & (volumeofsedimentationchamber <= 25))
    df.temp3[,'density'] = df.temp3[,'organismquantity']/df.temp3[,'transectcounting']*1000/0.010555
    df.merged.concat = rbind(df.merged.concat,df.temp3)
    df.temp4 = subset(df.temp,(volumeofsedimentationchamber > 25) & (volumeofsedimentationchamber <= 50))
    df.temp4[,'density'] = df.temp4[,'organismquantity']/df.temp4[,'transectcounting']*1000/0.021703
    df.merged.concat = rbind(df.merged.concat,df.temp4)
    df.temp5 = subset(df.temp,volumeofsedimentationchamber > 50)
    df.temp5[,'density'] = df.temp5[,'organismquantity']/df.temp5[,'transectcounting']*1000/0.041598
    df.merged.concat = rbind(df.merged.concat,df.temp5)
    df.merged.concat = df.merged.concat[order(df.merged.concat[,'index']),]
    df.merged = df.merged.concat
    df.merged[,'density'] = round(df.merged[,'density'],2)
  }
  # counts per random field
  else if(countingStrategy=='density1'){
    df.merged[,'areaofsedimentationchamber'] = ((df.merged[,'diameterofsedimentationchamber']/2)^2)*pi
    df.merged[,'areaofcountingfield'] = ((df.merged[,'diameteroffieldofview']/2)^2)*pi
    df.merged[,'density'] = round(df.merged[,'organismquantity']*1000*df.merged[,'areaofsedimentationchamber']/df.merged[,'numberofcountedfields']*df.merged[,'areaofcountingfield']*df.merged[,'settlingvolume'],2)
  }
  # counts per diameter transects
  else if(countingStrategy=='density2'){
    df.merged[,'density'] = round(((df.merged[,'organismquantity']/df.merged[,'numberoftransects'])*(pi/4)*(df.merged[,'diameterofsedimentationchamber']/df.merged[,'diameteroffieldofview']))*1000/df.merged[,'settlingvolume'],2)
  }
  # counting method for whole chamber
  else if(countingStrategy=='density3'){
    df.merged[,'density'] = round((df.merged[,'organismquantity']*1000)/df.merged[,'settlingvolume'],2)
  }
  df.merged[,'density'] = df.merged[,'density']/df.merged[,'dilutionfactor']
}   
    


if(conf_totalbiovolume==1){
  if((conf_density==0) & (!'density'%in%names(df.merged))) df.merged[,'density']=NA
  if((conf_biovolume==0) & (!'biovolume'%in%names(df.merged))) df.merged[,'biovolume']=NA
  df.merged[,'totalbiovolume'] = round(df.merged[,'density']*df.merged[,'biovolume'],2)
}
    
    
if(conf_surfacevolumeratio==1){
  if((conf_surfacearea==0) & (!'surfacearea'%in%names(df.merged))) df.merged[,'surfacearea']=NA
  if((conf_biovolume==0) & (!'biovolume'%in%names(df.merged))) df.merged[,'biovolume']=NA
  df.merged[,'surfacevolumeratio']=round(df.merged[,'surfacearea']/df.merged[,'biovolume'],2)
}
    
    

if(conf_totalcarboncontent==1){
  if((conf_density==0) & (!'density'%in%names(df.merged))) df.merged[,'density']=NA
  if((conf_cellcarboncontent==0) & (!'cellcarboncontent'%in%names(df.merged))) df.merged[,'cellcarboncontent']=NA
  df.merged[,'totalcarboncontent']=round(df.merged[,'density']*df.merged[,'cellcarboncontent'],2)
}
   
output_dfmerged_5 = paste(conf_output, "dfmerged_5.csv",sep = "")
write.table(df.merged,output_dfmerged_5,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/output_dfmerged_5_', id, '.json'))
writeLines(toJSON(output_dfmerged_5, auto_unbox=TRUE), file)
close(file)
