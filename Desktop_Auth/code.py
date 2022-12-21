# импортируем библиотеку
from tkinter import *
from tkinter import messagebox
# главное окно приложения
window = Tk()

window.title('Авторизация')
# размер окна
window.geometry('450x230')
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


# клавиша'Войти'
def clicked():

    #  имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()

    # выводим данные пользователя
    messagebox.showinfo('Заголовок', '{username}, {password}'
                        .format(username=username, password=password))

# настройки для всех остальных виджетов
main_label = Label(window, text='Авторизация',
                   font=font_header, justify=CENTER, **header_padding)

main_label.pack()

username_label = Label(window, text='Имя пользователя',
                       font=label_font, **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

password_label = Label(window, text='Пароль', font=label_font,
                       **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# кнопка отправки
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

# запускаем окна
window.mainloop()