from main import BooksCollector
import pytest

# 1.1
@pytest.fixture (scope='function')
def collector_instance():
    return BooksCollector()

# 1.2
@pytest.fixture (scope='function')
def setup_collector_with_book(collector_instance): 
    book_name = 'Пять поросят'
    collector_instance.add_new_book(book_name)
    return collector_instance, book_name

# 2   
@pytest.fixture(scope='function')
def setup_collector_with_favorited_book(collector_instance):      
    book_name = 'Война и мир'    
    collector_instance.add_new_book(book_name)
    collector_instance.add_book_in_favorites(book_name)     
    return collector_instance, book_name

# 3
@pytest.fixture(scope='function')
def setup_collector_with_three_favorites(collector_instance): 
    book_names = ['Обломов', 'Зеленая миля', 'Сияние']        
        
    for name in book_names:
        collector_instance.add_new_book(name)
        collector_instance.add_book_in_favorites(name)         
        
    return collector_instance, book_names
