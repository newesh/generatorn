
import random
import string
from datetime import date, timedelta
import os

# Английские имена и фамилии для генерации почты (расширены)
first_names_m_en = ["alexander", "dmitry", "ivan", "sergey", "andrey", "evgeny", "vladimir", "pavel", "artyom", "maxim", "nikita", "kirill", "roman", "denis", "anton", "victor", "oleg", "igor", "stanislav", "ruslan",
                    "ahmed", "magomed", "islam", "ramzan", "kazbek", "timur", "rustam", "aslan", "zaur", "murad", "arthur", "david", "georgy", "eduard", "robert", "adam", "ali", "bek", "emir", "gasan", "ibragim", "kamil", "mansur", "said", "shamil", "suleiman", "umar", "yusuf", "zagir", "tamerlan",
                    "boris", "vadim", "gleb", "egor", "konstantin", "leonid", "mark", "nazar", "petr", "rostislav", "svyatoslav", "taras", "filipp", "yaroslav", "akim", "bulat", "chingiz", "ernest", "felix", "ilya", "khasan", "marat", "nurlan", "oskar", "radik", "rinat", "salavat", "temirlan", "vladislav", "vyacheslav"] # Added more English transliterations of names
last_names_m_en = ["ivanov", "petrov", "sidorov", "smirnov", "kuznetsov", "popov", "vasilyev", "mikhailov", "fedorov", "sokolov", "morozov", "volkov", "alekseyev", "lebedev", "semyonov", "yershov", "pavlov", "kozlov", "andreyev", "nikolayev",
                   "magomedov", "aliev", "ibragimov", "gadzhiev", "akhmedov", "kadyrov", "basaev", "dadaev", "musaev", "khalidov", "abdullaev", "osmanov", "guseynov", "dzhabrailov", "isaev", "abakarov", "agaev", "amirov", "bayramov", "dzhanaliev", "kerimov", "nabiev", "rustamov", "saitov", "tagirov", "umarov", "yakubov", "zeynalov", "dzucev", "gagloev", "bagaev", "kochiev", "tedeev",
                   "andreev", "bondarenko", "grigoryev", "demidov", "yeremenko", "zhukov", "zaytsev", "kovalyov", "lukyanov", "makarov", "naumov", "orekhov", "panov", "romanov", "savelyev", "timofeev", "ustinov", "fomichev", "kharitonov", "tsaryov", "shestakov", "yakovlev"] # Added more English transliterations of surnames
first_names_f_en = ["elena", "olga", "natalia", "tatyana", "anastasia", "ekaterina", "yulia", "svetlana", "anna", "maria", "victoria", "polina", "ksenia", "alina", "sofia", "daria", "elizaveta", "valeria", "vera", "nadezhda",
                    "fatima", "saida", "amina", "zarema", "leyla", "madina", "khadija", "dzhamilya", "aisha", "karina", "diana", "elvira", "snezhana", "regina", "anzhela", "adina", "aliya", "gulnara", "kamila", "mariam", "sabina", "samira", "sara", "zalina", "zara", "adel", "zhasmin", "rayana",
                    "alla", "angelina", "antonina", "valentina", "vasilisa", "galina", "darya", "evangelina", "zhanna", "zoya", "irina", "klavdiya", "lyudmila", "margarita", "oksana", "raimova", "stellla", "tamara", "uliana", "faina", "elina", "yanina", "zlata", "kira", "mila"] # Added more English transliterations of names
last_names_f_en = ["ivanova", "petrova", "sidorova", "smirnova", "kuznetsova", "popova", "vasilyeva", "mikhailova", "fedorova", "sokolova", "morozova", "volkova", "alekseyeva", "lebedeva", "semyonova", "yershova", "pavlova", "kozlova", "andreyeva", "nikolayeva",
                   "magomedova", "alieva", "ibragimova", "gadzhieva", "akhmedova", "kadyrova", "basaeva", "dadaeva", "musaeva", "khalidova", "abdullaeva", "osmanova", "guseynova", "dzhabrailova", "isaeva", "abakarova", "agaeva", "amirova", "bayramova", "dzhanalieva", "kerimova", "nabieva", "rustamova", "saitova", "tagirova", "umarova", "yakubova", "zeynalova", "dzuceva", "gagloeva", "bagaeva", "kochieval", "tedeeva",
                   "andreeva", "bondarenko", "grigoryeva", "demidova", "yeremenko", "zhukova", "zaytseva", "kovalyova", "lukyanova", "makarova", "naumova", "orekhova", "panova", "romanova", "savelyeva", "timofeeva", "ustinova", "fomicheva", "kharitonova", "tsaryova", "shestakova", "yakovleva"] # Added more English transliterations of surnames


