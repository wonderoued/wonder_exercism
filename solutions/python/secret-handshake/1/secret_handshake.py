def commands(binary_str):

    actions = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []
    reversed_binary = binary_str[::-1]
    for i in range(4):
        if reversed_binary[i] == "1":
            handshake.append(actions[i])

    if reversed_binary[4] == "1":
        handshake.reverse()

    return handshake
