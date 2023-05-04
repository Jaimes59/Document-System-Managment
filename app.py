import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os

from pydantic import BaseModel, validator
from enum import Enum
from typing import Optional
from fastapi import Query
from fastapi.openapi.models import Schema
from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from fastapi import Request
from fastapi.templating import Jinja2Templates

from logic.classes.address import Address
from logic.classes.administrator import Administrator
from logic.classes.audiobook import AudioBook
from logic.classes.book import Book
from logic.classes.client import Client
from logic.classes.delivery import Delivery
from logic.classes.dms import DMS
from logic.classes.document import Document
from logic.classes.ebook import Ebook
from logic.classes.edelivery import EDelivery
from logic.classes.edoc import Edoc
from logic.classes.fdelivery import FDelivery
from logic.classes.fdoc import Fdoc
from logic.classes.invbook import InvBook
from logic.classes.lease import Lease
from logic.classes.magazine import Magazine
from logic.classes.person import Person
from logic.classes.sell import Sell

from logic.controllers.address_controller import AddressController
from logic.controllers.administrator_controller import AdministratorController
from logic.controllers.audiobook_controller import AudioBookController
from logic.controllers.book_controller import BookController
from logic.controllers.client_controller import ClientController
from logic.controllers.delivery_controller import DeliveryController
from logic.controllers.document_controller import DocumentController
from logic.controllers.ebook_controller import EBookController
from logic.controllers.edelivery_controller import EdeliveryController
from logic.controllers.edoc_controller import EdocController
from logic.controllers.fdelivery_controller import FdeliveryController
from logic.controllers.fdoc_controller import FdocController
from logic.controllers.invbook_controller import InvbookController
from logic.controllers.lease_controller import LeaseController
from logic.controllers.magazine_controller import MagazineController
from logic.controllers.person_controller import PersonController
from logic.controllers.sell_controller import SellController

app = FastAPI()
address_object = AddressController()
administrator_object = AdministratorController()
audiobook_object = AudioBookController()
book_object = BookController()
client_object = ClientController()
delivery_object = DeliveryController()
document_object = DocumentController()
ebook_object = EBookController()
edelivery_object = EdeliveryController()
edoc_object = EdocController()
fdelivery_object = FdeliveryController()
fdoc_object = FdocController()
invbook_object = InvbookController()
lease_object = LeaseController()
magazine_object = MagazineController()
person_object = PersonController()
sell_object = SellController()

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
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, publisher: str,
              editor: str,
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


@app.get("/api/document")
async def root():
    return document_object.show()


@app.post("/api/document")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str):
    return document_object.add(Document(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                        language=language))


@app.get("/api/ebook")
async def root():
    return ebook_object.show()


@app.post("/api/ebook")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, pub_date: str,
              size: float, doi: str, editor: str, pages: int, synopsis: str):
    return ebook_object.add(Ebook(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                  language=language, pub_date=pub_date, size=size, doi=doi, editor=editor,
                                  pages=pages, synopsis=synopsis))


@app.get("/api/edelivery")
async def root():
    return edelivery_object.show()


@app.post("/api/edelivery")
async def add(buyer: str, delivery_id: int, date: str, deliver_mail: str):
    return edelivery_object.add(EDelivery(buyer=buyer, deliver_id=delivery_id, date=date, deliver_mail=deliver_mail))


@app.get("/api/edoc")
async def root():
    return edoc_object.show()


@app.post("/api/edoc")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, pub_date: str,
              size: float, doi: str):
    return edoc_object.add(Edoc(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                language=language, pub_date=pub_date, size=size, doi=doi))


@app.get("/api/fdelivery")
async def root():
    return fdelivery_object.show()


@app.post("/api/fdelivery")
async def add(buyer: str, delivery_id: int, date: str, address: str, contact: str, company: str):
    return fdelivery_object.add(FDelivery(buyer=buyer, deliver_id=delivery_id, date=date, address=address,
                                          contact=contact, company=company))


@app.get("/api/fdoc")
async def root():
    return fdoc_object.show()


@app.post("/api/fdoc")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, publisher: str):
    return fdoc_object.add(Fdoc(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                language=language, publisher=publisher))


@app.get("/api/invbook")
async def root():
    return invbook_object.show()


@app.post("/api/invbook")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, pages: int, abstract: str):
    return invbook_object.add(InvBook(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                      language=language, pages=pages, abstract=abstract))


@app.get("/api/lease")
async def root():
    return lease_object.show()


@app.post("/api/lease")
async def add(lease_id: int, start_date: str, finish_date: str, pay_method: str, total_price: float, items: list):
    return lease_object.add(Lease(lease_id=lease_id, start_date=start_date, finish_date=finish_date,
                                  pay_method=pay_method, total_price=total_price, items=items))


@app.get("/api/magazine")
async def root():
    return magazine_object.show()


@app.post("/api/magazine")
async def add(id_doc: int, author: str, title: str, price: float, topic: str, language: str, pub_date: str,
              size: float, doi: str, edition: int, pages: int):
    return magazine_object.add(Magazine(id_doc=id_doc, author=author, title=title, price=price, topic=topic,
                                        language=language, pub_date=pub_date, size=size, doi=doi, edition=edition,
                                        pages=pages))


@app.get("/api/person")
async def root():
    return person_object.show()


@app.post("/api/person")
async def add(id_person: int, name: str, last_name: str, phone: str, mail: str):
    return person_object.add(Person(id_person=id_person, name=name, last_name=last_name, phone=phone, mail=mail))


@app.get("/api/sell")
async def root():
    return sell_object.show()


@app.post("/api/sell")
async def add(sell_id: int, date: str, pay_method: str, total_price: float, items: list):
    return sell_object.add(
        Sell(sell_id=sell_id, date=date, pay_method=pay_method, total_price=total_price, items=items))




if __name__ == "__main__":
    uvicorn.run(app, port=33508)
