setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_a"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_b"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_c"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_d"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_e"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)

param_a = opt$param_a
param_b = opt$param_b
param_c = opt$param_c
param_d = opt$param_d
param_e = opt$param_e




print(param_a, param_b, param_c, param_d, param_e)



