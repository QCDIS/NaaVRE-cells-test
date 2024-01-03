setwd('/app')

# retrieve input parameters

library(optparse)
library(jsonlite)

option_list = list

option_list = list(
make_option(c("--bi"), action="store", default=NA, type='character', help="my description"),
make_option(c("--bk"), action="store", default=NA, type='character', help="my description"),
make_option(c("--clamp"), action="store", default=NA, type='character', help="my description"),
make_option(c("--dplyr"), action="store", default=NA, type='character', help="my description"),
make_option(c("--id"), action="store", default=NA, type='character', help="my description"),
make_option(c("--id"), action="store", default=NA, type='character', help="my description"),
make_option(c("--iris"), action="store", default=NA, type='character', help="my description"),
make_option(c("--luna"), action="store", default=NA, type='character', help="my description"),
make_option(c("--terra"), action="store", default=NA, type='character', help="my description")
)

# set input parameters accordingly
opt = parse_args(OptionParser(option_list=option_list))


bi = opt$bi
bk = opt$bk
clamp = opt$clamp
dplyr = opt$dplyr
id = opt$id
id = opt$id
iris = opt$iris
luna = opt$luna
terra = fromJSON(opt$terra)





install.packages('terra')

install.packages('terra', repos='https://rspatial.r-universe.dev')
library(terra)
install.packages('luna', repos='https://rspatial.r-universe.dev')

install.packages('dplyr')
library(dplyr)
iris
plot(iris[,1],iris[,2])

library(luna)
prod <- getProducts()
head(prod)


modis <- getProducts("^MOD|^MYD|^MCD")
head(modis)


session_wd <- tempdir() # this is a temporay working space, you can change to your local WD

area <- c(4.5,5.5, 53, 53.5)

mf <- luna::getNASA("MOD09A1", start_date = "2019-05-29",end_date =  "2019-05-30",path = session_wd, aoi=area, download = TRUE,username="Qingfly",password="Nioo&Nioz2023")


available.files <- list.files(path=session_wd, pattern=".hdf", all.files=FALSE, 
           full.names=FALSE)


library(terra)
r_mod <- rast(available.files)
r_mod
dim(r_mod)
names(r_mod)
plot(r_mod)

vi <- function(img, NIR_b, RED_b) {
  bk <- img[[NIR_b]]
  bi <- img[[RED_b]]
  vi <- (bk - bi) / (bk + bi)
  return(vi)
}


names(r_mod)
ndvi <- vi(r_mod, "sur_refl_b02", "sur_refl_b01")
plot(ndvi, col=rev(terrain.colors(10)), main = "NDVI")
hist(ndvi)
?clamp
veg <- clamp(ndvi, lower= 0.3, upper=1)
plot(veg,col=rev(terrain.colors(10)))







