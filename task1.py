import argparse
import os
import pathlib
import shutil

def strange_copy(input_dir, output_dir):
    with os.scandir(input_dir) as entries:
        for entry in entries:
            if entry.is_dir():
                strange_copy(entry.path, output_dir)
            elif entry.is_file():
                try:
                    _, file_extension = os.path.splitext(entry.name)
                    pathlib.Path(f"{output_dir}/{file_extension[1:]}").mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(entry.path, output_dir + '/' + file_extension[1:] + '/' + entry.name)
                except:
                    print(f"ERROR: Failed to copy {entry.path} to {output_dir}/{file_extension[1:]}")

def main():
    parser = argparse.ArgumentParser(description='Strange file copying')
    parser.add_argument('-i', '--input', required=True, type=str, help='Input dir')
    parser.add_argument('-o', '--output', type=str, default="dist", help='Output dir (default: "dist")')
    args = parser.parse_args()
    strange_copy(args.input, args.output)

if __name__ == "__main__":
    main()