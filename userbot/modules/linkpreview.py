from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.ctg$")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await event.edit("```Reply to a Link.```")
        return
    if not reply_message.text:
        await event.edit("```Reply to a Link```")
        return
    chat = "@chotamreaderbot"
    await event.edit("```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "`RIP Check Your Blacklist Boss and unblock @chotamreaderbot`"
            )
            return
        if response.text.startswith(""):
            await event.edit("Am I Dumb Or Am I Dumb?")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "linkpreview": "**Plugin : **`linkpreview`\
    \n\n**Syntax : **`.ctg` reply to link\
    \n**Function : **Converts the given link to link preview"
    }
)