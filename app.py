import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os

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
from classes.person import Person
from classes.sell import Sell

from classes.address_controller import AddressController
from classes.administrator_controller import AdministratorController
from classes.audiobook_controller import AudioBookController
from classes.book_controller import BookController
from classes.client_controller import ClientController
from classes.delivery_controller import DeliveryController
from classes.document_controller import DocumentController

"""

from classes.ebook_controller import EbookController
from classes.edelivery_controller import EDeliveryController
from classes.edoc_controller import EdocController
from classes.fdelivery_controller import FDeliveryController
from classes.fdoc_controller import FdocController
from classes.invbook_controller import InvBookController
from classes.lease_controller import LeaseController
from classes.magazine_controller import MagazineController
from classes.person_controller import PersonController
from classes.sell_controller import SellController
"""

app = FastAPI()
address_object = AddressController()
administrator_object = AdministratorController()
audiobook_object = AudioBookController()
book_object = BookController()
client_object = ClientController()
delivery_object = DeliveryController()
document_object = DocumentController()

"""
ebook_object = EbookController()
edelivery_object = EDeliveryController()
edoc_object = EdocController()
fdelivery_object = FDeliveryController()
fdoc_object = FdocController()
invbook_object = InvBookController()
lease_object = LeaseController()
magazine_object = MagazineController()
person_object = PersonController()
sell_object = SellController()
"""

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"200": "Welcome To Document Management System Restful API"}


@app.get("/api/document")
async def root():
    return document_object.show()


@app.post("/api/document")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str):
    return document_object.add(Document(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                        language=language))


@app.get("/api/address")
async def root():
    return address_object.show()


@app.post("/api/address")
async def add(country: str, department: str, city: str, post_code: str, neighborhood: str, street: str,
              complement: str):
    return address_object.add(Address(country=country, department=department, city=city, post_code=post_code,
                                      neighborhood=neighborhood, street=street, complement=complement))


@app.get("/api/administrator")
async def root():
    return administrator_object.show()


@app.post("/api/administrator")
async def add(id_person: int, name: str, last_name: str, phone: str, mail: str):
    return administrator_object.add(
        Administrator(id_person=id_person, name=name, last_name=last_name, phone=phone, mail=mail))


@app.get("/api/audiobook")
async def root():
    return audiobook_object.show()


@app.post("/api/audiobook")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, pub_date: str, size: float,
              doi: str, hours: int, minutes: int, seconds: int, synopsis: str):
    return audiobook_object.add(AudioBook(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                          language=language, pub_date=pub_date, size=size, doi=doi, hours=hours,
                                          minutes=minutes, seconds=seconds, synopsis=synopsis))


@app.get("/api/book")
async def root():
    return book_object.show()


@app.post("/api/book")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, publisher: str, editor: str,
              pages: int, synopsis: str, presentation: str):
    return book_object.add(Book(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                language=language, publisher=publisher, editor=editor, pages=pages, synopsis=synopsis,
                                presentation=presentation))


@app.get("/api/client")
async def root():
    return client_object.show()


@app.post("/api/client")
async def add(id_person: int, name: str, last_name: str, phone: str, mail: str):
    return client_object.add(Client(id_person=id_person, name=name, last_name=last_name, phone=phone, mail=mail))


@app.get("/api/delivery")
async def root():
    return delivery_object.show()


@app.post("/api/delivery")
async def add(buyer: str, delivery_id: int, date: str):
    return delivery_object.add(Delivery(buyer=buyer, deliver_id=delivery_id, date=date))


if __name__ == "__main__":
    uvicorn.run(app, port=33508)
