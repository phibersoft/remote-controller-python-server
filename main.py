import lib.error_handler

import eventlet
import socketio

from lib.events.action_keypress import action_keypress
from lib.events.lol import lol
from lib.utils import logger

import lib.wifi_handler

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, _environ, _auth):
    logger(f'User connected: {sid}')


@sio.event
def disconnect(sid):
    logger(f'User disconnected: {sid}', 'warning')


@sio.on('action_keypress')
def act_action_keypress(_, key, modifs):
    action_keypress(key, modifs)


@sio.on('lol')
def act_lol(_, action, hero):
    lol(action, hero)


if __name__ == '__main__':
    # Start the server
    eventlet.wsgi.server(eventlet.listen(('', 9292)), app, log_output=False)
