from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def collector_kb(jid:str):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ Done',callback_data=f'done:{jid}'),InlineKeyboardButton(text='❌ Cancel',callback_data=f'cancel:{jid}')]])
