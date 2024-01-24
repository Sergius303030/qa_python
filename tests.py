import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_books_again(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    @pytest.mark.parametrize('book', ['Другая легенда о Тиле Уленшпигеле и Ламме', ''])
    def test_add_new_book_name_too_long(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_assign_book(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == genre

    def test_set_book_genre_not_assign_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Приключения')
        assert len(collector.get_books_genre()['Гордость и предубеждение и зомби']) == 0

    def test_get_books_with_specific_genre_book_list(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_new_book('Приключение Электроника')
        collector.add_new_book('Индиана Джонс')
        collector.add_new_book('Тиг и Лео')
        collector.set_book_genre('Звездные войны','Фантастика')
        collector.set_book_genre('Приключение Электроника', 'Фантастика')
        collector.set_book_genre('Приключение Электроника', 'Приключения')
        collector.set_book_genre('Тиг и Лео', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Звездные войны','Приключение Электроника']

    def test_get_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_new_book('Тиг и Лео')
        collector.set_book_genre('Звездные войны','Фантастика')
        collector.set_book_genre('Тиг и Лео', 'Мультфильмы')
        assert collector.get_books_genre() == {'Звездные войны':'Фантастика','Тиг и Лео':'Мультфильмы'}

    def test_get_books_genre_not_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        assert collector.get_books_genre() == {'Звездные войны': ''}

    def test_get_books_for_children_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Тиг и Лео')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Тиг и Лео', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Тиг и Лео']

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_new_book('Приключение Электроника')
        collector.add_book_in_favorites('Звездные войны')
        collector.add_book_in_favorites('Приключение Электроника')
        assert collector.get_list_of_favorites_books() == ['Звездные войны', 'Приключение Электроника']

    def test_delete_book_from_favorites_delete_one_books(self):
        collector = BooksCollector()
        collector.add_new_book('Звездные войны')
        collector.add_new_book('Приключение Электроника')
        collector.add_book_in_favorites('Звездные войны')
        collector.add_book_in_favorites('Приключение Электроника')
        collector.delete_book_from_favorites('Звездные войны')
        assert collector.get_list_of_favorites_books() == ['Приключение Электроника']
