# main.py

from message_formatter import leafy_frame, rainbow_wave

@leafy_frame
@rainbow_wave
def send_message(message):
    """
    A simple function that takes a message as input and returns it.
    This function is decorated with `leafy_frame` and `rainbow_wave`.
    """
    return message

if __name__ == "__main__":
    # Example usage: Print a decorated message
    print(send_message("Hello, Nature Lover! from Eshban Bahadur"))