def generate_random_card():
    """Generates a random card number (MIR, OZON, or TINKOFF)."""
    card_type = random.choice(["MIR", "OZON", "TINKOFF"])
    if card_type == "MIR":
        # МИР карты обычно начинаются с 220
        return "220" + "".join(random.choices(string.digits, k=13)) # 16 цифр в сумме
    elif card_type == "OZON":
        # OZON карты начинаются с 2204
        return "2204" + "".join(random.choices(string.digits, k=12)) # 16 цифр в сумме
    elif card_type == "TINKOFF":
        # TINKOFF карты начинаются с 5536
        return "5536" + "".join(random.choices(string.digits, k=12)) # 16 цифр в сумме

def generate_random_fio():
    """Generates a random Russian full name (Last Name, First Name, Middle Name) including more Caucasian names."""
    first_names_m = ["Александр", "Дмитрий", "Иван", "Сергей", "Андрей", "Евгений", "Владимир", "Павел", "Артём", "Максим", "Никита", "Кирилл", "Роман", "Денис", "Антон", "Виктор", "Олег", "Игорь", "Станислав", "Руслан",
                     "Ахмед", "Магомед", "Ислам", "Рамзан", "Казбек", "Тимур", "Рустам", "Аслан", "Заур", "Мурад", "Артур", "Давид", "Георгий", "Эдуард", "Роберт", "Адам", "Али", "Бек", "Эмир", "Гасан", "Ибрагим", "Камиль", "Мансур", "Саид", "Шамиль", "Сулейман", "Умар", "Юсуф", "Загир", "Тамерлан",
                     "Борис", "Вадим", "Глеб", "Егор", "Константин", "Леонид", "Марк", "Назар", "Пётр", "Ростислав", "Святослав", "Тарас", "Филипп", "Ярослав", "Аким", "Булат", "Чингиз", "Эрнест", "Феликс", "Илья", "Хасан", "Марат", "Нурлан", "Оскар", "Радик", "Ринат", "Салават", "Темирлан", "Владислав", "Вячеслав"] # Added more names
    last_names_m = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", "Васильев", "Михайлов", "Фёдоров", "Соколов", "Морозов", "Волков", "Алексеев", "Лебедев", "Семёнов", "Ершов", "Павлов", "Козлов", "Андреев", "Николаев",
                    "Магомедов", "Алиев", "Ибрагимов", "Гаджиев", "Ахмедов", "Кадыров", "Басаев", "Дадаев", "Мусаев", "Халидов", "Абдуллаев", "Османов", "Гусейнов", "Джабраилов", "Исаев", "Абакаров", "Агаев", "Амиров", "Байрамов", "Джаналиев", "Керимов", "Набиев", "Рустамов", "Саитов", "Тагиров", "Умаров", "Якубов", "Зейналов", "Дзуцев", "Гаглоев", "Багаев", "Кочиев", "Тедеев",
                    "Андреев", "Бондаренко", "Григорьев", "Демидов", "Ерёменко", "Жуков", "Зайцев", "Ковалёв", "Лукьянов", "Макаров", "Наумов", "Орехов", "Панов", "Романов", "Савельев", "Тимофеев", "Устинов", "Фомичёв", "Харитонов", "Царёв", "Шестаков", "Яковлев"] # Added more surnames
    middle_names_m = ["Александрович", "Дмитриевич", "Иванович", "Сергеевич", "Андреевич", "Евгеньевич", "Владимирович", "Павлович", "Артёмович", "Максимович", "Никитич", "Кириллович", "Романович", "Денисович", "Антонович", "Викторович", "Олегович", "Игоревич", "Станиславович", "Русланович",
                      "Ахмедович", "Магомедович", "Исламович", "Рамзанович", "Казбекович", "Тимурович", "Рустамович", "Асланович", "Заурович", "Мурадович", "Артурович", "Давидович", "Георгиевич", "Эдуардович", "Робертович", "Адамович", "Алиевич", "Бекович", "Эмирович", "Гасанович", "Ибрагимович", "Камильевич", "Мансурович", "Саидович", "Шамилевич", "Сулейманович", "Умарович", "Юсуфович", "Загирович", "Тамерланович",
                      "Борисович", "Вадимович", "Глебович", "Егорович", "Константинович", "Леонидович", "Маркович", "Назарович", "Петрович", "Ростиславович", "Святославович", "Тарасович", "Филиппович", "Ярославович", "Акимович", "Булатович", "Чингизович", "Эрнестович", "Феликсович", "Ильич", "Хасанович", "Маратович", "Нурланович", "Оскарович", "Радикович", "Ринатович", "Салаватович", "Темирланович", "Владиславович", "Вячеславович"] # Added more patronymics
    first_names_f = ["Елена", "Ольга", "Наталья", "Татьяна", "Анастасия", "Екатерина", "Юлия", "Светлана", "Анна", "Мария", "Виктория", "Полина", "Ксения", "Алина", "София", "Дарья", "Елизавета", "Валерия", "Вера", "Надежда",
                     "Фатима", "Саида", "Амина", "Зарема", "Лейла", "Мадина", "Хадижа", "Джамиля", "Аиша", "Карина", "Диана", "Эльвира", "Снежана", "Регина", "Анжела", "Адина", "Алия", "Гульнара", "Камила", "Мариам", "Сабина", "Самира", "Сара", "Залина", "Зара", "Адель", "Жасмин", "Раяна",
                     "Алла", "Ангелина", "Антонина", "Валентина", "Василиса", "Галина", "Дарья", "Евангелина", "Жанна", "Зоя", "Ирина", "Клавдия", "Людмила", "Маргарита", "Оксана", "Раима", "Стелла", "Тамара", "Ульяна", "Фаина", "Элина", "Янина", "Злата", "Кира", "Мила"] # Added more names
    last_names_f = ["Иванова", "Петрова", "Сидорова", "Смирнова", "Кузнецова", "Попова", "Васильева", "Михайлова", "Фёдорова", "Соколова", "Морозова", "Волкова", "Алексеева", "Лебедева", "Семёнова", "Ершова", "Павлова", "Козлова", "Андреева", "Николаева",
                    "Магомедова", "Алиева", "Ибрагимова", "Гаджиева", "Ахмедова", "Кадырова", "Басаева", "Дадаева", "Мусаева", "Халидова", "Абдуллаева", "Османова", "Гусейнова", "Джабраилова", "Исаева", "Абакарова", "Агаева", "Амирова", "Байрамова", "Джаналиева", "Керимова", "Набиева", "Рустамова", "Саитова", "Тагирова", "Умарова", "Якубова", "Зейналова", "Дзуцева", "Гаглоева", "Багаева", "Кочиева", "Тедеева",
                    "Андреева", "Бондаренко", "Григорьева", "Демидова", "Ерёменко", "Жукова", "Зайцева", "Ковалёва", "Лукьянова", "Макарова", "Наумова", "Орехова", "Панова", "Романова", "Савельева", "Тимофеева", "Устинова", "Фомичёва", "Харитонова", "Царёва", "Шестакова", "Яковлева"] # Added more surnames
    middle_names_f = ["Александровна", "Дмитриевна", "Ивановна", "Сергеевна", "Андреевна", "Евгеньевна", "Владимировна", "Павловна", "Артёмовна", "Максимовна", "Никитична", "Кирилловна", "Романовна", "Денисовна", "Антоновна", "Викторовна", "Олеговна", "Игоревна", "Станиславовна", "Руслановна",
                      "Ахмедовна", "Магомедовна", "Исламовна", "Рамзановна", "Казбековна", "Тимуровна", "Рустамовна", "Аслановна", "Зауровна", "Мурадовна", "Артуровна", "Давидовна", "Георгиевна", "Эдуардовна", "Робертовна", "Адамовна", "Алиевна", "Бековна", "Эмировна", "Гасановна", "Ибрагимовна", "Камильевна", "Мансуровна", "Саидовна", "Шамильевна", "Сулеймановна", "Умаровна", "Юсуфовна", "Загировна", "Тамерлановна",
                      "Борисовна", "Вадимовна", "Глебовна", "Егоровна", "Константиновна", "Леонидовна", "Марковна", "Назаровна", "Петровна", "Ростиславовна", "Святославовна", "Тарасовна", "Филипповна", "Ярославовна", "Акимовна", "Булатовна", "Чингизовна", "Эрнестовна", "Феликсовна", "Ильинична", "Хасановна", "Маратовна", "Нурлановна", "Оскаровна", "Радиковна", "Ринатовна", "Салаватовна", "Темирлановна", "Владиславовна", "Вячеславовна"] # Added more patronymics

    gender = random.choice(["male", "female"])
    if gender == "male":
        return f"{random.choice(last_names_m)} {random.choice(first_names_m)} {random.choice(middle_names_m)}"
    else:
        return f"{random.choice(last_names_f)} {random.choice(first_names_f)} {random.choice(middle_names_f)}"

