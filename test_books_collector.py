from main import BooksCollector
import pytest

class TestBooksCollector:
#1.1
    def test_add_new_book_add_two_books(self, collector_instance):
        collector_instance.add_new_book('Гордость и предубеждение и зомби')
        collector_instance.add_new_book('Что делать, если ваш кот хочет вас убить')        
        assert len(collector_instance.get_books_genre()) == 2

#1.2
    @pytest.mark.parametrize(
        "book_name, expected_length",
        [
            ("", 0),
            ("a" * 41, 0),            
            ("b" * 50, 0)
        ]
    )
    def test_add_new_book_invalid_length_not_added(self, collector_instance, book_name, expected_length):        
        collector_instance.add_new_book(book_name)      
        assert len(collector_instance.get_books_genre()) == expected_length
        
    
#2  
    def test_set_book_genre_valid_book_and_genre(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book
        genre_name = 'Детективы'
        collector.set_book_genre(book_name, genre_name) 
        assert collector.get_book_genre(book_name) == genre_name

#3   
    def test_get_book_genre_by_the_name(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book
        genre_name = 'Фантастика'
        collector.set_book_genre(book_name, genre_name) 
        assert collector.get_book_genre(book_name) == genre_name

#4
    def test_get_book_with_specific_genre(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book
        genre_name = 'Детективы'
        collector.set_book_genre(book_name, genre_name)
        result = collector.get_books_with_specific_genre(genre_name)             
        assert result == [book_name]

#5   
    def test_get_list_book_genre(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book
        genre_name = 'Фантастика'
        collector.set_book_genre(book_name, genre_name)
        result = collector.get_books_genre()
        assert result == {book_name: genre_name}

#6
    def test_books_with_age_rating_not_in_children_list(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book
        genre_name = 'Ужасы'
        expected_result = [] 
        collector.set_book_genre(book_name, genre_name)
        children_books_list = collector.get_books_for_children()
        assert children_books_list == expected_result


#7
    def test_add_book_in_favorites_book(self, setup_collector_with_book):
        collector, book_name = setup_collector_with_book    
        collector.add_book_in_favorites(book_name)       
        favorites_list = collector.get_list_of_favorites_books()
        assert len(favorites_list) == 1
        assert favorites_list == [book_name]

#8
    def test_book_is_already_in_favorites(self, setup_collector_with_favorited_book):
        collector, book_name = setup_collector_with_favorited_book
        assert book_name in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

#9
    def test_delete_book_from_favorites(self, setup_collector_with_favorited_book):
        collector, book_name = setup_collector_with_favorited_book     
        collector.delete_book_from_favorites(book_name)       
        favorites_list = collector.get_list_of_favorites_books()
        assert book_name not in favorites_list        

#10
    def test_get_list_of_favorites_books(self, setup_collector_with_three_favorites):
        collector, expected_books_list = setup_collector_with_three_favorites       
        actual_favorites_list = collector.get_list_of_favorites_books()      
        assert len(actual_favorites_list) == 3
        assert actual_favorites_list == expected_books_list
