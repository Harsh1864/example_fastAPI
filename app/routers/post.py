from fastapi import FastAPI, HTTPException, Response,status,Depends,APIRouter
from sqlalchemy import desc, func
from .. import models,schema,utils,oauth2
from ..database import get_db,engine
from sqlalchemy.orm import Session,declarative_base 
from typing import List, Optional


router = APIRouter(
    prefix="/posts"
)


#fetch all post
# @router.get("/",response_model=List[schema.Post])
@router.get("/",response_model=List[schema.Postout])
async def get_post(db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user),limit : int = 10,skip : int = 0,search : Optional[str] = ""):
    # cursor.execute("""select * from posts""")
    # posts  = cursor.fetchall()
    # print(posts)
    print(limit)
    post_query = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    results = db.query(models.Post, func.count(models. Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(post_query)
    return results
    # print(search)
    # post = post_query.all()

    if not post_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} was not found")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,details=f"Not authorised to perform requested action")
    return post_query

#insert the data
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_post(post : schema.postcreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,contant,published) VALUES (%s,%s,%s) RETURNING *""",
    #                (Post.title,Post.contant,Post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(current_user.email)
    # new_post = models.Post(title=post.title,contant=post.contant,published=post.published)
    print(current_user.id)
    print(current_user.email)
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#FOR LATEST post
@router.get("/latest") 
def get_latest_post(db: Session = Depends(get_db)):
    post1 = db.query(models.Post).order_by(desc(models.Post.created_at)).limit(1).first()
    return {"details":post1}

#FOR FINDIND SPECIFIC ID
# def find_id(id):
#     for p in my_post:
#         if p["id"]==id:
#             return p

@router.get("/{id}",response_model=schema.Postout)
def get_post(id : int,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * from posts WHERE id=%s""",(str(id),))
    # post = cursor.fetchone()
    #change responce
    
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models. Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    
    return post

#find the index
# def find_index(id):
#     for i,p in enumerate(my_post):
#         if p['id']==id:
#             return i

#delete the post
@router.delete("/{id}",response_model=schema.Post)
def delete_post(id : int,db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",(str(id),))
    # delete_post = cursor.fetchone()    
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()


    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,details=f"Not authorised to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK)


#UPDATE a post

def date_post(id):
    pass

@router.put("/{id}",response_model=schema.Post)
def update(id:int,update_post : schema.postupdate,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    # cursor.execute("""UPDATE posts SET title = %s , contant = %s , published = %s WHERE id = %s RETURNING *""",(post.title,post.contant,post.published,(str(id))))
    # update_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id) 
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id : {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            details=f"Not authorised to perform requested action")
    post_query.update(update_post.dict(),synchronize_session=False)
    db.commit() 
    db.refresh(post)
    return post