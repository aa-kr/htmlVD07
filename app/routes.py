from flask import Flask, render_template, request, redirect, url_for
from app import app



@app.route('/', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

       

        # Перенаправляем пользователя на ту же страницу после сохранения
        return redirect(url_for('edit_profile'))

    return render_template('edit_profile.html')


