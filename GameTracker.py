import json
from datetime import datetime

class Genre:
    def __init__(self, name, description=""):
        self.__id = None
        self.__name = name
        self.__description = description
    
    @property
    def id(self):
        return self.__id
    @property 
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @id.setter
    def id(self,id):
        self.__id = id
    @name.setter
    def name(self,name):
        self.__name = name
    @description.setter
    def description(self, description):
        self.__description = description

    def show_genre(self):
        print("Nombre:",self.__name)
        print("Descripcion:",self.__description)

    def show_genre_with_id(self):
        self.show_genre()
        print("ID:",self.__id)
class GenreList:
    def __init__(self,path):
        self.__list = []
        self.__path = path
    
    def load_genre_list(self):
        try:
            with open(self.__path,"r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Sin archivos por cargar")
            self.__list = []
        except FileNotFoundError:
            print("Error:Archivo no encontrado.")
            self.__list = []
        else:
            self.__list = []
            for d in data:
                genre =Genre(d["Name"],d["Description"])
                genre.id = d["Id"]
                self.__list.append(genre)
            print("Se cargaron",len(self.__list),"generos")
    
    def save_genre_list(self):
        data = []
        for genre in self.__list:
            data.append({
                "Id": genre.id,
                "Name" : genre.name,
                "Description" : genre.description
            })
        with open(self.__path,"w") as file:
            json.dump(data,file,indent=4)

    def add_genre_list(self,genre):
        initial_id = -1
        for g in self.__list:
            if g.id >= initial_id:
                initial_id = g.id
        genre.id = initial_id + 1
        self.__list.append(genre)
        
    #show genre list
    def show_genre_list(self):
        print("-------Generos-------")
        for genre in self.__list:
            genre.show_genre()
            print("--------------------")
    
    def show_genre_list_with_id(self):
        print("-------Generos-------")
        for genre in self.__list:
            genre.show_genre_with_id()
            print("--------------------")
    #Update genre
    def update_genre_name_by_id(self, id, name):
        for genre in self.__list:
            if genre.id == id:
                genre.name = name
                print("El nombre del genero con id",id,"se cambio a:",name)
                break

    def update_genre_description_by_id(self, id, description):
        for genre in self.__list:
            if genre.id == id:
                genre.description = description
                print("La descripcion del genero con id",id,"se cambio a:",description)
                break
    #Delete genre
    def delete_genre_by_id(self, id):
        for i,genre in enumerate(self.__list):
            if genre.id == id:
                del self.__list[i]
                print("Se elimino el genero de Id:",id)
                break

    def get_genre_by_id(self,id)->Genre:
        for genre in self.__list:
            if genre.id == id:
                return genre

class Platform:
    def __init__(self, name, description = ""):
        self.__id = None
        self.__name = name
        self.__description = description
    
    @property
    def id(self):
        return self.__id
    @property 
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @id.setter
    def id(self,id):
        self.__id = id
    @name.setter
    def name(self,name):
        self.__name = name
    @description.setter
    def description(self, description):
        self.__description = description


    def show_platform(self):
        print("Nombre:",self.__name)
        print("Descripcion:",self.__description)
    def show_platform_with_id(self):
        self.show_platform()
        print("ID:",self.__id)