def generate_random_date():
    """Generates a random date of birth between 1940 and 2012."""
    start_date = date(1940, 1, 1)
    end_date = date(2012, 12, 31) # Extended end date
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date # Return date object to easily get the year

def generate_random_email(birth_year):
    """Generates a random email address, potentially including the birth year."""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com", "outlook.com", "icloud.com", "yandex.com", "mail.com", "gmx.com", "protonmail.com", "zoho.com", "bk.ru", "list.ru", "inbox.ru", "internet.ru"] # Added Russian domains
    name_parts = []

    # Add first and last names (English transliterations)
    if random.random() < 0.8: # Increased chance of including name parts
        name_parts.append(random.choice(first_names_m_en + first_names_f_en))
    if random.random() < 0.8: # Increased chance
        name_parts.append(random.choice(last_names_m_en + last_names_f_en))

    # Add birth year or random number
    if random.random() < 0.8: # Increased chance of including birth year
         name_parts.append(str(birth_year))
    elif random.random() < 0.5: # Increased chance of adding a smaller random number
        name_parts.append(str(random.randint(10, 999)))
    elif random.random() < 0.2: # Sometimes add just a short random string
         name_parts.append("".join(random.choices(string.ascii_lowercase, k=random.randint(2, 5))))


    # Ensure there's at least one part for the local part
    if not name_parts:
        local_part = "".join(random.choices(string.ascii_lowercase, k=random.randint(8, 12)))
    else:
        # Combine parts with a random separator
        separators = ["", ".", "_", "-"]
        local_part = random.choice(separators).join(part for part in name_parts if part)
        # Clean up potential multiple separators or leading/trailing separators
        for sep in separators:
            local_part = local_part.replace(sep*2, sep)
        local_part = local_part.strip("._-")


    # Ensure local part is not empty after cleaning
    if not local_part:
         local_part = "".join(random.choices(string.ascii_lowercase, k=random.randint(8, 12)))

    # Ensure local part doesn't start or end with a separator
    while local_part and local_part[0] in "._-":
        local_part = local_part[1:]
    while local_part and local_part[-1] in "._-":
        local_part = local_part[:-1]

    # Ensure local part is not empty after all checks, add random chars if too short
    if not local_part or len(local_part) < 3:
         local_part += "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 6)))

    # Convert to lowercase
    local_part = local_part.lower()


    return f"{local_part}@{random.choice(domains)}"

