from datetime import date
from fastapi import FastAPI, Depends, Query
from typing import Union, List, Optional
from auth import AuthHandler
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI(
    title="Travel Deals Aggregator Docs",
    description='',
    servers=[{
        "name": "Local",
        "url": "http://127.0.0.1:8000/api",
    }]
)

auth_handler = AuthHandler()

# Authentication
@app.post('/login', tags=["Common"])
def login(
        email:      Union[str, None] = None, 
        password:   Union[str, None] = None
    ):
    return {'success': True}

@app.post('/logout', tags=["Common"])
def logout(
        email = Depends(auth_handler.auth_wrapper)
    ):
    return {'success': True}

@app.post('/register', tags=["Common"])
def signup(
        name:                   Union[str, None] = None,
        password:               Union[str, None] = None,
        password_confirmation:  Union[str, None] = None,
        email:                  Union[str, None] = None,         
    ):
    return {'success': True}

@app.get('/deals', tags=["Common"])
def getProfile(  
        email = Depends(auth_handler.auth_wrapper)
    ):
    return {'success': True}

@app.get('/deals/{id}', tags=["Common"])
def getProfile(  
        id: int,
        email = Depends(auth_handler.auth_wrapper)
    ):
    return {'success': True}

@app.post('/deals/{id}/bookmark', tags=["Common"])
def updateProfile(  
        id: int,
        email = Depends(auth_handler.auth_wrapper)
    ):
    return {'success': True}

@app.get('/user/bookmarks', tags=["Common"])
def getProfile(  
        email = Depends(auth_handler.auth_wrapper)
    ):
    return {'success': True}