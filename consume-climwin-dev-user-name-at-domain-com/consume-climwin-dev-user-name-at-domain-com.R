setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--rolling_mean_temp"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--temperature_data"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
rolling_mean_temp <- gsub('"', '', opt$rolling_mean_temp)
temperature_data <- gsub('"', '', opt$temperature_data)






cat("Original Temperature Data:\n", head(temperature_data), "\n\n")
cat("Rolling Mean Temperature in Moving Windows:\n", head(coredata(rolling_mean_temp)), "\n")



