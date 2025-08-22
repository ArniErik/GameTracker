import json

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

    def get_genre_by_id(self,id):
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
        for genre in self.genres_list:
            genre.show_genre()
        print("Plataforma:", self.__platform)
        print("Completado:","Terminado" if self.__completed else "Pendiente")
        print(f"Calificacion: {self.__rating}" if self.__rating is not None else "Sin Calificar!!")
        print(f"Se completo el: {self.__completed_date}" if self.__completed_date is not None else "Sin terminar!!")
    def show_game_name_and_id(self):
        print("--------")
        print("ID:", self.__id, "Nombre:",self.__name)
    def show_game_with_id_genres(self):
        print(f"-----{self.__name}---------")
        for genre in self.__genres_list:
            print(f"Id: {genre.id}, Nombre: {genre.name}")
class GamesList:
    def __init__(self, path):
        self.__list = []
        self.__path = path
    
    def load_games_list(self):
        try:
            with open(self.__path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Sin archivo por cargar")
            self.__list = []
        except FileNotFoundError:
            print("Errfor:Archivo no encontrado")
            self.__list = []
        else:
            self.__list = []
            for g in data:
                genre_list = []
                for genre_dicc in g["Genres_list"]:
                    genre = genre(genre_dicc["Name"],genre_dicc["Description"])
                    genre.id = genre_dicc["Id"]
                    genre_list.append(genre)
                game = Game(g["Name"],genre_list,g["Platform"],g["Completed"],g["Description"],g["Rating"],g["Completed_Date"])
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
            data.append({
                "Id" : game.id,
                "Name" : game.name,
                "Genres_list" : genre_dicc,
                "Platform" : game.platform,
                "Completed" : game.completed,
                "Description" : game.description,
                "Rating" : game.rating,
                "Completed_Date" : game.completed_date
            })
        with open(self.__path,"w") as file:
            json.dump(data,file, indent=4)

    def add_game(self, game):
        initial_id = game.id
        for g in self.__list:
            if g.id > initial_id:
                initial_id = g.id
        game.id = initial_id
        self.__list.append(game)

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
        elif opc is not [1,2,3,4]:
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
    if id >= 0 :
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
            elif opc is not [1,2,3]:
                print("Opcion no valida")
def delete_genre_process(genre_list:GenreList):
    genre_list.show_genre_list_with_id()
    id = get_number("Selecciona el id del genero a eliminar(-1 para salir):")
    if id >= 0:
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
        elif opc is not [1,2,3,4]:
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
    if id >= 0 :
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
            elif opc is not [1,2,3]:
                print("Opcion no valida")
def delete_platform_process(platform_list:PlatformsList):
    platform_list.show_platform_list_with_id()
    id = get_number("Selecciona el id de la plataforma a eliminar(-1 para salir):")
    if id >= 0:
        platform_list.delete_platform_by_id(id)


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
        elif opc is not [1,2,3]:
            print("Opcion no valida intenta de nuevo")
    
    
def main():
    genre_list = GenreList("Data/Genre.json")
    platform_list = PlatformsList("Data/Platforms.json")
    platform_list.load_platform_list()
    genre_list.load_genre_list()
    end = False
    while not end:
        main_menu()
        opc = get_number("Selecciona una opcion:")
        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            pass
        elif opc == 6:
            extra_menu(genre_list,platform_list)
        elif opc == 7:
            genre_list.save_genre_list()
            platform_list.save_platform_list()
            print("Todos los datos guardados")
        elif opc == 8:
            end = True
        elif opc is not [1,2,3,4,5,6,7,8]:
            print("Opcion no valida")

main()