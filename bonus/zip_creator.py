import zipfile
import pathlib


def make_archive(file_paths, des_dir):
    deth_path = pathlib.Path(des_dir, 'compressed.zip')
    with zipfile.ZipFile(deth_path, 'w') as archive:

        for file_path in file_paths:
            filepath = pathlib.Path(file_path)
            archive.write(file_path, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(file_paths=["bonus17.py"], des_dir='compressed')
