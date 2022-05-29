import keys
import aiohttp


class Plot:
    def __init__(self, name):
        self.name = name
        self.search = f'{keys.BASE_URL}/SearchMovie/{keys.WORKING_KEY}/{self.name}'

    async def get_id(self, session) -> str:
        async with session.get(self.search) as request:
            if request.status != 200:
                return None
            else:
                content = await request.json()
                return content['results'][0]['id']

    async def get_plot(self) -> str:
        async with aiohttp.ClientSession() as session:
            self.id = await self.get_id(session)
            if self.id is None:
                return None
            self.plot_url = f'{keys.BASE_URL}/Wikipedia/{keys.WORKING_KEY}/{self.id}'
            async with session.get(self.plot_url) as request:
                content = await request.json()
                return content["plotFull"]["plainText"]
