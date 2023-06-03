from datetime import datetime
from tabulate import tabulate
import pymysql
import pandas as pd

tabulate.WIDE_CHARS_MODE = False  # 한글로 인한 테이블 깨짐 현상 해결

def selectMenu():
    print("\n------ 번호 선택 -------\n")
    print("0. 프로그램 종료") # break
    print("1. 회원가입") # signUp
    print("2. 비밀번호 변경") # changePassword
    print("3. 영화 구매하기") # downloadMovie
    print("4. 구입한 영화 목록보기") # showDownloadList
    print("5. 회원탈퇴\n") # signOut
    num = input("0 ~ 5 사이의 숫자를 입력해주세요 : ")
    
    return num

def signUp():
    print("------ 회원가입 ------\n")

    # pymysql을 이용하여 MOVIE DB 연결하기
    movie_db = pymysql.connect(host='localhost',port=3306, user='root', password='zuitopia', db='MOVIE', charset='utf8')
    point = movie_db.cursor(pymysql.cursors.DictCursor)
    
    # 새로운 USER 등록
    inputId = input("ID를 입력해주세요 : ")
    inputPassword = input("비밀번호를 입력해주세요 : ")
    inputName = input("이름/닉네임을 입력해주세요 : ")

    sql = "select * from User where U_ID = %s"
    point.execute(sql, inputId)
    alreadyExist = point.fetchall()

    if (alreadyExist):
        print("\n이미 등록된 ID입니다.")
    else:
        sql_insert = "insert into User (U_ID, PASSWORD, U_NAME, SIGNUPDATE) values (%s, %s, %s, %s)"
        values = (inputId, inputPassword, inputName, datetime.now().strftime("%Y-%m-%d"))
        point.execute(sql_insert, values)
        print("\n회원가입을 축하드립니다!\n")


def changePassword():
    print("------ 비밀번호 변경 ------\n")

    # pymysql을 이용하여 MOVIE DB 연결하기
    movie_db = pymysql.connect(host='localhost',port=3306, user='root', password='zuitopia', db='MOVIE', charset='utf8')
    point = movie_db.cursor(pymysql.cursors.DictCursor)

    userId = input("ID를 입력해주세요 : ")
    userPassword = input("기존 비밀번호를 입력해주세요 : ")
    rePassword = input("새로운 비밀번호를 입력해주세요 : ")

    sql = "select * from User where U_ID = %s and PASSWORD = %s"
    values = (userId, userPassword)
    point.execute(sql, values)
    alreadyExist = point.fetchall()

    if (alreadyExist):
        sql_changePassword = "update User set PASSWORD = %s where U_ID = %s"
        values = (rePassword, userId)
        point.execute(sql_changePassword, values)

        print("\n비밀번호가 변경되었습니다.")
        sql_confirm = "select * from User where U_ID = %s"
        point.execute(sql_confirm, userId)
        alreadyExist = point.fetchall()
        movie_db.close()

        user = pd.DataFrame(alreadyExist)
        print(tabulate(user, headers="keys", tablefmt="fancy_grid", showindex=False, stralign="center"))
    else:
        print("\n" + userId + "은 등록되지 않은 회원이거나 비밀번호를 잘못 입력하였습니다.")



