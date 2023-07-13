from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv("TOKEN"))