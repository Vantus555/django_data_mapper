import sqlite3
from django.db import models

# Create your models here.


class Mapper():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            "db.sqlite3", check_same_thread=False)
        self.cursor = self.connection.cursor()
        # Создаем таблицу если ее нет
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Student(first_name text, last_name text, course int)'''
        )
        # Отправляем запрос
        self.connection.commit()

    def getStuden(self, first_name):
        self.cursor.execute(
            f'SELECT * FROM Student WHERE first_name="{first_name}" LIMIT 1'
        )

        records = self.cursor.fetchall()
        if len(records) > 0:
            Student(records[0][0], records[0][1], records[0][2])
        else:
            return None

    def getAllStudents(self):
        self.cursor.execute(
            f'SELECT * FROM Student'
        )

        # Берем все записи
        records = self.cursor.fetchall()
        if len(records) > 0:
            results = []
            for i in records:
                results.append(Student(i[0], i[1], i[2]))
            return results
        else:
            return None

    def newStudent(self, first_name, last_name, course):
        # Создаем запрос на создание
        self.cursor.execute(
            f'INSERT INTO Student VALUES("{first_name}", "{last_name}", "{course}")'
        )
        # Отправляем запрос
        self.connection.commit()


class Student():
    def __init__(self, first_name, last_name, course) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
