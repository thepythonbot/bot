from api import token
from asos import main
from aiogram.types import ParseMode
from aiogram.utils import executor
async def on_startup( ):
    print('online')
main.button1_handler(token.dp)

if __name__ == '__main__':
    executor.start_polling(token.dp, skip_updates=True)