def generate_random_inn():
    """Generates a random 12-digit INN."""
    return "".join(random.choices(string.digits, k=12))

def generate_random_address():
    """Generates a random Russian address with more variety."""
    cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород", "Челябинск", "Красноярск", "Самара", "Уфа",
              "Пермь", "Воронеж", "Волгоград", "Ростов-на-Дону", "Краснодар", "Саратов", "Тюмень", "Тольятти", "Ижевск", "Барнаул",
              "Сочи", "Махачкала", "Грозный", "Владикавказ", "Нальчик", "Черкесск", "Ставрополь", "Пятигорск", "Анапа", "Геленджик", "Новороссийск", "Астрахань", "Элиста", "Калининград", "Мурманск", "Архангельск", "Владивосток", "Хабаровск", "Иркутск", "Омск", "Томск", "Кемерово", "Новокузнецк", "Краснодар", "Воронеж", "Самара", "Пермь", "Волгоград", "Ростов-на-Дону",
              "Астрахань", "Белгород", "Брянск", "Владимир", "Вологда", "Иваново", "Калуга", "Кострома", "Курск", "Липецк", "Орел", "Рязань", "Смоленск", "Тамбов", "Тверь", "Тула", "Ярославль",
              "Петрозаводск", "Сыктывкар", "Йошкар-Ола", "Саранск", "Владикавказ", "Казань", "Уфа", "Ижевск", "Чебоксары", "Горно-Алтайск", "Улан-Удэ", "Махачкала", "Магас", "Элиста", "Черкесск", "Петрозаводск", "Сыктывкар", "Йошкар-Ола", "Саранск", "Якутск", "Владикавказ", "Казань", "Уфа", "Ижевск", "Чебоксары", "Горно-Алтайск", "Улан-Удэ", "Махачкала", "Магас", "Элиста", "Черкесск", "Грозный", "Нальчик", "Анадырь", "Салехард", "Ханты-Мансийск", "Биробиджан", "Нарьян-Мар", "Севастополь", "Симферополь"] # Added many more cities
    street_types = ["ул.", "пр.", "пер.", "бульвар", "ш.", "пл.", "наб.", "туп.", "проезд", "аллея", "линия", "переулок", "проспект", "шоссе", "площадь", "набережная", "тупик", "проезд", "аллея", "линия", "микрорайон", "квартал", "сквер", "спуск", "съезд", "тупичок"] # Added more street types
    streets = ["Ленина", "Мира", "Гагарина", "Победы", "Молодежная", "Строителей", "Школьный", "Космонавтов", "Энтузиастов", "Революции",
               "Пушкина", "Лермонтова", "Гоголя", "Толстого", "Достоевского", "Чехова", "Горького", "Маяковского", "Есенина", "Блока",
               "Центральная", "Садовая", "Лесная", "Полевая", "Набережная", "Советская", "Заречная", "Цветочная", "Юбилейная", "Весенняя",
               "Кирова", "Маркса", "Энгельса", "Дзержинского", "Калинина", "Фрунзе", "Куйбышева", "Ватутина", "Жукова", "Конева",
               "Гастелло", "Чкалова", "Матросова", "Космодемьянской", "Талалихина", "Покрышкина", "Суворова", "Кутузова", "Невского", "Донского",
               "Первомайская", "Октябрьская", "Комсомольская", "Пионерская", "Пролетарская", "Рабочая", "Колхозная", "Совхозная",
               "Вокзальная", "Заводская", "Фабричная", "Шахтерская", "Нефтяников", "Газовиков", "Энергетиков",
               "Северная", "Южная", "Восточная", "Западная",
               "Красная", "Зеленая", "Синяя", "Желтая", "Белая", "Черная",
               "Мичурина", "Тимирязева", "Вавилова", "Ломоносова", "Менделеева", "Циолковского", "Королева", "Курчатова", "Сахарова",
               "Маяковского", "Бажова", "Шолохова", "Фадеева", "Твардовского", "Симонова", "Высоцкого", "Цоя", "Бродского",
               "Героев Сталинграда", "30 лет Победы", "60 лет Октября", "70 лет Победы", "Победы", "Мира", "Дружбы", "Согласия",
               "Новая", "Старая", "Тихая", "Шумная", "Короткая", "Длинная", "Узкая", "Широкая", "Высокая", "Низкая", "Дальняя", "Ближняя"] # Added many more street names

    street_type = random.choice(street_types)
    street_name = random.choice(streets)

    # Format street based on type (e.g., "ул. Ленина", "пр. Победы")
    if street_type in ["ул.", "пр.", "пер.", "ш.", "пл.", "наб.", "туп.", "проезд", "аллея", "линия"]:
         full_street = f"{street_type} {street_name}"
    else: # For types like "бульвар", "микрорайон"
         full_street = f"{street_type} {street_name}"


    house_number = random.randint(1, 600) # Increased max house number
    building_letter = random.choice(['', 'А', 'Б', 'В', 'Г', 'Д']) if random.random() < 0.4 else '' # Add building letter sometimes
    building_number = random.randint(1, 15) if building_letter else None # Add building number if letter exists

    apartment_number = random.randint(1, 700) if random.random() < 0.9 else None # Apartment number is optional, increased chance and max

    address_parts = [random.choice(cities), full_street, f"д.{house_number}"]

    if building_letter:
        address_parts[-1] += building_letter
    if building_number is not None:
        address_parts[-1] += f" к.{building_number}"

    if apartment_number is not None:
        address_parts.append(f"кв.{apartment_number}")

    return ", ".join(address_parts)