def downloadMovie():
    print("------ 영화 구매하기 ------\n")

    # pymysql을 이용하여 MOVIE DB 연결하기
    movie_db = pymysql.connect(host='localhost',port=3306, user='root', password='zuitopia', db='MOVIE', charset='utf8')
    point = movie_db.cursor(pymysql.cursors.DictCursor)
    
    sql = "select * from Movie"
    point.execute(sql)
    alreadyExist = point.fetchall()
    movie = pd.DataFrame(alreadyExist)
    print(tabulate(movie, headers="keys", tablefmt="fancy_grid", showindex=False, stralign="center"))

    userId = input("본인의 ID를 입력해주세요 : ")
    movieId = int(input("구매할 영화 ID의 번호를 입력해주세요 : "))
    m_id = "M"+str(movieId)

    sql_user = "select * from User where U_ID = %s"
    point.execute(sql_user, userId)
    alreadyExist_user = point.fetchall()

    sql_movie = "select * from Movie where M_ID = %s order by M_ID"
    point.execute(sql_movie, m_id)
    alreadyExist_movie = point.fetchall()

    if (alreadyExist_user and alreadyExist_movie):
        price = movie.iloc[movieId-1, 3]

        sql_insert = "insert into Payment (PAYDATE, U_ID, M_ID, PRICE) values (%s, %s, %s, %s)"
        values = (datetime.now().strftime("%Y-%m-%d"), userId, m_id, price)
        point.execute(sql_insert, values)
        alreadyExist = point.fetchall()

        sql_select = "select User.U_NAME, Movie.TITLE, Movie.PRICE from Payment, Movie, User where Payment.U_ID = User.U_ID and Payment.M_ID = Movie.M_ID order by P_ID desc limit 1"
        point.execute(sql_select)
        alreadyExist = point.fetchall()
        movie_db.close()

        newDownloadList = pd.DataFrame(alreadyExist)

        print("\n 구매가 완료되었습니다.")
        print(tabulate(newDownloadList, headers="keys", tablefmt="fancy_grid", showindex=False, stralign="center"))
    else : 
        print("\n" + userId + "은 등록되지 않은 회원입니다.")


def showDownloadList():
    print("------ 구입한 영화 목록보기 ------\n")
    u_id = input("내역을 검색하고 싶은 회원의 ID를 입력하세요 : ")

    # pymysql을 이용하여 MOVIE DB 연결하기
    movie_db = pymysql.connect(host='localhost',port=3306, user='root', password='zuitopia', db='MOVIE', charset='utf8')
    point = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from User, Payment where User.U_ID = %s and Payment.U_ID = User.U_ID"
    point.execute(sql, u_id)
    alreadyExist = point.fetchall()

    if (alreadyExist):
        # 영화 구매내역
        sql_selectDownloadList = "select Payment.PAYDATE, User.U_NAME, Movie.TITLE, Director.D_NAME, Movie.OPENDATE, Movie.PRICE from User, Movie, Payment, Director where User.U_ID = %s and Payment.U_ID = User.U_ID and Movie.M_ID = Payment.M_ID and Movie.D_ID = Director.D_ID order by Payment.PAYDATE" # 3중 조인
        point.execute(sql_selectDownloadList, u_id)
        alreadyExist = point.fetchall()
        movie_db.close()

        downloadList = pd.DataFrame(alreadyExist)
        print("\n"+u_id+"님께서 구매하신 영화 내역입니다.\n")
        print(tabulate(downloadList, headers="keys", tablefmt="fancy_grid", showindex=False, stralign="center"))
    else:
        print("\n"+ u_id+"님은 등록된 회원이 아니거나 구매내역이 없는 회원입니다.")


def signOut():
    print("------ 회원탈퇴 ------\n")

    # pymysql을 이용하여 MOVIE DB 연결하기
    movie_db = pymysql.connect(host='localhost',port=3306, user='root', password='zuitopia', db='MOVIE', charset='utf8')
    point = movie_db.cursor(pymysql.cursors.DictCursor)

    userId = input("ID를 입력해주세요 : ")
    userPassword = input("비밀번호를 입력해주세요 : ")

    sql = "select * from User where U_ID = %s and PASSWORD = %s"
    values = (userId, userPassword)
    point.execute(sql, values)
    alreadyExist = point.fetchall()

    if (alreadyExist) :
        sql_deleteUser = "delete from User where U_ID = %s"
        point.execute(sql_deleteUser, userId)
        print("\n완료되었습니다. 그동안 이용해주셔서 감사합니다.")
    else : 
        print("\n"+ userId +"님은 등록된 회원이 아니거나 비밀번호를 잘못 입력하였습니다.")


    
while(True):
    num = selectMenu()
    
    if num == "0":
        print("프로그램을 종료합니다.")
        break
    elif num == "1":
        signUp()
    elif num == "2":
            changePassword()
    elif num == "3":
            downloadMovie()
    elif num == "4":
            showDownloadList()
    elif num == "5":
            signOut()
    else :
            print("올바른 번호를 다시 입력해주세요.")
            