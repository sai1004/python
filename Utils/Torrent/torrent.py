from qbittorrent import Client


# connect to the qbittorent Web UI
qb = Client("http://127.0.0.1:8080/")

# put the credentials (as you configured)
qb.login("admin", "adminadmin")

# open the torrent file of the file you wanna download
torrent_file = open("kali-linux-2020.1-installer-amd64.iso.torrent", "rb")

# start downloading
qb.download_from_file(torrent_file)

# you can specify the save path for downloads
qb.download_from_file(torrent_file, savepath="/root/home/Downloads")

# this magnet is not valid, replace with yours
magnet_link = "magnet:?xt=urn:btih:e334ab9ddd91c10938a7....."
qb.download_from_link(magnet_link)

# # pause all downloads
# qb.pause_all()

# # resume them
# qb.resume_all()


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


# return list of torrents
torrents = qb.torrents()

for torrent in torrents:
    print("Torrent name:", torrent["name"])
    print("hash:", torrent["hash"])
    print("Seeds:", torrent["num_seeds"])
    print("File size:", get_size_format(torrent["total_size"]))
    print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")
