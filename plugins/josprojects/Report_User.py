#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pyrogram
import asyncio
import os
from pyrogram import filters, Client as beta

@beta.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        success = False
        report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        for admin in admins:
            try:
                reported_post = await message.reply_to_message.forward(admin.user.id)
                await reported_post.reply_text(
                    text=report,
                    chat_id=admin.user.id,
                    disable_web_page_preview=True
                )
                success = True
            except:
                pass
        if success:
            await message.reply_text("𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝖽 𝗍𝗈 𝖠𝖽𝗆𝗂𝗇𝗌!")
