from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Настройки почты (обновите своими SMTP настройками для продакшена)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'
mail = Mail(app)

# Примеры данных для сайта
trainers = [
    {
        'id': 1,
        'name': 'Слава Супер',
        'title': 'Главный тренер',
        'bio': 'Начинающий тренер с опытом работы 2 месяца, но с большим энтузиазмом.',
        'image': 'mike.jpg'
    }
]

classes = [
    {
        'id': 1,
        'name': 'Бокс для начинающих',
        'description': 'Изучите основы бокса в дружественной атмосфере.',
        'schedule': 'Пн, Ср, Пт: 18:00 - 19:30',
        'image': 'boxing-class.jpg'
    },
    {
        'id': 2,
        'name': 'Продвинутая техника',
        'description': 'Совершенствуйте свои навыки с продвинутыми комбинациями и техниками защиты.',
        'schedule': 'Вт, Чт: 19:00 - 20:30',
        'image': 'boxing-class.jpg'
    },
    {
        'id': 3,
        'name': 'Тренировочный лагерь',
        'description': 'Высокоинтенсивные тренировки для развития силы, скорости и выносливости.',
        'schedule': 'Пн, Ср, Пт: 8:00 - 9:30',
        'image': 'boxing-class.jpg'
    },
    {
        'id': 4,
        'name': 'Спарринг-сессии',
        'description': 'Контролируемые спарринги для боксеров среднего и продвинутого уровня.',
        'schedule': 'Сб: 10:00 - 12:00',
        'image': 'boxing-class.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', trainers=trainers[:2], classes=classes[:3])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/classes')
def class_list():
    return render_template('classes.html', classes=classes)

@app.route('/trainers')
def trainer_list():
    return render_template('trainers.html', trainers=trainers)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Отправка email (закомментировано для разработки)
        """
        msg = Message(
            subject=f"Боксерский лагерь контакт: {subject}",
            recipients=["gym-email@example.com"],
            body=f"От: {name} <{email}>\n\n{message}"
        )
        mail.send(msg)
        """
        
        flash('Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', classes=classes)

@app.template_filter('current_year')
def current_year(value):
    return datetime.now().year

if __name__ == '__main__':
    app.run(debug=True, port=5000) 