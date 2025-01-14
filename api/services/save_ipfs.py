import os
import time
import pexpect

PSW = "MeetDapp"
FOLDER_D = "/meetdapp-data-backend/data_storage"


class lightHouse:

    def __init__(self):
        """
        Init class
        """
        self.light = "lighthouse-web3"

    def send_data_lh(self, path: str):
        """
        This function upload data to lighthouse
        :param path:
        :return:
        """
        s_data = pexpect.spawn(f"{self.light} upload {path}", timeout=100)
        s_data.expect("Y/n")
        time.sleep(3)
        s_data.sendline("Y")
        time.sleep(3)
        s_data.expect("Enter your password:")
        time.sleep(3)
        s_data.sendline(f"{PSW}")
        time.sleep(10)
        s_data.expect("File Uploaded, visit following url to view content!")
        time.sleep(3)
        log = s_data.buffer.decode("utf-8").split()

        logs = []
        for line in log:
            logs.append(line.replace("\x1b[39m", ""))

        print(logs)

        # Pilas si no regresa bien el CID
        if len(logs) == 6:
            index_data = {"url": logs[1],
                          "CID": logs[-1]}
        else:
            index_data = {"url": logs[2].replace("\x1b[39m", ""),
                          "CID": None}

        return index_data

    def download_data_lh(self, cid: str):
        """
        This function download data from IPFS lighthouse
        :param cid:
        :return:
        """
        d_data = pexpect.spawn(f"{self.light} decrypt-file {cid}",
                                cwd=FOLDER_D,
                                timeout=100)
        d_data.expect("Enter your password:")
        d_data.sendline(f"{PSW}")
        d_data.expect("Decrypted")
        time.sleep(10)
        log = d_data.before.decode("utf-8")

        print(f"{log}")

        return log.replace("\u001b[92m", "")