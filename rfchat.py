import sys
import tty
import termios
import threading
import time
from rpi_rf import RFDevice


# Elegant shutdown
def exithandler():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    try:
        rx.cleanup()
        tx.cleanup()
    except:
        pass
    sys.exit(0)

# Activate our transmitter and received
tx = RFDevice(17)
tx.enable_tx()
rx = RFDevice(27)
rx.enable_rx()


# Receiving loop
def rec(rx):

    print("Receiving")

    lastTime = None
    while True:
        currentTime = rx.rx_code_timestamp
        if (
            currentTime != lastTime and
            (lastTime is None or currentTime - lastTime > 350000)
        ):
            lastTime = rx.rx_code_timestamp
            try:
                if (rx.rx_code == 13):  # Enter/Return Pressed
                    sys.stdout.write('\r\n')
                else:
                    sys.stdout.write(chr(rx.rx_code))
                sys.stdout.flush()
            except:
                pass

        time.sleep(0.01)

# Start receiving thread
t = threading.Thread(target=rec, args=(rx,), daemon=True)
t.start()

print("Ready to transmit")

# Remember how the shell was set up so we can reset on exit
old_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)

while True:

    # Wait for a keypress
    char = sys.stdin.read(1)

    # If CTRL-C, shutdown
    if ord(char) == 3:
        exithandler()
    else:
        # Transmit character
        tx.tx_code(ord(char))

    time.sleep(0.01)
