library(DBI)
library(RPostgres)

conexion <- dbConnect(
  RPostgres::Postgres(),
  dbname = "paloma",
  host = "localhost",
  port = 5432,
  user = "examen",
  password = "12345"
)

sexenio1 <- dbGetQuery(conexion, "SELECT fecha, cotizacion FROM sexenio1")
sexenio2 <- dbGetQuery(conexion, "SELECT fecha, cotizacion FROM sexenio2")

dbDisconnect(conexion)

x1 <- sexenio1$cotizacion
x2 <- sexenio2$cotizacion

# Sexenio 1
print(mean(x1, na.rm = TRUE))
print(var(x1, na.rm = TRUE))
print(sd(x1, na.rm = TRUE))
print(min(x1, na.rm = TRUE))
print(max(x1, na.rm = TRUE))
print(max(x1, na.rm = TRUE) - min(x1, na.rm = TRUE))

# Sexenio 2
print(mean(x2, na.rm = TRUE))
print(var(x2, na.rm = TRUE))
print(sd(x2, na.rm = TRUE))
print(min(x2, na.rm = TRUE))
print(max(x2, na.rm = TRUE))
print(max(x2, na.rm = TRUE) - min(x2, na.rm = TRUE))
