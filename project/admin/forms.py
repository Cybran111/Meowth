from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Regexp
from project.admin.logic import get_categories


class VacancyForm(Form):
    title = StringField(
        'Позиция',
        validators=[
            DataRequired('Required Field'),
            Length(
                max=100,
                message='Must not exceed 100 symbols'
            ),
            Regexp(
                '^[\.\d\w\sА-Яа-яІіЇїҐґ\-\+]+$',
                message='Should contain only cyryllic \
                         and latin letters,- ,+, . and \
                         spaces'
            )
        ]
    )
    name_in_url = StringField(
        "URL-имя",
        validators=[
            DataRequired('Required Field'),
            Length(
                max=50,
                message='Must not exceed 50 symbols'
            ),
            Regexp(
                '^[\d\w\-]+$',
                message='Should contain only \
                         latin characters and dashes'
            )
        ]
    )
    short_description = StringField(
        "Краткое описание",
        validators=[
            DataRequired('Required Field'),
            Length(
                max=300,
                message='Must not exceed 300 symbols'
            )
        ]
    )
    text = TextAreaField(
        'Текст вакансии',
        validators=[DataRequired('Required Field')]
    )
    category_id = QuerySelectField(
        'Категория',
        query_factory=get_categories,
        validators=[DataRequired('Required field')]
    )


class CategoryForm(Form):
    name = StringField("Название категории", validators=[DataRequired()])