class PlatformsList:
    def __init__(self, path):
        self.__list = []
        self.__path = path

    def load_platform_list(self):
        try:
            with open(self.__path,"r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Sin archivos por cargar")
            self.__list = []
        except FileNotFoundError:
            print("Error:Archivo no encontrado.")
            self.__list = []
        else:
            self.__list = []
            for p in data:
                platform =Platform(p["Name"],p["Description"])
                platform.id = p["Id"]
                self.__list.append(platform)
    
    def save_platform_list(self):
        data = []
        for platform in self.__list:
            data.append({
                "Id": platform.id,
                "Name": platform.name,
                "Description":platform.description
            })
        with open(self.__path, "w") as file:
            json.dump(data,file,indent=4)

    def add_platform(self, platform):
        initial_id = -1
        for p in self.__list:
            if p.id >= initial_id:
                initial_id = p.id
        platform.id = initial_id +1
        self.__list.append(platform)
    
    #show platform list
    def show_platform_list(self):
        print("-------Plataformas-------")
        for platform in self.__list:
            platform.show_platform()
            print("-------------------------")

    def show_platform_list_with_id(self):
        print("-------Plataformas-------")
        for platform in self.__list:
            platform.show_platform_with_id()
            print("-------------------------")  

    #update plataform
    def update_platform_name_by_id(self,id,name):
        for platform in self.__list:
            if platform.id == id:
                platform.name = name
                print("El nombre de la plataforma con id",id,"se cambio a:",name)
                break
    
    def update_platform_description_by_id(self,id,description):
        for platform in self.__list:
            if platform.id == id:
                platform.description = description
                print("La descripcion de la plataforma con id",id,"se cambio a:",description)
                break
    #delete platform
    def delete_platform_by_id(self,id):
        for i,platform in enumerate(self.__list):
            if platform.id == id:
                del self.__list[i]
                print("Se elimino la plataforma del id",id)
                break

    def get_platform_by_id(self,id):
        for platform in self.__list:
            if platform.id == id:
                return platform

    def get_len(self):
        return len(self.__list)

class Game:
    def __init__(self, name, genres_list : list, platform, completed, description = "", rating = None, completed_date = None):
        self.__id = None
        self.__name = name
        self.__description = description
        self.__genres_list = genres_list
        self.__platform = platform
        self.__completed = completed
        self.__rating = rating
        self.__completed_date = completed_date

    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def genres_list(self):
        return self.__genres_list
    @property
    def platform(self):
        return self.__platform
    @property
    def completed(self):
        return self.__completed
    @property
    def description(self):
        return self.__description
    @property
    def rating(self):
        return self.__rating
    @property
    def completed_date(self):
        return self.__completed_date
    
    @id.setter
    def id(self,id):
        self.__id = id
    @name.setter
    def name(self,name):
        self.__name = name
    @genres_list.setter
    def genres_id(self, genres_list):
        self.__genres_list = genres_list
    @platform.setter
    def platform(self, platform):
        self.__platform = platform
    @completed.setter
    def completed(self,completed):
        self.__completed = completed
    @description.setter
    def description(self, description):
        self.__description = description
    @rating.setter
    def rating(self,rating):
        self.__rating = rating
    @completed_date.setter
    def completed_date(self,completed_date):
        self.__completed_date = completed_date

    def add_genre_to_game(self,genre:Genre):
        self.__genres_list.append(genre)
    def delete_genre_to_game_by_id(self,id):
        for i,genre in enumerate(self.__genres_list):
            if genre.id == id:
                del self.genres_list[i]
                break
    def show_game(self):
        print("******", self.__name,"******")
        print("Description:",self.__description)
        print("--Generos:")
        for genre in self.genres_list:
            genre.show_genre()
            print("--------")
        print("--Plataforma:")
        self.__platform.show_platform()
        print("--------")
        print("Completado:","Terminado" if self.__completed else "Pendiente")
        print(f"Calificacion: {self.__rating}" if self.__rating is not None else "Sin Calificar!!")
        print(f"Se completo el: {self.__completed_date}" if self.__completed_date is not None else "Sin terminar!!")
    def show_game_name_and_id(self):
        print("--ID:", self.__id, ", Nombre:",self.__name)
    def show_game_with_id_genres(self):
        print(f"-----{self.__name}---------")
        for genre in self.__genres_list:
            print(f"Id: {genre.id}, Nombre: {genre.name}")
