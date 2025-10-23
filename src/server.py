from aiohttp import web
import json

async def handle(request):
    response_obj = {'status': 'ok'}
    return web.json_response(response_obj)

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app, port=8000)
