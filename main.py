from datetime import date
import getPlanets as planets
import getMoon as moon
import DSO

today = date.today().strftime("%Y-%m-%d")
zipcode = 98115


#all_planet_data = planets.get_planets(zipcode, today)
moon_data = moon.get_moon(zipcode, today)
print(moon_data)




