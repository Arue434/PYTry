from pynput import keyboard, mouse
import time
import threading

print("Program started...")
print("Klik mouse kiri/kanan untuk mencatat posisi.")
print("Tekan 's' untuk menghentikan program.\n")

start_time = None
running = True

def on_press(key):
    global start_time, running
    try:
        if start_time is None:
            start_time = time.time()
            print(f"[KEYBOARD] Mulai waktu pada: {key.char}")
        elif key.char == 's':
            running = False
            print("\nProgram dihentikan")
            return False  
        
    except AttributeError:
        if start_time is None:
            start_time = time.time()
            print(f"[KEYBOARD] Mulai waktu pada: {key}")

def on_click(x, y, button, pressed):
    global start_time
    if pressed:
        if start_time is None:
            start_time = time.time()
            print("[MOUSE] Timer dimulai.")
        else:
            durasi = time.time() - start_time
            print(f"[MOUSE] Klik di ({x}, {y}) setelah {durasi:.2f} detik.")

def run_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def run_mouse_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

keyboard_thread = threading.Thread(target=run_keyboard_listener)
mouse_thread = threading.Thread(target=run_mouse_listener)

keyboard_thread.start()
mouse_thread.start()

try:
    while running:
        time.sleep(0.1)
    if start_time:
        total = time.time() - start_time
        print(f"\nTotal durasi program: {total:.2f} detik.")
    print("Selesai.")
except KeyboardInterrupt:
    print("\nProgram dihentikan manual (Ctrl+C).")
