from fastapi import FastAPI

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    description: str


app = FastAPI(title='Bamboo Cargo')

posts = {}


@app.get('/posts/')
async def get_posts():
    return {'msg': [post for post in posts.items()]}


@app.post('/post/')
async def create_post(post: Post):
    posts[len(posts)] = post

    return {'msg': 'Пост успешно добавлен'}


@app.get('/post/{post_id}/')
async def get_post(post_id: int):
    if post_id not in posts:
        return {'error': {
            'code': 404,
            'msg': 'Post not found'
        }}

    return posts[post_id]


@app.delete('/posts/{post_id}/')
async def delete_post(post_id: int):
    try:
        del posts[post_id]
        return {'msg': 'Пост успешно удален'}
    except Exception:
        raise {'error': {
            'code': 404,
            'msg': 'Post not found'
        }}

