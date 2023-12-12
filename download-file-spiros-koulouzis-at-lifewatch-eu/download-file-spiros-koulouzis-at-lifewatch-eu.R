setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

option_list = list

option_list = list(
make_option(c("--dest"), action="store", default=NA, type='character', help="my description"),
make_option(c("--file_name"), action="store", default=NA, type='character', help="my description"),
make_option(c("--id"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_hostname"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_login"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_password"), action="store", default=NA, type='character', help="my description")
)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


dest = opt$dest
file_name = opt$file_name
id = opt$id

param_hostname = opt$param_hostname
param_login = opt$param_login
param_password = opt$param_password




 
install.packages("RCurl",repos = "http://cran.us.r-project.org")
RCurl = ''
library(RCurl)
install.packages("httr",repos = "http://cran.us.r-project.org")
httr = ''
library(httr)

auth = basicTextGatherer()
cred = paste(param_login, param_password, sep = ":")
download_file = paste0(param_hostname,file_name)
print(download_file)
file_content <- getURL(download_file, curl = getCurlHandle(userpwd = cred))
write(file_content, file = dest)

output = ""



# capturing outputs
file <- file(paste0('/tmp/output_', id, '.json'))
writeLines(toJSON(output, auto_unbox=TRUE), file)
close(file)
