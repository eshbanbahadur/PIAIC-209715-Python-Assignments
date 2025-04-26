# message_formatter.py

def leafy_frame(func):
    """
    Decorator to surround the message with a frame of leaf emojis (🌿).
    The border length dynamically adjusts based on the message length.
    """
    def wrapper(message):
        # Create a border of leaves that matches the message length
        border = "🌿" * (len(message) + 4)
        # Format the message with the leafy border
        formatted_message = f"{border}\n🌿 {func(message)} 🌿\n{border}"
        return formatted_message
    return wrapper


def rainbow_wave(func):
    """
    Decorator to add rainbow emojis 🌈 before and after the message.
    This gives the message a vibrant, magical appearance.
    """
    def wrapper(message):
        # Wrap the message with rainbow emojis
        formatted_message = f"🌈 {func(message)} 🌈"
        return formatted_message
    return wrapper