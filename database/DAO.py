from database.DB_connect import DBConnect
from model.aeroporti import Aeroporti
from model.voli import Voli


class DAO():

    @staticmethod
    def getAllFlights(distanza):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """select *
                    from flights f 
                    where DISTANCE > %s"""
        cursor.execute(query, (distanza,))

        result = []

        for row in cursor:
            result.append(Voli(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """select *
                    from airports a"""
        cursor.execute(query)

        result = []

        for row in cursor:
            result.append(Aeroporti(**row))

        cursor.close()
        conn.close()
        return result

