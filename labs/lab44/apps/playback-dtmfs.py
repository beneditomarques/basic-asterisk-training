#!/usr/bin/python3

"""Brief example of using the channel API with a state machine.

This app will answer any channel sent to Stasis(hello), and play "Hello,
world" to the channel. For any DTMF events received, the number is played back
to the channel. Press # to hang up, and * for a special message.
"""

#
# Copyright (c) 2013, Digium, Inc.
# Copyright (c) 2018, Matthias Urlichs
#

import asyncari
from asyncari.state import ToplevelChannelState, DTMFHandler
import anyio
import logging
import asks
import httpx
import os

ast_host = os.getenv("AST_HOST", '192.168.100.153')
ast_port = int(os.getenv("AST_ARI_PORT", 8088))
ast_url = os.getenv("AST_URL", 'http://%s:%d/'%(ast_host,ast_port))
ast_username = os.getenv("AST_USER", 'ari')
ast_password = os.getenv("AST_PASS", 'mypassword')
ast_app = os.getenv("AST_APP", 'hello')
webhook_url = 'https://webhook.site/5302ee20-ef1c-45be-b995-3825e7fab09a'

class State(ToplevelChannelState, DTMFHandler):
    do_hang = False

    async def on_start(self):
        await self.channel.play(media='sound:welcome')

    async def on_dtmf_Star(self, evt):
        async with httpx.AsyncClient() as client_http:
            await client_http.get(f"{webhook_url}?digit={evt.digit}")
        self.do_hang = True
        await self.channel.play(media='sound:vm-goodbye')

    async def on_dtmf_Pound(self, evt):
        async with httpx.AsyncClient() as client_http:
            await client_http.get(f"{webhook_url}?digit={evt.digit}")

        await self.channel.play(media='sound:asterisk-friend')

    async def on_dtmf(self, evt):
        async with httpx.AsyncClient() as client_http:
            await client_http.get(f"{webhook_url}?digit={evt.digit}")
        await self.channel.play(media='sound:digits/%s' % evt.digit)

    async def on_PlaybackFinished(self, evt):
        if self.do_hang:
            try:
                await self.channel.continueInDialplan()
            except asks.errors.BadStatus:
                pass
        
async def on_start(client):
    
    """Callback for StasisStart events.

    On new channels, register the on_dtmf callback, answer the channel and
    play "Hello, world"

    :param channel: Channel DTMF was received from.
    :param event: Event.
    """
    async with client.on_channel_event('StasisStart') as listener:
        async for objs, event in listener:
            channel = objs['channel']
            await channel.answer()
            client.taskgroup.start_soon(State(channel).start_task)

async def main():
    async with asyncari.connect(ast_url, ast_app, ast_username,ast_password) as client:
        client.taskgroup.start_soon(on_start, client)
        # Run the WebSocket
        async for m in client:
            print("** EVENT **", m)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        anyio.run(main, backend="trio")
    except KeyboardInterrupt:
        pass

