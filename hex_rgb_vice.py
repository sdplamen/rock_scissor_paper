def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print('HEX value for your', rgb_to_hex(255, 165, 1))

# === === === === ===

def hex_to_rgb(ip):
    return tuple(int(ip[i:i+2],16) for i in (0, 2, 4))
hex = 'D70A51'
print('RGB value for your', hex,'is',hex_to_rgb(hex))
