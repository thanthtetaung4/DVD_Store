import sqlite3
strr = 'dvd_9999'

print(ord(strr[4]), ord(strr[5]), ord(strr[6]), ord(strr[7]))

print(chr(48), chr(48), chr(48), chr(58))

only_numb = strr[4:7]
print(only_numb)
new_numb = (int(only_numb) + 1)
new_numb = str(new_numb)
print(new_numb)

new_id = '0' * (4 - len(new_numb)) + new_numb
print(new_id)
if int(new_id) > 9999:
    print('error')

# movie_name = input("Enter movie name: \t")
# stars = input("Enter Stars:\t")
# producer = input("Enter Producer:\t")
# director = input("Enter Director:\t")
# company = input("Enter Company:\t")
# copies = (input("Enter Copies:\t"))
# released_date = input("Enter Released Date:\t")
# dvd_id = 'dvd_11111'
# query = "insert into dvd (movie_name, dvd_id, stars, producer, company, released_data, director, copies) values ('" + movie_name + "','" + dvd_id + "','" + stars + "','" + producer + "','" + company + "','" + released_date + "','" + director + "','" + copies + "');"
# con = sqlite3.connect(r"database/dvd_store.db")
# cur = con.cursor()
# cur.execute(query)
# con.commit()
# con.close()