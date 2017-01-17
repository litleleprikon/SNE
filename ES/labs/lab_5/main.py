#!/usr/bin/env python3

from bottle import run, get, post, abort, request
import sys

USERS = {
    'litleleprikon': {
        'name': 'litleleprikon',
        'surname': 'litleleprikon',
        'posts': [
            {
                'title': 'First post',
                'article': 'My first post on this blog'
            },
            {
                'title': 'First post',
                'article': 'My first post on this blog'
            }
        ]
    },
    'e.sharifullin': {
        'name': 'Emil',
        'surname': 'Sharifullin',
        'posts': [
            {
                'title': 'First post',
                'article': 'My first post on this blog'
            },
            {
                'title': 'First post',
                'article': 'My first post on this blog'
            }
        ]
    }
}

def search_user(func):
    def wrapper(name):
        if name in USERS:
            return func(name)
        else:
            abort(404, "Sorry, Page not found.")
    return wrapper


@get('/')
def hello():
    return {
        'api usage': {
            'GET /': 'this page',
            'GET /users': 'list of users',
            'GET /users/[name]': 'info about user',
            'GET /users/[name]/posts': 'users posts',
            'POST /users/[name]/posts': 'create post for user'
        }
    }

@get('/users')
def users():
    return {'users': list(USERS.keys())}

@get('/users/<name>')
@search_user
def user(name):
    return USERS[name]


@get('/users/<name>/posts')
@search_user
def user_posts(name):
    return {
            'user': name,
            'posts': USERS[name]['posts']
        }


@post('/users/<name>/posts')
@search_user
def user_posts(name):
    if request.json is None:
        abort(400, "Data must be in JSON")
    USERS[name]['posts'].append({
            'title': request.json.get('title'),
            'article': request.json.get('article')
        })
    return {'status': 'Ok'}


def main():
    host = 'localhost'
    port = 8080
    if len(sys.argv) > 3:
        print('Bad number of arguments\nZero or one required')
    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) == 3:
        port = sys.argv[2]
    run(host='localhost', port=port, debug=True)

if __name__ == '__main__':
    main()
