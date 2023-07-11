import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="cbot")

cursor =mydb.cursor()



def register(name,age,dob,phone,email,pname,occu,income,pin,address,gender,clss,passw):
    cursor.execute("""INSERT INTO `students`(`name`, `age`, `dob`, `phone`, `email`, `occu`, `income`, `pin`, `address`, `gender`, `clss`, `passw`, `pname`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(name,age,dob,phone,email,occu,income,pin,address,gender,clss,passw,pname))   
    mydb.commit()
    return True

def verify(user,passw):


    return True

def view_target_result():
    data = ""

    return data

    
def view_all_result():
    data = ""

    return data

name = "om rajan rawool"
age = "20"
dob = "2-5-2003"
phone = "9604449928"
email = "lrrawool2503@gmail.com"
pname = "rajan sahadev rawool"
occu = "private job"
income = "100000"
pin = "416602"
address= "halwal brahmanwadi"
gender = "male"
clss= "TyBsc cs"
passw = "2503"
print(register(name,age,dob,phone,email,pname,occu,income,pin,address,gender,clss,passw))