def generate_random_street():
     """Generates a random Russian street name with more variety."""
     street_types = ["ул.", "пр.", "пер.", "бульвар", "ш.", "пл.", "naб.", "туп.", "проезд", "аллея", "линия", "переулок", "проспект", "шоссе", "площадь", "набережная", "тупик", "проезд", "аллея", "линия", "микрорайон", "квартал", "сквер", "спуск", "съезд", "тупичок"] # Added more street types
     streets = ["Ленина", "Мира", "Гагарина", "Победы", "Молодежная", "Строителей", "Школьный", "Космонавтов", "Энтузиастов", "Революции",
                "Пушкина", "Лермонтова", "Гоголя", "Толстого", "Достоевского", "Чехова", "Горького", "Маяковского", "Есенина", "Блока",
                "Центральная", "Садовая", "Лесная", "Полевая", "Набережная", "Советская", "Заречная", "Цветочная", "Юбилейная", "Весенняя",
                "Кирова", "Маркса", "Энгельса", "Дзержинского", "Калинина", "Фрунзе", "Куйбышева", "Ватутина", "Жукова", "Конева",
                "Гастелло", "Чкалова", "Матросова", "Космодемьянской", "Талалихина", "Покрышкина", "Суворова", "Кутузова", "Невского", "Донского",
                "Первомайская", "Октябрьская", "Комсомольская", "Пионерская", "Пролетарская", "Рабочая", "Колхозная", "Совхозная",
                "Вокзальная", "Заводская", "Фабричная", "Шахтерская", "Нефтяников", "Газовиков", "Энергетиков",
                "Северная", "Южная", "Восточная", "Западная",
                "Красная", "Зеленая", "Синяя", "Желтая", "Белая", "Черная",
                "Мичурина", "Тимирязева", "Вавилова", "Ломоносова", "Менделеева", "Циолковского", "Королева", "Курчатова", "Сахарова",
                "Маяковского", "Бажова", "Шолохова", "Фадеева", "Твардовского", "Симонова", "Высоцкого", "Цоя", "Бродского",
                "Героев Сталинграда", "30 лет Победы", "60 лет Октября", "70 лет Победы", "Победы", "Мира", "Дружбы", "Согласия",
                "Новая", "Старая", "Тихая", "Шумная", "Короткая", "Длинная", "Узкая", "Широкая", "Высокая", "Низкая", "Дальняя", "Ближняя"] # Added many more street names

     street_type = random.choice(street_types)
     street_name = random.choice(streets)

     # Format street based on type
     if street_type in ["ул.", "пр.", "пер.", "ш.", "пл.", "наб.", "туп.", "проезд", "аллея", "линия"]:
          return f"{street_type} {street_name}"
     else: # For types like "бульвар", "микрорайон"
          return f"{street_type} {street_name}"


