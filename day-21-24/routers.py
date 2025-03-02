from fastapi import APIRouter

from schemas import Post


router = APIRouter(tags=['Posts'])

posts = {}


@router.get('/posts/')
async def get_posts():
    return {'msg': [post for post in posts.items()]}


@router.post('/post/')
async def create_post(post: Post):
    posts[len(posts)] = post

    return {'msg': 'Пост успешно добавлен'}


@router.get('/post/{post_id}/')
async def get_post(post_id: int):
    if post_id not in posts:
        return {'error': {
            'code': 404,
            'msg': 'Post not found'
        }}

    return posts[post_id]


@router.delete('/posts/{post_id}/')
async def delete_post(post_id: int):
    try:
        del posts[post_id]
        return {'msg': 'Пост успешно удален'}
    except Exception:
        raise {'error': {
            'code': 404,
            'msg': 'Post not found'
        }}

