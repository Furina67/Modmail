async def send_files(dest, attachments):
    if attachments:
        files = [await a.to_file() for a in attachments]
        await dest.send(files=files)