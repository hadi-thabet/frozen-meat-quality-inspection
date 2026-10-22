"""Copy a random sample of unlabelled training images for manual checking."""
import random
import shutil
from pathlib import Path

from inspect_data import read_labels


def sample_empty_images(root="data/raw", split="train", n=30, seed=0,
                        out_dir="results/figures/no_box_sample"):
    """Copy ``n`` random images that have no label boxes to ``out_dir``.

    Args:
        root: Dataset folder.
        split: Split to sample from.
        n: Number of images to copy.
        seed: Random seed so the same sample is drawn each run.
        out_dir: Destination folder.

    Returns:
        list[Path]: Paths of the copied images.
    """
    root = Path(root)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    empty = [p for p in sorted((root / split / "images").glob("*.jpg"))
             if not read_labels(root / split / "labels" / f"{p.stem}.txt")]
    random.Random(seed).shuffle(empty)
    chosen = empty[:n]
    for p in chosen:
        shutil.copy(p, out_dir / p.name)
    print(f"Copied {len(chosen)} of {len(empty)} unlabelled images to {out_dir}")
    return chosen

if __name__ == "__main__":
    sample_empty_images()  # 30 random unlabelled training images
    for split in ("valid", "test"):
        # n=100 is larger than either split, so every unlabelled image is copied
        sample_empty_images(split=split, n=100,
                            out_dir=f"results/figures/no_box_{split}")