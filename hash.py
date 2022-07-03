#!/usr/bin/env python3

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import timeit
import threading
import multiprocessing

Private_key = []
Ethereum_addr = []

def generate_address():
        private_key = keccak_256(token_bytes(32)).digest()
        public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
        addr = keccak_256(public_key).digest()[-20:]
        Private_key.append(private_key.hex())
        Ethereum_addr.append("0x" + str(addr.hex()))

def Timeit():
    print(timeit.timeit(
        stmt="generate_address()",
        setup="from __main__ import generate_address",
        number=20000))


def Threading():
        t1 = threading.Thread(target=Timeit)
        t2 = threading.Thread(target=Timeit)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


        with open("key.txt", "a") as file:
            for i in range(len(Ethereum_addr)):
                file.write(Private_key[i] + "\n" + Ethereum_addr[i] + "\n")
        
        file.close()

    


if __name__ == '__main__':

    for i in range(5):
        P1 = multiprocessing.Process(target=Threading)
        P2 = multiprocessing.Process(target=Threading)
        P3 = multiprocessing.Process(target=Threading)
        P4 = multiprocessing.Process(target=Threading)
        P5 = multiprocessing.Process(target=Threading)
        P1.start()
        P2.start()
        P3.start()
        P4.start()
        P5.start()
        P1.join()
        P2.join()
        P3.join()
        P4.join()
        P5.join()