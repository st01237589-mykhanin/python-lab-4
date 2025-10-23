from molotov import scenario

@scenario(weight=100)
async def test_server(session):
    async with session.get('http://localhost:8000/') as resp:
        assert resp.status == 200
        json_data = await resp.json()
        assert 'status' in json_data