# Don't Remove Credit @Illegal_Developer
# Subscribe YouTube Channel For Amazing Bot @Illegal_Developer
# Ask Doubt on telegram @Illegal_Developer

import pyrogram
import os
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize Pyrogram Client
try:
    app_id = int(os.environ.get("app_id", "23990433"))
except Exception as app_id:
    print(f"⚠️ App ID Invalid {app_id}")

try:
    api_hash = os.environ.get("api_hash", "e6c4b6ee1933711bc4da9d7d17e1eb20")
except Exception as api_id:
    print(f"⚠️ Api Hash Invalid {api_hash}")

try:
    bot_token = os.environ.get("bot_token", "5992501587:AAHdDLpHnleGcpCQUizT1efHLhDNYUrtuYA")
except Exception as bot_token:
    print(f"⚠️ Bot Token Invalid {bot_token}")

try:
    custom_caption = os.environ.get("custom_caption", """ 
    <b>{file_name} ~ @missqueenbotx</b>""")
except Exception as custom_caption:
    print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBotV1 = pyrogram.Client(
    name="AutoCaptionBotV1", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

# Start and About Messages
start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>Maintained By : @Illegal_Developer</b>"""

about_message = """
<b>• Name : <a href=https://t.me/Illegal_Developer>AutoCaption</a></b>
<b>• Developer : <a href=https://t.me/Illegal_Developer>ɪʟʟᴇɢᴀʟ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/Illegal_Developer>Click Here</a></b>"""

# Start command
@AutoCaptionBotV1.on_message(filters.private & filters.command(["start"]))
def start_command(bot, update):
    update.reply(start_message.format(update.from_user.mention),
                 reply_markup=start_buttons(bot, update),
                 parse_mode=pyrogram.enums.ParseMode.HTML,
                 disable_web_page_preview=True)

# Start callback
@AutoCaptionBotV1.on_callback_query(filters.regex("start"))
def strat_callback(bot, update):
    update.message.edit(start_message.format(update.from_user.mention),
                        reply_markup=start_buttons(bot, update.message),
                        parse_mode=pyrogram.enums.ParseMode.HTML,
                        disable_web_page_preview=True)

# About callback
@AutoCaptionBotV1.on_callback_query(filters.regex("about"))
def about_callback(bot, update):
    bot = bot.get_me()
    update.message.edit(about_message.format(version=pyrogram.__version__,
                                              username=bot.mention),
                        reply_markup=about_buttons(bot, update.message),
                        parse_mode=pyrogram.enums.ParseMode.HTML,
                        disable_web_page_preview=True)

# Edit caption in channel
@AutoCaptionBotV1.on_message(filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
    motech, _ = get_file_details(update)
    try:
        try:
            update.edit(custom_caption.format(file_name=motech.file_name))
        except pyrogram.errors.FloodWait as FloodWait:
            asyncio.sleep(FloodWait.value)
            update.edit(custom_caption.format(file_name=motech.file_name))
    except pyrogram.errors.MessageNotModified:
        pass

# Replace texts dictionary
replace_texts = {}

# Update replace command
@AutoCaptionBotV1.on_message(filters.private & filters.command("update_replace"))
async def update_replace_command(bot, update):
    await update.reply("➸ To update current replace texts, click update replace and send the new replace text.")

# Handle replace text
@AutoCaptionBotV1.on_message(filters.private & filters.regex(r"Replace words : (.+)"))
async def handle_replace_text(bot, update):
    replace_text = update.matches[0].group(1)
    replace_pairs = [pair.split(":") for pair in replace_text.split("|")]

    for old, new in replace_pairs:
        replace_texts[old] = new

    await update.reply("➸ Replace texts updated successfully!")

# Delete replace command
@AutoCaptionBotV1.on_message(filters.private & filters.command("delete_replace"))
async def delete_replace_command(bot, update):
    replace_texts.clear()
    await update.reply("➸ Replace texts deleted successfully!")

# ... (your existing code)

@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
async def process_file_caption(bot, update):
    # Extract file name
    file_name = "www.1tamilmv.phd - some name - hevc @channel_name.mkv"  # Replace with your logic to get the file name

    # Remove .mkv and .mp4 automatically
    file_name = file_name.replace(".mkv", "").replace(".mp4", "")

    # Replace words based on user-defined replace_texts
    for old, new in replace_texts.items():
        file_name = file_name.replace(old, new)

    # Your existing logic to handle the caption
    try:
        # Assuming you have a function to edit the caption
        await edit_caption(update, file_name)
    except Exception as e:
        print(f"Error editing caption: {e}")

async def edit_caption(update, file_name):
    # Your existing logic to edit the caption
    # ...

# ... (your existing code)

# Get file details function (continued)
def get_file_details(update: pyrogram.types.Message):
    if update.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(update, message_type)
            if obj:
                return obj, obj.file_id

# ... (your existing code)

print("Telegram AutoCaption V1 Bot Start")
print("Bot Created By https://t.me/Illegal_Developer")

AutoCaptionBotV1.run()
