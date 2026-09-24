"""
main.py
~~~~~~~~

With this file, I can be able to run the whole project at once.
Basically, it connected to data loader, train and test fodlers
at the same time.
"""

from dataloader.load_video import LoadVideo
import configs as get

def main():
    loader = LoadVideo(get.video_data, get.path_to_processed_data)
    n = loader.make_frames()
    print(f"Saved {n} frames")


if __name__ == "__main__":
    main()