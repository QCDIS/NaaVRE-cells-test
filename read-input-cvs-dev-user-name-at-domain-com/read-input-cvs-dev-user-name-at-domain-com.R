setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

option_list = list

option_list = list(
make_option(c("--id"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_hostname"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_login"), action="store", default=NA, type='character', help="my description"),
make_option(c("--param_password"), action="store", default=NA, type='character', help="my description")
)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id = opt$id

param_hostname = opt$param_hostname
param_login = opt$param_login
param_password = opt$param_password


conf_datain1 = 'traits/input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'
conf_datain2 = 'traits/input/2_FILEinformativo_OPERATORE.csv'
conf_density = 1
conf_local_datain1 = 'input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'
conf_local_datain2 = 'input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'


conf_density = 1
conf_local_datain2 = 'input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'
conf_local_datain1 = 'input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'
conf_datain2 = 'traits/input/2_FILEinformativo_OPERATORE.csv'
conf_datain1 = 'traits/input/Phytoplankton__Progetto_Strategico_2009_2012_Australia.csv'

install.packages("RCurl",repos = "http://cran.us.r-project.org")
RCurl = ''
library(RCurl)


UserPwd = ''
auth <- basicTextGatherer()
auth$UserPwd <- paste(param_login, param_password, sep = ":")


countingStrategy = ''
if (conf_density==1) {countingStrategy <- 'density0'}





# capturing outputs
file <- file(paste0('/tmp/auth_', id, '.json'))
writeLines(toJSON(auth, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/diameteroffieldofview_', id, '.json'))
writeLines(toJSON(diameteroffieldofview, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/transectcounting_', id, '.json'))
writeLines(toJSON(transectcounting, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/UserPwd_', id, '.json'))
writeLines(toJSON(UserPwd, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/numberofcountedfields_', id, '.json'))
writeLines(toJSON(numberofcountedfields, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/settlingvolume_', id, '.json'))
writeLines(toJSON(settlingvolume, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/dilutionfactor_', id, '.json'))
writeLines(toJSON(dilutionfactor, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/index_', id, '.json'))
writeLines(toJSON(index, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/diameterofsedimentationchamber_', id, '.json'))
writeLines(toJSON(diameterofsedimentationchamber, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/countingStrategy_', id, '.json'))
writeLines(toJSON(countingStrategy, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/numberoftransects_', id, '.json'))
writeLines(toJSON(numberoftransects, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/output_dfmerged_', id, '.json'))
writeLines(toJSON(output_dfmerged, auto_unbox=TRUE), file)
close(file)
