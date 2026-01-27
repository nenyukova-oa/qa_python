from main import BooksCollector

import pytest
#1f
@pytest.fixture (scope='function')
def setup_collector_with_book():
    collector = BooksCollector()
    book_name = 'Пять поросят'
    collector.add_new_book(book_name)
    return collector, book_name

#2f    
@pytest.fixture(scope='function')
def setup_collector_with_favorited_book():       
    collector = BooksCollector()
    book_name = 'Война и мир'    
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)     
    return collector, book_name

#3f
@pytest.fixture(scope='function')
def setup_collector_with_three_favorites():       
    collector = BooksCollector()
    book_names = ['Обломов', 'Зеленая миля', 'Сияние']        
        
    for name in book_names:
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)         
        
    return collector, book_names

