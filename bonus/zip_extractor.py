import zipfile


def extractor_archive(filepath, des_dir):
    with zipfile.ZipFile(filepath) as archive:
        archive.extractall(des_dir)


if __name__ == '__main__':
    extractor_archive(r"C:\Users\aram2401\Desktop\Amplifiers\test\compressed.zip",
                      r"C:\Users\aram2401\Desktop\Amplifiers\test")