def generate_random_postal_code():
    """Generates a random 6-digit postal code."""
    return "".join(random.choices(string.digits, k=6))

def generate_random_phone_number():
    """Generates a random Russian phone number."""
    operators = ["900", "901", "902", "903", "904", "905", "906", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "936", "937", "938", "939", "950", "951", "952", "953", "958", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "991", "992", "993", "994", "995", "996", "997", "998", "999"]
    return f"+7 ({random.choice(operators)}) {''.join(random.choices(string.digits, k=3))}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.digits, k=2))}"

def generate_random_occupation():
    """Generates a random occupation."""
    # Expanded list of occupations covering various levels
    occupations = [
        # High-skill/Professional
        "Инженер", "Врач", "Учитель", "Программист", "Менеджер проектов", "Экономист", "Юрист", "Дизайнер", "Маркетолог", "Журналист",
        "Аналитик данных", "Финансовый аналитик", "Системный администратор", "Бухгалтер", "Переводчик", "Архитектор", "Фармацевт",
        "Психолог", "Логист", "HR-менеджер", "Веб-разработчик", "Data Scientist", "Специалист по кибербезопасности", "UX/UI дизайнер",
        "Научный сотрудник", "Преподаватель ВУЗа", "Исследователь", "Адвокат", "Нотариус", "Аудитор", "Бизнес-аналитик", "Сетевой инженер",
        "DevOps инженер", "Тестировщик ПО", "Врач-терапевт", "Хирург", "Педиатр", "Стоматолог", "Учитель школы", "Директор школы",
        "Художественный руководитель", "Режиссер", "Сценарист", "Композитор", "Дирижер", "Артист балета", "Театральный актер", "Киноактер",

        # Mid-skill/Service/Trades
        "Фельдшер", "Медицинская сестра", "Воспитатель", "Библиотекарь", "Архивариус", "Культуролог", "Продавец-консультант", "Кассир",
        "Оператор колл-центра", "Администратор", "Секретарь", "Менеджер по продажам", "Менеджер по работе с клиентами", "Заведующий складом",
        "Мастер участка", "Бригадир", "Электрик", "Сантехник", "Механик", "Сварщик", "Токарь", "Фрезеровщик", "Наладчик станков", "Слесарь",
        "Монтажник", "Отделочник", "Маляр", "Штукатур", "Плиточник", "Кровельщик", "Строитель", "Геодезист", "Землеустроитель",
        "Швея", "Портной", "Закройщик", "Парикмахер", "Мастер маникюра", "Косметолог", "Массажист", "Фитнес-тренер", "Тренер",
        "Повар", "Шеф-повар", "Кондитер", "Пекарь", "Бариста", "Бармен", "Официант", "Работник кухни", "Работник шаурмечной", "Повар-шаурмист",
        "Водитель грузовика", "Водитель автобуса", "Таксист", "Курьер", "Экспедитор", "Кладовщик", "Упаковщик", "Сборщик",

        # Low-skill/Manual Labor
        "Грузчик", "Разнорабочий", "Уборщик", "Дворник", "Посудомойщик", "Подсобный рабочий", "Сторож", "Охранник", "Вахтер", "Курьер пеший",
        "Промоутер", "Раздатчик листовок", "Мойщик автомобилей", "Шиномонтажник",

        # Other
        "Студент", "Пенсионер", "Безработный", "Предприниматель", "Самозанятый", "Фрилансер", "Фотограф", "Видеооператор", "Музыкант", "Артист цирка", "Спортсмен", "Тренер спортивный"
    ]
    return random.choice(occupations)

