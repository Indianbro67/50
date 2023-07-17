from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"Hey {message.from_user.first_name}\n\nWelcome to {Anony.mention}\n\n๏ To Save To Timer Photos And Timer Video\n𝙲𝚘𝚗𝚗𝚎𝚌𝚝 𝚃𝚘 𝙱𝚘𝚝\n\nBy @Black_Devil_Admin.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