class GamesList:
    def __init__(self, path):
        self.__list = []
        self.__path = path
    
    def get_list(self):
        return self.__list

    def load_games_list(self,genre_list:GenreList=None, platform_list:PlatformsList=None):
        try:
            with open(self.__path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Sin archivo por cargar")
            self.__list = []
        except FileNotFoundError:
            print("Error: Archivo no encontrado")
            self.__list = []
        else:
            self.__list = []
            for g in data:
                genre_list_to_add = []
                for genre_dicc in g["Genres_list"]:
                    genre = genre_list.get_genre_by_id(genre_dicc["Id"])
                    genre_list_to_add.append(genre)
                platform = platform_list.get_platform_by_id(g["Platform"]["Id"])
                game = Game(g["Name"],genre_list_to_add,platform,g["Completed"],g["Description"],g["Rating"],datetime.strptime(g["Completed_Date"],"%y-%m-%d").date() if g["Completed_Date"] is not None else None )
                game.id = g["Id"]
                self.__list.append(game)    

    def save_games_list(self):
        data = []
        
        for game in self.__list:
            genre_dicc = []
            for genre in game.genres_list:
                genre_dicc.append({
                    "Id" : genre.id,
                    "Name" : genre.name,
                    "Description" : genre.description
                })
            platform = {
                "Id": game.platform.id,
                "Name" : game.platform.name,
                "Description" : game.platform.description
            }
            data.append({
                "Id" : game.id,
                "Name" : game.name,
                "Genres_list" : genre_dicc,
                "Platform" : platform,
                "Completed" : game.completed,
                "Description" : game.description,
                "Rating" : game.rating,
                "Completed_Date" : game.completed_date.strftime("%y-%m-%d") if game.completed_date is not None else None
            })
        with open(self.__path,"w") as file:
            json.dump(data,file, indent=4)

    def add_game(self, game):
        initial_id = -1
        for g in self.__list:
            if g.id > initial_id:
                initial_id = g.id
        game.id = initial_id + 1
        self.__list.append(game)

    def show_games(self):
        print("#########Juegos#########")
        for game in self.__list:
            game.show_game()
            print("########################")

    def get_game_by_id(self,id) -> Game:
        for game in self.__list:
            if game.id == id:
                return game

    def show_games_with_id(self):
        print("---------Juegos-----------")
        for game in self.__list:
            game.show_game_name_and_id()
            print("--------------------------")        

    def show_games_completed(self):
        games_complete = [game for game in self.__list if game.completed]
        print("-------Juegos Completados ---------")
        for game in games_complete:
            game.show_game_name_and_id()
            print("-----------------------------------")
    
    def show_games_not_completed(self):
        games_not_completed = [game for game in self.__list if not game.completed]
        for game in games_not_completed:
            game.show_game_name_and_id()
            print("-----------------------------------")

    #Mostrar juegos en cierto orden
    def show_games_ordered_by_name(self):
        games_by_name = sorted(self.__list, key=lambda game: game.name.lower())
        print("-------Juegos Ordenados por Nombre ---------")
        for game in games_by_name:
            game.show_game_name_and_id()
            print("-----------------------------------")
    def show_games_ordered_by_date(self):
        games_by_date = sorted(self.__list,key=lambda game: game.completed_date if game.completed_date is not None else None)
        print("-------Juegos Ordenados por Fecha ---------")
        for game in games_by_date:
            game.show_game_name_and_id()
            print("Fecha: ", game.completed_date.strftime("%y-%m-%d") if game.completed_date is not None else None)
            print("-----------------------------------")
    def show_games_ordered_by_rating(self):
        games_by_rating = sorted(self.__list, key=lambda game: game.rating, reverse=True)
        print("-------Juegos Ordenados por Calificación ---------")
        for game in games_by_rating:
            game.show_game_name_and_id()
            print("Calificación: ", game.rating)
            print("-----------------------------------")

def get_date():
    end_get_date = False
    while not end_get_date:
        print("Terminaste el juego el dia de hoy?")
        print("1)Si")
        print("2)No")
        answer = get_number("Respuesta:")
        if answer == 1:
            date = datetime.today().date()
            end_get_date = True
        elif answer == 2:
            while True:
                date_str = input("Ingresa fecha en formato(AAAA-MM-DD):")
                try:
                    date = datetime().strptime(date_str,"%y-%m-%d").date()
                    break
                except ValueError:
                    print("Formato incorrecto")
            end_get_date = True
        else:
            print("Introduce una opcion valida.")
    return date

def get_number(text):
    is_number = False
    while not is_number:
        try:
            number = int(input(text))
        except:
            print("Error se tiene que introducir un numero")
        else:
            is_number = True
    return number

#seccion del genero
def genre_section(genre_list:GenreList):
    genre_list.show_genre_list()
    end = False
    while not end:
        print("""Menu Genero
1)Agregar genero
2)Actualizar genero
3)Borrar genero
4)Salir
        """)
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            add_genre_process(genre_list)
        elif opc == 2:
            update_genre_process(genre_list)
        elif opc == 3:
            delete_genre_process(genre_list)
        elif opc == 4:
            end = True
        elif opc not in [1,2,3,4]:
            print("Opcion no valida intente de nuevo")
def add_genre_process(genre_list:GenreList):
    print("Agregando nuevo genero.")
    name = input("Nombre:")
    description = input("Descripcion:")
    genre = Genre(name,description)
    genre_list.add_genre_list(genre)
def update_genre_process(genre_list:GenreList):
    genre_list.show_genre_list_with_id()
    id = get_number("Selecciona el id del genero a modificar(-1 para salir):")
    if id > 0 :
        end = False
        while not end:
            print("---Que quieres modificar---")
            print("1)Nombre")
            print("2)Descripcion")
            print("3)Salir")
            opc = get_number("Selecciona una opcion:")
            if opc == 1:
                name = input("Introduce el nuevo nombre:")
                genre_list.update_genre_name_by_id(id,name)
            elif opc == 2:
                description = input("Introduce la nueva descripcion:")
                genre_list.update_genre_description_by_id(id,description)
            elif opc ==3:
                end = True
            elif opc not in [1,2,3]:
                print("Opcion no valida")
def delete_genre_process(genre_list:GenreList):
    genre_list.show_genre_list_with_id()
    id = get_number("Selecciona el id del genero a eliminar(-1 para salir):")
    if id > 0:
        genre_list.delete_genre_by_id(id)
#Seccion de plataformas
def platform_section(platform_list:PlatformsList):
    platform_list.show_platform_list()
    end = False
    while not end:
        print("""Menu Plataforma
1)Agregar plataforma
2)Actualizar plataforma
3)Borrar plataforma
4)Salir
        """)
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            add_platform_process(platform_list)
        elif opc == 2:
            update_platform_process(platform_list)
        elif opc == 3:
            delete_platform_process(platform_list)
        elif opc == 4:
            end = True
        elif opc not in [1,2,3,4]:
            print("Opcion no valida, intenta de nuevo.")
def add_platform_process(platform_list:PlatformsList):
    print("Agregando nueva plataforma.")
    name = input("Nombre:")
    description = input("Descripcion:")
    platform = Platform(name,description)
    platform_list.add_platform(platform)
def update_platform_process(platform_list:PlatformsList):
    platform_list.show_platform_list_with_id()
    id = get_number("Selecciona el id de la plataforma a modificar(-1 para salir):")
    if id > 0 :
        end = False
        while not end:
            print("---Que quieres modificar---")
            print("1)Nombre")
            print("2)Descripcion")
            print("3)Salir")
            opc = get_number("Selecciona una opcion:")
            if opc == 1:
                name = input("Introduce el nuevo nombre:")
                platform_list.update_platform_name_by_id(id,name)
            elif opc == 2:
                description = input("Introduce la nueva descripcion:")
                platform_list.update_platform_description_by_id(id,description)
            elif opc ==3:
                end = True
            elif opc not in [1,2,3]:
                print("Opcion no valida")
def delete_platform_process(platform_list:PlatformsList):
    platform_list.show_platform_list_with_id()
    id = get_number("Selecciona el id de la plataforma a eliminar(-1 para salir):")
    if id > 0:
        platform_list.delete_platform_by_id(id)
#Seccion de juegos
def add_game_process(game_list:GamesList,genre_list:GenreList,platform_list:PlatformsList):
    print("Añadiendo un juego.")
    exit = input("Escribe lo que sea para continar(-1 para salir):")
    if exit != -1:
        name = input("Introduce el nombre del juego:")
        end_genre_selection = False
        genres_to_add = []
        #hacer la lista de generos para el juego
        while not end_genre_selection:
            print("Generos a agregar")
            genre_list.show_genre_list_with_id()
            opc = get_number("Selcciona el id del genero a agregar(-1 salir):")
            if opc < 0:
                if len(genres_to_add) == 0:
                    try:
                        repeated = False
                        genre_to_add = genre_list.get_genre_by_id(0)
                        for genre in genres_to_add:
                            if genre.id == genre_to_add.id:
                                repeated = True
                                break
                        if not repeated:
                            genres_to_add.append(genre_to_add)
                            end_genre_selection = True
                        else:
                            end_genre_selection = True
                    except:
                        end_genre_selection = True
                else:
                    end_genre_selection = True
            else:
                try:
                    repeated = False
                    genre_to_add = genre_list.get_genre_by_id(opc)
                    for genre in genres_to_add:
                        if genre.id == genre_to_add.id:
                            repeated = True
                            break
                    if not repeated:
                        genres_to_add.append(genre_to_add)
                    else:
                        print("Este genero se esta repitiendo")
                except:
                    print("Error:fuera de rango")
        #agregar la plataforma en la que se jugo este juego
        print("Agregando plataforma")
        platform_list.show_platform_list_with_id()
        adding_platform = False
        #se tiene que agregar lo que pasaria si no se tiene ninguna plataforma registrada
        if platform_list.get_len() > 0: 
            while not adding_platform:
                opc = get_number("Selecciona el id de la plataforma a agregar:")
                try:
                    platform = platform_list.get_platform_by_id(opc)
                except:
                    print("Error:Fuera de rango selecciona una opcion valida")
                else:
                    adding_platform = True
        else:
            platform = platform_list.get_platform_by_id(0)

        end_complete_game = False
        while not end_complete_game:
            print("Se termino el juego?")
            print("1)Si")
            print("2)No")
            opc = get_number("Opcion:")
            if opc == 1:
                completed = True
                end_complete_game = True
            elif opc == 2:
                completed = False
                end_complete_game = True
            else:
                print("Selecciona una opcion valida")
        description = input("Escribe una descripcion del videojuego:")
        end_game_rating = False
        while not end_game_rating:
            print("Califica el videojuego del 1 al 10.")
            rate = get_number("Calificacion:")
            if rate > 10 or rate < 0:
                print("Da una respuesta valida")
            else:
                end_game_rating = True 
        if completed:
            date = get_date()
        else:
            date = None
        game = Game(name,genres_to_add,platform,completed,description,rate,date)
        game_list.add_game(game)
        print(f"El juego {game.name} fue agregado")
def show_games_and_filter_section(game_list:GamesList):
    game_list.show_games()
    while True:
        print("Opciones para ordenar.")
        print("1)Por alfabeto.")
        print("2)Por fecha.")
        print("3)Por calificacion.")
        print("4)Salir.")
        opc = get_number("Elije una opcion:")
        if opc == 1:
            game_list.show_games_ordered_by_name()
        elif opc == 2:
            game_list.show_games_ordered_by_date()
        elif opc == 3:
            game_list.show_games_ordered_by_rating()
        elif opc == 4:
            print("Saliste de la seccion de ordenar juegos.")
            break
        else:
            print("Selecciona una opcion valida.")
    pass
def completed_game_process(game_list:GamesList):

    while True:
        game_list.show_games_not_completed()
        opc = get_number("Id del juego completado (-1 para salir):")
        if opc < 0:
            print("Saliste de la seccion de completar un juego.")
            break
        else:
            try:
                game_selected = game_list.get_game_by_id(opc)
            except:
                print("Error:elecciona una opcion valida.")
            else:
                game_selected.completed = True
                date = get_date()
                game_selected.completed_date = date
                print(f"El juego {game_selected.name} fue completado.")
                break

def search_game_process(game_list:GamesList,genre_list:GenreList, platform_list:PlatformsList):
    while True:
        print("-------Buscar juegos-------")
        print("1)Buscar juego por nombre")
        print("2)Buscar juego por genero")
        print("3)Buscar juego por plataforma")
        print("4)Buscar juegos terminados")
        print("5)Buscar juegos pendientes")
        print("6)Salir")
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            search_game_by_name(game_list)
        elif opc == 2:
            search_game_by_genre(game_list,genre_list)
        elif opc == 3:
            search_game_by_platform(game_list,platform_list)
        elif opc == 4:
            search_game_by_completed(game_list)
        elif opc == 5:
            search_game_by_not_completed(game_list)
        elif opc == 6:
            print("Saliste de la seccion de buscar juegos.")
            break
        else:
            print("Selecciona una opcion valida.")

def search_game_by_name(game_list:GamesList):
    name = input("Introduce el nombre del juego a buscar:")
    found_games = [game for game in game_list.get_list() if name.lower() in game.name.lower()]
    if found_games:
        print(f"Se encontraron {len(found_games)} juegos con el nombre {name}:")
        for game in found_games:
            game.show_game()
            print("--------------------")
    else:
        print(f"No se encontraron juegos con el nombre {name}.")

def search_game_by_genre(game_list:GamesList, genre_list:GenreList):
    while True:
        genre_list.show_genre_list_with_id()
        id = get_number("Selecciona el id del genero a buscar(-1 para salir):")
        if id >= 0:
            try:
                genre = genre_list.get_genre_by_id(id)
            except:
                print("Error:Selecciona una opcion valida")
                break
            else:
                found_games = [game for game in game_list.get_list() if genre in game.genres_list]
                if found_games:
                    print(f"Se encontraron {len(found_games)} juegos con el genero {genre.name}:")
                    for game in found_games:
                        game.show_game()
                        print("--------------------")
                    break
                else:
                    print(f"No se encontraron juegos con el genero {genre.name}.")
        elif id == -1:
            print("Saliste de la seccion de buscar por genero.")
            break

def search_game_by_platform(game_list:GamesList, platform_list:PlatformsList):
    while True:
        platform_list.show_platform_list_with_id()
        id = get_number("Selecciona el id de la plataforma a buscar(-1 para salir):")
        if id >= 0:
            try:
                platform = platform_list.get_platform_by_id(id)
            except:
                print("Error:Selecciona una opcion valida")
                break
            else:
                found_games = [game for game in game_list.get_list() if game.platform.id == platform.id]
                if found_games:
                    print(f"Se encontraron {len(found_games)} juegos en la plataforma {platform.name}:")
                    for game in found_games:
                        game.show_game()
                        print("--------------------")
                    break
                else:
                    print(f"No se encontraron juegos en la plataforma {platform.name}.")
        elif id == -1:
            print("Saliste de la seccion de buscar por plataforma.")
            break

def search_game_by_completed(game_list:GamesList):
    completed_games = [game for game in game_list.get_list() if game.completed]
    if completed_games:
        print(f"Se encontraron {len(completed_games)} juegos completados:")
        for game in completed_games:
            game.show_game()
            print("--------------------")
    else:
        print("No se encontraron juegos completados.")

def search_game_by_not_completed(game_list:GamesList):
    not_completed_games = [game for game in game_list.get_list() if not game.completed]
    if not_completed_games:
        print(f"Se encontraron {len(not_completed_games)} juegos pendientes:")
        for game in not_completed_games:
            game.show_game()
            print("--------------------")
    else:
        print("No se encontraron juegos pendientes.")

def delete_or_update_game_process(game_list:GamesList, genre_list:GenreList, platform_list:PlatformsList):
    in_process = True
    while in_process:
        game_list.show_games_with_id()
        id = get_number("Selecciona el id del juego a borrar o actualizar(-1 para salir):")
        if id >= 0:
            try:
                game = game_list.get_game_by_id(id)
            except:
                print("Error:Selecciona una opcion valida")
            else:
                end = False
                while not end:
                    print("Juego seleccionado:")
                    game.show_game()
                    print("1)Borrar juego")
                    print("2)Actualizar juego")
                    print("3)Salir")
                    opc = get_number("Selecciona una opcion:")
                    if opc == 1:
                        game_list.get_list().remove(game)
                        print(f"El juego {game.name} fue eliminado.")
                        end = True
                    elif opc == 2:
                        update_game_process(game,genre_list,platform_list)
                    elif opc == 3:
                        print("Saliste de la seccion de borrar o actualizar juegos.")
                        end = True
                    else:
                        print("Opcion no valida intenta de nuevo")
        elif id == -1:
            print("Saliste de la seccion de borrar o actualizar juegos.")
            in_process = False
    
def update_game_process(game:Game, genre_list:GenreList, platform_list:PlatformsList):
    end = False
    while not end:
        print("----Que quieres modificar----")
        print("1)Nombre")
        print("2)Descripcion")
        print("3)Generos")
        print("4)Plataforma")
        print("5)Fecha de completado")
        print("6)Calificacion")
        print("7)Salir")
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            name = input("Introduce el nuevo nombre:")
            game.name = name
            print("El nombre del juego se cambio a:",name)
        elif opc == 2:
            description = input("Introduce la nueva descripcion:")
            game.description = description
            print("La descripcion del juego se cambio a:",description)
        elif opc == 3:
            end_genre_selection = False
            while not end_genre_selection:
                print("Generos actuales del juego:")
                for genre in game.genres_list:
                    genre.show_genre_with_id()
                    print("--------")
                print("1)Agregar genero")
                print("2)Eliminar genero")
                print("3)Salir")
                opc_genre = get_number("Selecciona una opcion:")
                if opc_genre == 1:
                    genre_list.show_genre_list_with_id()
                    id = get_number("Selecciona el id del genero a agregar(-1 para salir):")
                    if id >= 0:
                        try:
                            genre_to_add = genre_list.get_genre_by_id(id)
                        except:
                            print("Error:Selecciona una opcion valida")
                        else:
                            repeated = False
                            for genre in game.genres_list:
                                if genre.id == genre_to_add.id:
                                    repeated = True
                                    break
                            if not repeated:
                                game.add_genre_to_game(genre_to_add)
                                print(f"El genero {genre_to_add.name} fue agregado al juego {game.name}.")
                            else:
                                print("Este genero ya esta en el juego.")
                    elif id == -1:
                        pass
                elif opc_genre == 2:
                    if len(game.genres_list) > 0:
                        game.show_game_with_id_genres()
                        id = get_number("Selecciona el id del genero a eliminar(-1 para salir):")
                        if id > 0:
                            genre_to_delete = None
                            for genre in game.genres_list:
                                if genre.id == id:
                                    genre_to_delete = genre
                                    break
                                if genre_to_delete is not None:
                                    game.delete_genre_to_game_by_id(id)
                                    print(f"El genero {genre_to_delete.name} fue eliminado del juego {game.name}.")
                                else:
                                    print("Error:Selecciona una opcion valida")
                        elif id == -1:
                            pass
                elif opc_genre == 3:
                    end_genre_selection = True
        elif opc == 4:
            #mostrar la plataforma actual y dar la opcion de cambiarla a otra o salir
            print("Plataforma actual del juego:")
            game.platform.show_platform_with_id()
            print("1) Cambiar plataforma")
            print("2) Salir")
            opc_platform = get_number("Selecciona una opcion:")
            if opc_platform == 1:
                platform_list.show_platform_list_with_id()
                id = get_number("Selecciona el id de la nueva plataforma:")
                if id >= 0:
                    try:
                        platform = platform_list.get_platform_by_id(id)
                    except:
                        print("Error:Selecciona una opcion valida")
                    else:
                        game.platform = platform
                        print(f"La plataforma del juego {game.name} fue cambiada a {platform.name}.")
                else:
                    print("Error:Selecciona una opcion valida")
            elif opc_platform == 2:
                pass
            else:
                print("Error:Selecciona una opcion valida")
        elif opc == 5:
            print("Cambiando fecha de completado del juego.")
            print("Fecha actual:", game.completed_date.strftime("%y-%m-%d") if game.completed_date is not None else "No tiene fecha de completado")
            print("1)Eliminar fecha de completado")
            print("2)Establecer nueva fecha de completado")
            print("3)Salir")
            opc_date = get_number("Selecciona una opcion:")
            if opc_date == 1:
                game.completed_date = None
                print(f"La fecha de completado del juego {game.name} fue eliminada.")
            elif opc_date == 2:
                game.completed_date = get_date()
                print(f"La fecha de completado del juego {game.name} fue cambiada a {game.completed_date}.")
            elif opc_date == 3:
                pass
        elif opc == 6:
            print("Cambiando calificacion del juego.")
            print("Calificacion actual:", game.rating if game.rating is not None else "No tiene calificacion")
            print("1)Modificar calificacion")
            print("2)salir")
            opc_rate = get_number("Selecciona una opcion:")
            if opc_rate == 1:
                new_rating = get_number("Ingresa la nueva calificacion:")
                game.rating = new_rating
                print(f"La calificacion del juego {game.name} fue cambiada a {game.rating}.")
            elif opc_rate == 2:
                pass
        elif opc == 7:
            end = True
def main_menu():
    print("""Menu
1)Agregar un juego
2)Ver lista de juegos
3)Completar un juego
4)Buscar juegos
5)Borrar o actualizar juegos
6)Extras
7)Guardar
8)Salir
""")

def extra_menu(genre_list,platform_list):
    end = False
    while not end:
        print("""Menu de extras
1)Ver lista de generos
2)Ver lista de plataformas
3)Salir
        """)
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            genre_section(genre_list)
        elif opc == 2:
            platform_section(platform_list)
        elif opc == 3:
            end = True
        elif opc not in [1,2,3]:
            print("Opcion no valida intenta de nuevo")

def main():
    genre_list = GenreList("Data/Genre.json")
    platform_list = PlatformsList("Data/Platforms.json")
    game_list = GamesList("Data/Games.json")
    platform_list.load_platform_list()
    genre_list.load_genre_list()
    game_list.load_games_list(genre_list,platform_list)
    end = False
    while not end:
        main_menu()
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            add_game_process(game_list,genre_list,platform_list)
        elif opc == 2:
            show_games_and_filter_section(game_list)
        elif opc == 3:
            completed_game_process(game_list)
        elif opc == 4:
            search_game_process(game_list,genre_list,platform_list)
        elif opc == 5:
            delete_or_update_game_process(game_list,genre_list,platform_list)
        elif opc == 6:
            extra_menu(genre_list,platform_list)
        elif opc == 7:
            genre_list.save_genre_list()
            platform_list.save_platform_list()
            game_list.save_games_list()
            print("Todos los datos guardados")
        elif opc == 8:
            end = True
        elif opc not in [1,2,3,4,5,6,7,8]:
            print("Opcion no valida")

main()