import aiohttp
from aiohttp import web
from aiohttp.client import request

HOST_IP = "0.0.0.0"
PORT_IP = "1336"

async def ChetNechet(request_obj):
    request = await request_obj.json()
    response = {}
    response["version"] = request["version"]
    response["session"] = request["version"]
    response["response"] = {"end_session": False}
    return web.json_response(response)

def init():
    app = web.Application()
    web.run_app(app, host = HOST_IP, port = PORT_IP)
    app.router.add_post("/ChetNechet", ChetNechet())

    if __name__ == "__main__":
        init()


        
        
