def get_sin(x):
    x = x % 6.28
    return x - x**3/6 + x**5/120 - x**7/5040

def get_cos(x):
    x = x % 6.28
    return 1 - x**2/2 + x**4/24 - x**6/720

# Settings
A, B = 0, 0  # Rotation angles
chars = ".,-~:;=!*#$@" # Shading levels (Light to Dark)

print("\033[2J") # Clear terminal screen

while True:
    # Buffers to store the "pixels" and the depth (z-buffer)
    b = [' '] * 1760 
    z = [0] * 1760
    
    # Mathematical loops to create the donut shape
    j = 0
    while j < 6.28:
        j += 0.07
        i = 0
        while i < 6.28:
            i += 0.02
            
            sin_i, cos_i = get_sin(i), get_cos(i)
            sin_j, cos_j = get_sin(j), get_cos(j)
            sin_A, cos_A = get_sin(A), get_cos(A)
            sin_B, cos_B = get_sin(B), get_cos(B)
            
            h = cos_j + 2
            D = 1 / (sin_i * h * sin_A + sin_j * cos_A + 5)
            t = sin_i * h * cos_A - sin_j * sin_A
            
            # Projecting 3D coordinates to 2D screen space
            x = int(40 + 30 * D * (cos_i * h * cos_B - t * sin_B))
            y = int(12 + 15 * D * (cos_i * h * sin_B + t * cos_B))
            o = x + 80 * y
            
            # Lighting calculation (Normal vector)
            N = int(8 * ((sin_j * sin_A - sin_i * cos_j * cos_A) * cos_B - sin_i * cos_j * sin_A - sin_j * cos_A - cos_i * cos_j * sin_B))
            
            if 22 > y > 0 and 80 > x > 0 and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    # Print the frame
    print("\033[H", end="") # Move cursor to top
    for k in range(1761):
        print(b[k] if k % 80 else '\n', end="")
    
    # Increment rotation for the next frame
    A += 0.04
    B += 0.02