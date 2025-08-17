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
                break
        print("Se elimino el genero de Id:",id)

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
        self.show_genre()
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



class Game:
    def __init__(self, name, genre, platform, completed, description = "", rating = None, completed_date = None):
        self.__id = None
        self.__name = name
        self.__description = description
        self.__genre = genre
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
    def genre(self):
        return self.__genre
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
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
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

    def show_game(self):
        print("******", self.__name,"******")
        print("Description:",self.__description)
        print("Genero:", self.__genre)
        print("Plataforma:", self.__platform)
        print("Completado:","Terminado" if self.__completed else "Pendiente")
        print(f"Calificacion: {self.__rating}" if self.__rating is not None else "Sin Calificar!!")
        print(f"Se completo el: {self.__completed_date}" if self.__completed_date is not None else "Sin terminar!!")
    def show_game_name_and_id(self):
        print("--------")
        print("ID:", self.__id, "Nombre:",self.__name)
class GamesList:
    def __init__(self, path):
        self.__list = []
        self.__path = path
    
    def load_games_list(self):
        try:
            with open(self.__path, "r") as file:
                data = json.load(file)
                self.__list = []
                for g in data:
                    game = Game(g["Name"],g["Genre"],g["Platform"],g["Completed"],g["Description"],g["Rating"],g["Completed_Date"])
                    game.id = g["Id"]
                    self.__list.append(game)
        except FileNotFoundError:
            print("Errfor:Archivo no encontrado")

    def save_games_list(self):
        data = []
        for game in self.__list:
            data.append({
                "Id" : game.id,
                "Name" : game.name,
                "Genre" : game.genre,
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
            pass
        elif opc == 3:
            pass
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