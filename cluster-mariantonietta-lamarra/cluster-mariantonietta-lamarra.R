setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)


option_list = list(

make_option(c("--id"), action="store", default=NA, type="character", help="my description"), 
make_option(c("--param_clusterin"), action="store", default=NA, type="character", help="my description")

)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


id <- gsub('"', '', opt$id)
param_clusterin <- gsub('"', '', opt$param_clusterin)





param_cluster = ''
cluster <- c(scan(text = param_clusterin, what = "", sep = ","))



# capturing outputs
file <- file(paste0('/tmp/cluster_', id, '.json'))
writeLines(toJSON(cluster, auto_unbox=TRUE), file)
close(file)
