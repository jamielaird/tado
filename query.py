import psycopg2

try:
   connection = psycopg2.connect(database="tado")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select distinct * from inside_temperature where timestamp = (select max(timestamp) from inside_temperature)"

   cursor.execute(postgreSQL_select_Query)
   records = cursor.fetchall() 
   
   print("LATEST READINGS")
   for row in records:
       print("------------------")
       print("Zone = "+str(row[0]))
       print("Timestamp = "+str(row[1]))
       print("Temperature  = "+str(row[2]))

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
