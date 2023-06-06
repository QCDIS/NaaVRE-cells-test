setwd('/app') 

# retrieve input parameters
library(optparse) 
option_list = list( 
	 make_option(c("--numbers"), action="store", default=NA, type='character', help="my description"),
	 make_option(c("--id"), action="store", default=NA, type='character', help="my description")
)

# set input parameters accordingly 
opt = parse_args(OptionParser(option_list=option_list)) 
library(jsonlite) 
numbers = fromJSON(opt$numbers) 
id = opt$id 

# check if the fields are set 
if(is.na(numbers)){ 
   stop('the `numbers` parameter is not correctly set. See script usage (--help)') 
}
if(is.na(id)){ 
   stop('the `id` parameter is not correctly set. See script usage (--help)') 
}

# source code 
average <- mean(numbers)

# capturing outputs 
file <- file(paste0('/tmp/average_', id, '.json')) 
writeLines(toJSON(average, auto_unbox=TRUE), file) 
close(file) 
