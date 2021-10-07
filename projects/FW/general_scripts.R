install.packages('shiny')
install.packages("dygraphs")


library(dygraphs)
lungDeaths <- cbind(mdeaths, fdeaths)
dygraph(lungDeaths)