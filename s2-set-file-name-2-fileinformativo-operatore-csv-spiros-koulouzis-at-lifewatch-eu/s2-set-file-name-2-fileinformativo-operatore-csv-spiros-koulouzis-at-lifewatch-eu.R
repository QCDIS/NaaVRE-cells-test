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



conf_output = '/tmp/data/'


conf_output = '/tmp/data/'

file_name = "2_FILEinformativo_OPERATORE.csv"
dest = paste(conf_output, file_name,sep = "")
print(dest)
dest_2 = dest



# capturing outputs
file <- file(paste0('/tmp/file_name_', id, '.json'))
writeLines(toJSON(file_name, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/dest_', id, '.json'))
writeLines(toJSON(dest, auto_unbox=TRUE), file)
close(file)
file <- file(paste0('/tmp/dest_2_', id, '.json'))
writeLines(toJSON(dest_2, auto_unbox=TRUE), file)
close(file)
