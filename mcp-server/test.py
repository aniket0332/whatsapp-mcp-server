from whatsapp import list_chats, list_messages

chats = list_messages()

print("\nChats:\n")

for chat in chats[:5]:
    print(chat)

if chats:
    first_chat = chats[0]

    print("\nMessages:\n")

    msgs = get_messages(first_chat["chat_jid"])

    for msg in msgs[:10]:
        print(msg)