import os

BASEDIR = os.getcwd()


class Editor:
    def __init__(self) -> None:
        self.dir_split = "\\" if os.name == 'nt' else "/"

    def rename(self, filename):
        files = [file.split for file in self.read_all_filenames()]
        if filename in files:
            os.rename(
                f"BASEDIR{self.dir_split}audio_in{self.dir_split}{filename}",
                f"BASEDIR{self.dir_split}audio_in{self.dir_split}{input('New name: ')}"
            )
        else:
            return False

    def read_all_filenames(self, overwrite: bool = True) -> list:
        input_files = [file.split(".")[0] for file in
                       os.listdir(f"{BASEDIR}{self.dir_split}audio_in{self.dir_split}")]
        if not overwrite:
            input_files = [
                i for i in input_files if i not in os.listdir(f"{BASEDIR}{self.dir_split}audio_out{self.dir_split}")
            ]
        return input_files


class Separator(Editor):
    def split(self, filename: str, stems: int) -> None:
        os.system(f"docker run -v {BASEDIR}{self.dir_split}audio_out:/output -v {BASEDIR}{self.dir_split}audio_in"
                  f":/input audiobag_spleeter separate -o /output /input/{filename} -p spleeter:{stems}stems")

    def split_all(self, overwrite: bool = False, stems: int = 3) -> None:
        for filename in self.read_all_filenames(overwrite):
            self.split(filename, stems)
            print(f"Seperated {filename} in {stems}")