def generate_random_car_plate():
    """Generates a random Russian car plate number."""
    # Valid Cyrillic letters used in Russian plates that look like Latin letters
    plate_letters = "ABCEHKMOPTXУ"
    letters = "".join(random.choices(plate_letters, k=3))
    numbers = "".join(random.choices(string.digits, k=3))
    # Expanded list of Russian regions
    regions = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38",
        "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57",
        "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76",
        "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95",
        "96", "97", "98", "99", "102", "113", "116", "121", "123", "124", "125", "126", "134", "136", "138", "142", "150",
        "152", "154", "156", "159", "161", "163", "164", "169", "173", "174", "177", "178", "186", "188", "190", "196",
        "197", "198", "199", "777", "799", "101", "105", "106", "107", "108", "110", "111", "114", "115", "117", "128", "139", "140", "141", "143", "144", "146", "147", "148", "151", "153", "155", "157", "158", "162", "166", "168", "171", "172", "176", "189", "191", "193", "194", "195",
        "201", "216", "221", "223", "224", "225", "226", "227", "228", "229", "234", "236", "238", "240", "241", "243", "244", "245", "246", "247", "248", "250", "251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "266", "268", "269", "271", "272", "273", "274", "275", "276", "278", "286", "288", "296", "299"
    ] # Added even more regions
    return f"{letters}{numbers}{random.choice(regions)}"


def generate_random_passport():
    """Generates a random Russian passport series and number."""
    series = "".join(random.choices(string.digits, k=4))
    number = "".join(random.choices(string.digits, k=6))
    return f"{series} {number}"

def generate_random_snils():
    """Generates a random 11-digit SNILS."""
    return "".join(random.choices(string.digits, k=11))

