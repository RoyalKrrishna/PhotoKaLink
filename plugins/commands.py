import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name}😚,\n\n<b>I Can Upload Your Images Or Videos From\nTelegram To Telegra.ph And Send You A Link.🔗\n\nCreated By @RoyalKrrishna 🕵️\nClick /help For More.❗</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>Send Me Or Forward Me Any Of Your Photos Or Videos,\nI'll Upload It To Telegra.ph And Provide You A Link.🔗\n\nListen Please:- 🔞+ Contents Are Not Allowed And You Can Upload Only 5MB Files At Once❗\nSo It's Better To Upload Only Images.🖼️\n\nCreated By @RoyalKrrishna</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong!\nSend Photo/Video Again Or Contact <b>@RoyalKrrishna 🕵️</b>")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact <b>@Royalkrrishna 🕵️</b>")
        return
    await dwn.edit_text
       (f"https://telegra.ph{response[0]}",disable_web_page_preview=True)
    try:
        os.remove(viddir)
    except:
        pass
