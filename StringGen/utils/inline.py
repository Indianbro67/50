from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝙲𝚘𝚗𝚗𝚎𝚌𝚝 𝚃𝚘 𝙱𝚘𝚝", callback_data="pyrogram")],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=https://t.me/adult_updates),
            InlineKeyboardButton(
                text="𝚐𝚛𝚘𝚞𝚙", url="https://t.me/adult_girls_chatting_groupp"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
