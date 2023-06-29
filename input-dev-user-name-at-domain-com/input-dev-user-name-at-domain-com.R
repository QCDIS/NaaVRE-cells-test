setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

option_list = list

option_list = list(
make_option(c("--id"), action="store", default=NA, type='character', help="my description")
)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id = opt$id





a = 2 
numbers <- c(a, 4, 6, 8, 10)



# capturing outputs
file <- file(paste0('/tmp/numbers_', id, '.json'))
writeLines(toJSON(numbers, auto_unbox=TRUE), file)
close(file)
