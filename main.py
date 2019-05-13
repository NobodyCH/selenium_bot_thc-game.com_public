from selenium import webdriver
import datetime
import time

def login_func(username, password):
    driver = webdriver.Chrome()
    driver.get('http://thc-game.com')

    mail_field = driver.find_element_by_name("thclogin_name")
    mail_field.send_keys(username)

    pass_field = driver.find_element_by_name("thclogin_pass")
    pass_field.send_keys(password)

    pass_field.submit()
    driver.switch_to.frame(driver.find_element_by_xpath(" / html / frameset / frame"))
    check_activity(driver)
    return driver


def skillen(driver,input_skilltype):
    print("waehle skillen")
    driver.find_element_by_xpath('//*[@id="hmenu"]/table[1]/tbody/tr[2]/td[2]/nav/a[11]').click()
    if input_skilltype == "1":
        print("eingabe erkannt")
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[3]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[3]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) + " sekunden!")
        time.sleep(sleep_time+1)
    elif input_skilltype == "2":
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[4]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[4]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) + " sekunden!")
        time.sleep(sleep_time+1)
    elif input_skilltype == "3":
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[5]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[5]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) + " sekunden!")
        time.sleep(sleep_time+1)
    elif input_skilltype == "4":
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[6]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[6]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) +" sekunden!")
        time.sleep(sleep_time+1)
    elif input_skilltype == "5":
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[7]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[7]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) + " sekunden!")
        time.sleep(sleep_time+1)
    elif input_skilltype == "6":
        driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[8]/td[4]/form').click()
        element = driver.find_element_by_xpath('//*[@id="skilltable"]/tbody/tr[8]/td[5]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Skille: " + str(sleep_time) + " sekunden!")
        time.sleep(sleep_time+1)

def insert_check(skill_type):
    if skill_type is None:
        skill_type = input("Bitte wähle was du Skillen willst [1] Stärke [2] Geschik usw.. [1-6]: ")
    if skill_type == "1" or skill_type == "2" or skill_type == "3" or skill_type == "4" or skill_type == "5" or skill_type == "6":
        print("Skilltyp erkannt!")
        return skill_type
    else:
        skill_type = None
        insert_check(skill_type)



def sleep_gangster():
    needsleep = driver.find_element_by_xpath('//*[@id="gangsterInfoDiv"]/table/tbody/tr[3]/td[2]')
    txt = needsleep.text
    numberprocent, pattern = txt.split()

    if float(numberprocent) <= 9:
        driver.find_element_by_xpath('//*[@id="hmenu"]/table[1]/tbody/tr[2]/td[2]/nav/a[2]').click()
        driver.find_element_by_xpath('//*[@id="gangster"]/div[5]/table/tbody/tr[1]/td[2]/form/input').click()
        element = driver.find_element_by_xpath('// *[ @ id = "stimer"]')
        timer = element.text
        h, m, s = timer.split(':')
        sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
        print("Aktion: Schlafen " + str(sleep_time) + " Sekunden")
        driver.find_element_by_xpath('//*[@id="hmenu"]/table[1]/tbody/tr[2]/td[2]/nav/a[2]').click()
        time.sleep(sleep_time)
    elif float(numberprocent) >= 10:
        print("genug Energie weiter gehts!")

def check_login(driver):
    print("Loging Prüfen..")
    gangsterinfo = driver.find_element_by_xpath('//*[@id="gangsterInfoDiv"]/table/tbody/tr[2]/td[1]')
    print("ok")
    health = str(gangsterinfo.text)
    if health == "Health:":
        print("du bist noch eingeloggt")
    else:
        login_func(username,password)


def action(username, password, driver, input_skilltype):
    try:
        while True:
            sleep_gangster()
            print("gehe zu skillen")
            skillen(driver, input_skilltype)
            check_login(driver)
    except:
            print("fail")
            driver.quit()
            main(input_skilltype)


def main(skill_type):
    global username, password, driver
    # Globale Variablen
    username = "here your mail"
    password = "here your password"
    input_skilltype = insert_check(skill_type)
    driver = login_func(username, password)
    action(username, password, driver, input_skilltype)


def check_activity(driver):
    element = driver.find_element_by_xpath('//*[@id="gangsterInfoDiv"]/table/tbody/tr[8]/td[2]')
    activity = element.text
    print(activity)
    if activity == "schlafen":
        element_task = driver.find_element_by_xpath('//*[@id="overview1"]')
        do_wait_task(element_task, activity, driver)
    elif activity == "skillen":
        element_task = driver.find_element_by_xpath('//*[@id="overview2"]')
        do_wait_task(element_task, activity, driver)
    elif activity == "keine aktivitaet":
        print("kein Skill am laufen")

def do_wait_task(element_task, activity, driver):
        activity_schlafen = element_task.text
        print(activity_schlafen)
        if activity_schlafen == "fertig":
            print("Hui dein Skill ist abgelaufen aber nicht aktualisiert.. aktualisieren..")
            driver.find_element_by_xpath('//*[@id="hmenu"]/table[1]/tbody/tr[2]/td[2]/nav/a[11]').click()
            driver.find_element_by_xpath('//*[@id="hmenu"]/table[1]/tbody/tr[2]/td[2]/nav/a[2]').click()
        else:
            h, m, s = activity_schlafen.split(':')
            sleep_time = int(datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds())
            print("Du bist noch am " + activity + ", erstmal warten: " + str(sleep_time) + " sekunden!")
            time.sleep(sleep_time + 1)

if __name__ == "__main__":
    skill_type = None
    main(skill_type)
