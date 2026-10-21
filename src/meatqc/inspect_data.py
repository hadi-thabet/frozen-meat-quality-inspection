"""Inspect a YOLO-format object-detection dataset (as exported by Roboflow).

Reports, for each split (train / valid / test): number of images, number of
boxes per class, images with no defects, and image sizes. These numbers
define the real inputs of the project and reveal class imbalance.
"""
from collections import Counter
from pathlib import Path

import cv2
import yaml

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp"}


def load_class_names(root):
    """Read the class names from the dataset's ``data.yaml``.

    Args:
        root: Dataset folder containing ``data.yaml``.

    Returns:
        list[str]: Class names, indexed by class id.

    Raises:
        FileNotFoundError: If ``data.yaml`` is missing.
    """
    yaml_path = Path(root) / "data.yaml"
    if not yaml_path.exists():
        raise FileNotFoundError(f"{yaml_path} not found")
    with open(yaml_path) as f:
        cfg = yaml.safe_load(f)
    names = cfg["names"]
    if isinstance(names, dict):  # some exports store {0: 'name', ...}
        names = [names[k] for k in sorted(names)]
    return list(names)


def read_labels(label_path):
    """Parse one YOLO label file.

    Each line is ``class x_center y_center width height``, with the four
    coordinates normalised to the range 0-1.

    Args:
        label_path: Path to a ``.txt`` label file.

    Returns:
        list[tuple]: ``(class_id, x, y, w, h)`` per box. Empty if the file
        is missing or contains no boxes. Malformed lines are skipped.
    """
    label_path = Path(label_path)
    if not label_path.exists():
        return []
    boxes = []
    for line in label_path.read_text().splitlines():
        parts = line.split()
        if len(parts) < 5:
            continue  # skip malformed lines rather than crash
        boxes.append((int(parts[0]), *map(float, parts[1:5])))
    return boxes


def inspect_dataset(root="data/raw", splits=("train", "valid", "test"),
                    size_sample=50):
    """Print a summary of each split of the dataset.

    Args:
        root: Dataset folder containing ``data.yaml`` and split folders.
        splits: Split folder names to inspect.
        size_sample: Number of images per split opened to check dimensions.

    Returns:
        None. Results are printed to the terminal.
    """
    root = Path(root)
    names = load_class_names(root)
    print(f"Classes ({len(names)}): {names}")

    for split in splits:
        img_dir = root / split / "images"
        lbl_dir = root / split / "labels"
        if not img_dir.exists():
            print(f"\n[{split}] folder not found, skipping")
            continue

        images = sorted(p for p in img_dir.iterdir()
                        if p.suffix.lower() in IMAGE_EXTS)
        class_counts = Counter()
        no_defect = 0
        for img in images:
            boxes = read_labels(lbl_dir / f"{img.stem}.txt")
            if not boxes:
                no_defect += 1
            class_counts.update(b[0] for b in boxes)

        sizes = Counter()
        for img in images[:size_sample]:
            im = cv2.imread(str(img))
            if im is not None:
                h, w = im.shape[:2]
                sizes[(w, h)] += 1

        total_boxes = sum(class_counts.values())
        print(f"\n[{split}] {len(images)} images, {total_boxes} boxes, "
              f"{no_defect} images with no boxes")
        for cid in sorted(class_counts):
            print(f"  {names[cid]:<16} {class_counts[cid]}")
        print(f"  image sizes (first {size_sample}): {dict(sizes)}")


if __name__ == "__main__":
    inspect_dataset()
