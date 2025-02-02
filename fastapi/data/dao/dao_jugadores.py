from data.modelo.jugador import Jugador

import mysql.connector

class DaoJugadores:
    
    def get_all(self,db) -> list[Jugador]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM jugadores")

        equipos_en_db = cursor.fetchall()
        equipos : list[Jugador]= list()
        for equipo in equipos_en_db:
            jugador = Jugador(equipo[0], equipo[1])
            equipos.append(jugador)
        cursor.close()
        
        return equipos
    
    def insert(self, db, nombre: str):
        cursor = db.cursor()
        sql = ("INSERT INTO jugadores (nombre) values (%s) ")
        data = (nombre,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def delete(self, db, nombre: str):
        cursor = db.cursor()
        sql = ("DELETE FROM jugadores where nombre = (%s) ")
        data = (nombre,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()