from classes.address import Address
from classes.administrator import Administrator
from classes.audiobook import AudioBook
from classes.book import Book
from classes.client import Client
from classes.delivery import Delivery
from classes.dms import DMS
from classes.document import Document
from classes.ebook import Ebook
from classes.edelivery import EDelivery
from classes.edoc import Edoc
from classes.fdelivery import FDelivery
from classes.fdoc import Fdoc
from classes.invbook import InvBook
from classes.lease import Lease
from classes.magazine import Magazine
from classes.sell import Sell



# Main function

if __name__ == "__main__":
    # Create a new document
    document1 = Document(id=1, author='Juan Perez',
                         title='La Bella y La Bestia', price=100,
                         topic='Fantasía', language='esp')
    document2 = Document(id=2, author='J.K. Rowling',
                         title='Harry Potter y la Piedra Filosofal',
                         price=150, topic='Fantasía', language='esp')
    document3 = Document(id=3, author='George R.R. Martin',
                         title='Canción de Hielo y Fuego', price=200,
                         topic='Fantasía', language='esp')


    # Create a new client
    client1 = Client(id_person=1, name='Gerardo', last_name='Iglesias',
                     phone='+573127485294', mail='gerardoigelsias@gmail.com')
    client2 = Client(id_person=2, name='Sofia', last_name='Rodriguez',
                     phone='+5712345678', mail='sofiarodriguez@hotmail.com')
    client3 = Client(id_person=3, name='Juan', last_name='Gonzales',
                     phone='+573127437294', mail='juangonzales@gmail.com')

    #Create a new administrator
    administrator1 = Administrator(id_person=1, name='Adrian', last_name='Gonzales',
                                   phone='+573127437294', mail='adriangonzales@gmail.com')
    administrator2 = Administrator(id_person=2, name='Ana', last_name='González',
                                   phone='+573012345678', mail='anagonzalez@gmail.com')
    administrator3 = Administrator(id_person=3, name='Pablo', last_name='Rodriguez',
                                   phone='+5712345678', mail='pablo.rodriguez@hotmail.com')
    administrator4 = Administrator(id_person=4, name='María', last_name='García',
                                   phone='+573012345678', mail='mariagarcia@yahoo.com')

    #Create a new dms
    dms = DMS(catalog=[document1, document2, document3],
              users=[client1, client2, client3],
              administrators=[administrator1, administrator2,
                              administrator3, administrator4])
    # Print the dms
    print("\n", dms)