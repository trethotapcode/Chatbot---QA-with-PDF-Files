import asyncio

# Hàm bất đồng bộ để gửi tin nhắn


async def send_message():
    print("Bắt đầu gửi tin nhắn...")
    await asyncio.sleep(2)  # Giả lập thời gian chờ 2 giây
    print("Tin nhắn đã được gửi!")

# Hàm bất đồng bộ để nhận tin nhắn


async def receive_message():
    print("Bắt đầu nhận tin nhắn...")
    await asyncio.sleep(3)  # Giả lập thời gian chờ 3 giây
    print("Tin nhắn đã được nhận!")

# Hàm chính để chạy hai tác vụ trên


async def main():
    print("Bắt đầu trò chuyện...")

    # Chạy cả hai tác vụ gửi và nhận tin nhắn đồng thời
    await asyncio.gather(send_message(), receive_message())

    print("Kết thúc trò chuyện!")

# Chạy hàm chính
asyncio.run(main())
