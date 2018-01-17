# NewYearBot
BSUIR, 550502
***

# **Требования к проекту**
## **1 Введение**
Название программы – NewYearBot. 
Данный продукт представляет собой телеграмм бота предназначенного для упрощения некоторых новогодних задач.
Бот позволяет произвести ритуал "Тайный Санта" в удаленном виде.
## **2 Требования пользователя**
### **2.1 Программные интерфейсы**
Приложение написано на языке Python.
Графический интерфейс предоставляет само приложение Telegram.
Управление ботом происходит с помощью следующих команд:
1. /creategroup- Создание группы
2. /join- Присоединение к группе
3. /get- Получение человека из группы
4. /getAll- Получение списка всех групп

### **2.2 Интерфейс пользователя**
Данное приложение не имеет графического собственного графического интерфейса интерфейса так как в нем нет необходимости.
### **2.3 Характеристики пользователей**
Целевая аудитория приложения - люди любого возраста.

## **3 Системные требования**
Для использования приложения необходим любой персональный компьютер либо мобильное устройство с выходом в интернет и установленным Telegram клиентом. 

### **3.1 Функциональные требования**
1. Пользователь может создать группу защищенную паролем.
2. Пользователь может вступить в группу.
3. Пользователь может узнать человека которому он должен дарить подарок.
4. Пользователь может просмотреть список всех существующих групп

### **3.2 Нефункциональные требования**
###### **3.2.1 АТРИБУТЫ КАЧЕСТВА**
1. Приложение на сервере занимает не более 100мб. Для тестирования данного требования необходимо нажать по исполняемому файлу правой кнопкой мыши,выбрать вкладку свойства,напротив поля "Размер:" отобразиться размер файла.
2. Приложение должно работать без остановок в течении недели перед новым годом. Для проверки данного требования необходимо запустить бота и в течении недели проверять его реакции на команды 

