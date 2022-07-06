from enum import auto
from time import time
from typing import List, Optional
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, SessionLocal,get_db
from .routers import post, user, auth,vote
from .config import settings

#Since we have Alembic that can handle this for us
#models.Base.metadata.create_all(bind=engine)

print(settings.database_hostname)

pa = FastAPI()

#origins = ["https://www.google.com/", "https://www.youtube.com/"]
origins = ["*"]

pa.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pa.include_router(post.router)
pa.include_router(user.router)
pa.include_router(auth.router)
pa.include_router(vote.router)


@pa.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}

while True:

    try:
        # conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
        #                         password='123456', cursor_factory=RealDictCursor)
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                       password='123456', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)


# @pa.get("/posts")
# def get_all_first():
#     cursor.execute(""" SELECT * FROM post """)
#     pst = cursor.fetchall()
#     #return {"message": pst}
#     return{pst}

# @pa.post("/posts", status_code= status.HTTP_201_CREATED)
# def new_post(pst: schemas.PostCreate):
#     cursor.execute("""INSERT INTO post (title,content, published) VALUES (%s, %s, %s) RETURNING 
#     * """,(pst.title, pst.content, pst.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     #return {"data": new_post}
#     return  new_post

# #To Get one record from postgres
# @pa.get("/posts/{id}", response_model = schemas.ResponsePost)
# def get_post_id(id: str):
#     cursor.execute("""SELECT * FROM post WHERE id = %s """,(str(id),))
#     post_byid = cursor.fetchone()
#     if not post_byid:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#          detail= f"post with this {id} not found")
#     return  post_byid

# #To delete a post
# @pa.delete("/posts/{id}",status_code= status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM post WHERE id = %s RETURNING * """,(str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
    
#     if deleted_post == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#         detail= f"post with {id} does not exist")

#     return Response(status_code= status.HTTP_204_NO_CONTENT)

# #To Update a post
# @pa.put("/posts/{id}", response_model = schemas.ResponsePost)
# def update_post(id: int, post: schemas.PostCreate)   :
#     cursor.execute("""UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s 
#     RETURNING * """,(post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
    
#     if updated_post == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#         detail= f"post with {id} does not  exist")
   
#     #return {"data": updated_post}
#     return updated_post



# #To get all posts 
# @pa.get("/postorm", response_model = List[schemas.ResponsePost])
# def get_postns(db: Session = Depends(get_db)):
    
#     dbposts = db.query(models.Post).all()
#     #return {"data": dbposts}
#     print(dbposts)
#     return  dbposts

# #To Post a record to postgres
# @pa.post("/postorm", status_code=status.HTTP_201_CREATED, response_model = schemas.ResponsePost)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

#     #If You dont want to type the model out like this   
#     #new_post = models.Post(title = post.title, content = post.content, published = post.published )
#     #print(current_user.email)
#     new_post = models.Post(** post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     #return {"data": new_post}
#     return  new_post

# #To Get one record from postgres
# @pa.get("/postorm/{id}", response_model = schemas.ResponsePost)
# def get_post_id(id: int, db: Session = Depends(get_db)):
    
#     post_byid = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post_byid:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#          detail= f"post with this {id} not found")
#     return post_byid

# #To delete a post
# @pa.delete("/postorm/{id}",status_code= status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
    
#     deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    
#     if deleted_post.first() == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#         detail= f"post with {id} does not exist")
    
#     deleted_post.delete(synchronize_session = False)
#     db.commit()

#     return Response(status_code= status.HTTP_204_NO_CONTENT)


# #To Update a post
# @pa.put("/postorm/{id}", response_model = schemas.ResponsePost)
# def update_post(id: int, post: schemas.PostCreate,db: Session = Depends(get_db))   :
    
#     query_post = db.query(models.Post).filter(models.Post.id == id)
#     updated_post = query_post.first()
#     if updated_post == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#         detail= f"post with {id} does not  exist")
    
#     #query_post.update({'title': post.title, 'content': post.content}, synchronize_session=False)
#     query_post.update(post.dict(), synchronize_session=False)
#     db.commit()
#     #return {"data": query_post.first()}
#     return  query_post.first()


# @pa.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @pa.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db), ):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id: {id} does not exist")

#     return user