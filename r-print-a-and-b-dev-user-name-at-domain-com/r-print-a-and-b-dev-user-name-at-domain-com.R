setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

option_list = list

option_list = list(


)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


a = opt$a
b = opt$b
id = opt$id.replace('"','')





print(class(a))
print(a + b)