def generate_random_data():
    """Generates a dictionary with random personal data."""
    fio = generate_random_fio()
    birth_date_obj = generate_random_date()
    birth_date_str = birth_date_obj.strftime("%d.%m.%Y")
    birth_year = birth_date_obj.year

    occupation = generate_random_occupation()
    # Set occupation to "Безработный" if birth year is between 2007 and 2012 (underage for most jobs)
    if 2007 <= birth_year <= 2012:
        occupation = "Безработный"
    # Set occupation to "Пенсионер" if birth year is before 1960 (roughly retirement age)
    elif birth_year < 1960:
         occupation = random.choice(["Пенсионер", "Пенсионер (бывший " + generate_random_occupation() + ")"]) # Sometimes add former occupation


    record = {
        "Карта": generate_random_card(),
        "ФИО": fio,
        "Дата рождения": birth_date_str,
        "Почта": generate_random_email(birth_year),
        "ИНН": generate_random_inn(),
        "Адрес проживания": generate_random_address(), # Renamed for clarity
        "Почтовый индекс": generate_random_postal_code(),
        "Телефон": generate_random_phone_number(),
        "Род деятельности": occupation, # Use the determined occupation
        "Улица работы": generate_random_street(), # Added work street
        "Номер автомобиля": generate_random_car_plate(),
        "Паспорт": generate_random_passport(),
        "СНИЛС": generate_random_snils()
    }
    return record

def print_newesh_ascii():
    """Prints the specified 'NEWESH' ASCII art."""
    print("\n")
    print(r"                                                       /$$      ")
    print(r"                                                      | $$      ")
    print(r" /$$$$$$$   /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$$| $$$$$$$ ")
    print(r"| $$__  $$ /$$__  $$| $$ | $$ | $$ /$$__  $$ /$$_____/| $$__  $$")
    print(r"| $$  \ $$| $$$$$$$$| $$ | $$ | $$| $$$$$$$$|  $$$$$$ | $$  \ $$")
    print(r"| $$  | $$| $$_____/| $$ | $$ | $$| $$_____/ \____  $$| $$  | $$")
    print(r"| $$  | $$|  $$$$$$$|  $$$$$/$$$$/|  $$$$$$$ /$$$$$$$/| $$  | $$")
    print(r"|__/  |__/ \_______/ \_____/\___/  \_______/|__/  |__/|__/  |__/")
    print(r"                                                                ")
    print("\n")

def print_menu():
    """Prints the main menu options."""
    print("Выберите действие:")
    print("[1] Сгенерировать данные")
    print("[2] Кредиты")
    print("-" * 50) # Separator before prompt

def display_credits():
    """Displays the credits and copyright information."""
    print("\n" + "=" * 50) # Separator before credits
    print("Кредиты:")
    print("Discord | .newesh")
    print("Github  | https://github.com/newesh")
    print("-" * 50) # Separator after credits

    # Add a simple copyright notice in English
    print("© 2024 newesh. All rights reserved.")
    print("Unauthorized copying, distribution, or modification of this code is prohibited.") # Slightly stronger wording
    print("=" * 50 + "\n") # Separator after copyright and spacing


if __name__ == "__main__":
    print_newesh_ascii() # Print the main ASCII art once at the start

    while True:
        print_menu() # Print the menu in each iteration
        choice = input("Введите номер опции: ").strip() # Get user input and remove whitespace

        if choice == '1':
            while True:
                try:
                    num_to_generate = int(input("Введите количество записей для генерации: "))
                    if num_to_generate > 0:
                        break
                    else:
                        print("Пожалуйста, введите положительное число.")
                except ValueError:
                    print("Некорректный ввод. Введите целое число.")

            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            file_path = os.path.join(desktop_path, "generated.txt")

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    for _ in range(num_to_generate):
                        data = generate_random_data()
                        for key, value in data.items():
                            f.write(f"{key}: {value}\n")
                        f.write("-" * 50 + "\n")
                print(f"Данные успешно сгенерированы и сохранены в файле: {file_path}")
            except Exception as e:
                print(f"Произошла ошибка при записи в файл: {e}")

            print("-" * 50) # Separator after data generation
            # The loop continues to show the menu again

        elif choice == '2':
            display_credits()
            # The loop continues to show the menu again

        else:
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
            print("-" * 50) # Separator after invalid input
            # The loop continues to show the menu again