library(threejs)

filter <- function(mag_min){
  seismes_filter <- seismes[apply(seismes["mag"],1, function(x) all(x>=mag_min)),]

  seismes_filter <- sample(seismes_filter,dim(seismes_filter)[1],replace=TRUE)

  rownames(seismes_filter) <- NULL

  seismes_filter
}

#on charge la base de données
seismes = read.csv("seismes_2014.csv");
seismes_filter <- filter(3)

#on affiche nos données sur un globe terrestre
palette <- c("#000000", "#663399", "#FF0099", "#003399", "#99FFFF", "#99FF33", "yellow", "orange", "red")
col <- palette[floor(seismes_filter$mag) + 1]
globejs(lat=seismes_filter$lat,
        long=seismes_filter$lon,
        value=10*(seismes_filter$mag),
        Atmosphere=FALSE,
        color=col,
        bg="white")
