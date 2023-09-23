import os

# print(os.getcwd())


def get_disk_FreeSpace(Drive_Letter: str, size: str, round_num):
    size_dictionary = {
        "B": 1,
        "KB": 1024,
        "MB": 1024**2,
        "GB": 1024**3,
        "TB": 1024**4,
        "PB": 1024**5,
        "EB": 1024**6,
    }
    FreeSpace = int(
        os.popen(
            f"""wmic logicaldisk where "DeviceID='{Drive_Letter}'" get FreeSpace"""
        )
        .read()
        .rstrip()
        .split("\n")[-1]
    )
    result = round(FreeSpace / size_dictionary[size], round_num)
    return result


if __name__ == "__main__":
    print(get_disk_FreeSpace("G:", "GB", 2))
