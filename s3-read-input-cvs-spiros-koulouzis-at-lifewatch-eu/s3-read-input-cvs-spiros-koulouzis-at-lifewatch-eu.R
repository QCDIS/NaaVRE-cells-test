setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_hostname"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_login"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_password"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)

param_hostname = opt$param_hostname
param_login = opt$param_login
param_password = opt$param_password


conf_density = 1
conf_output = '/tmp/data/'


conf_density = 1
conf_output = '/tmp/data/'

install.packages("RCurl",repos = "http://cran.us.r-project.org")
RCurl = ''
library(RCurl)
install.packages("httr",repos = "http://cran.us.r-project.org")
httr = ''
library(httr)

auth = basicTextGatherer()
cred = paste(param_login, param_password, sep = ":")

file_name = "Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv"
dest_1 = paste(conf_output, file_name,sep = "")
download_file = paste0(param_hostname,file_name)
print(download_file)
file_content <- getURL(download_file, curl = getCurlHandle(userpwd = cred))
write(file_content, file = dest_1)


file_name = "2_FILEinformativo_OPERATORE.csv"
dest_2 = paste(conf_output, file_name,sep = "")
download_file = paste0(param_hostname,file_name)
print(download_file)
file_content <- getURL(download_file, curl = getCurlHandle(userpwd = cred))
write(file_content, file = dest_2)


countingStrategy = ''
if (conf_density==1) {countingStrategy <- 'density0'}

index = 0

df.datain = read.csv(dest_1,stringsAsFactors=FALSE,sep = ";", dec = ".")
head(df.datain, n = 3)
df.datain[,'measurementremarks'] = tolower(df.datain[,'measurementremarks']) # eliminate capital letters
df.datain[,'index'] = c(1:nrow(df.datain)) # needed to restore rows order later

df.operator=read.csv(dest_2,stringsAsFactors=FALSE,sep = ",", dec = ".") # load internal database 
head(df.operator, n = 3)
df.operator[df.operator==('no')]<-NA
df.operator[df.operator==('see note')]<-NA

df.merged = merge(x = df.datain, y = df.operator, by = c("scientificname","measurementremarks"), all.x = TRUE)
head(df.merged, n = 3)

if(!'diameterofsedimentationchamber'%in%names(df.merged))df.merged[,'diameterofsedimentationchamber']=NA
if(!'diameteroffieldofview'%in%names(df.merged))df.merged[,'diameteroffieldofview']=NA
if(!'transectcounting'%in%names(df.merged))df.merged[,'transectcounting']=NA
if(!'numberofcountedfields'%in%names(df.merged))df.merged[,'numberofcountedfields']=df.merged[,'transectcounting']
if(!'numberoftransects'%in%names(df.merged))df.merged[,'numberoftransects']=df.merged[,'transectcounting']
if(!'settlingvolume'%in%names(df.merged))df.merged[,'settlingvolume']=NA
if(!'dilutionfactor'%in%names(df.merged))df.merged[,'dilutionfactor']=1

output_dfmerged_1 = paste(conf_output, "dfmerged_1.csv",sep = "")
write.table(df.merged,output_dfmerged_1,row.names=FALSE,sep = ";",dec = ".",quote=FALSE)



# capturing outputs
file <- file(paste0('/tmp/file_name_', id, '.json'))
writeLines(toJSON(file_name, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_1_', id, '.json'))
writeLines(toJSON(output_dfmerged_1, auto_unbox=TRUE), file)
close(file)
